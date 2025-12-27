from flask import Flask, render_template, request, jsonify
from car_bot import CarPostingBot
from chat_assistant import get_chat_response, get_api_status
from image_processor import CarImageProcessor
from werkzeug.utils import secure_filename
from functools import lru_cache
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max upload
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'webp'}

# Lazy load modules
_bot = None
_image_processor = None

def get_bot():
    """Lazy load bot module"""
    global _bot
    if _bot is None:
        _bot = CarPostingBot()
    return _bot

def get_image_processor():
    """Lazy load image processor"""
    global _image_processor
    if _image_processor is None:
        _image_processor = CarImageProcessor()
    return _image_processor

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/process-car', methods=['POST'])
def process_car():
    """API endpoint to process car description with comprehensive error handling"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'success': False,
                'errors': ['Invalid JSON format']
            }), 400
            
        description = data.get('description', '').strip()
        
        # Validation
        if not description:
            return jsonify({
                'success': False,
                'errors': ['Please enter a car description']
            }), 400
        
        if len(description) < 20:
            return jsonify({
                'success': False,
                'errors': ['Description too short - please provide more details (minimum 20 characters)']
            }), 400
        
        if len(description) > 5000:
            return jsonify({
                'success': False,
                'errors': ['Description too long - please keep it under 5000 characters']
            }), 400
        
        bot = get_bot()
        result = bot.generate_full_post(description)
        
        if result['success']:
            return jsonify({
                'success': True,
                'data': {
                    'selling_angle': result['selling_angle'],
                    'category': result['category'],
                    'caption': result['caption'],
                    'hashtags': result['hashtags'],
                    'features': result['features_summary'],
                    'posting_instructions': result['posting_instructions'],
                    'inquiry_script': result['inquiry_script'],
                    'delivery_script': result['delivery_script'],
                    'car_info': {
                        'make_model': result['car_info']['make_model'],
                        'year': result['car_info']['year'],
                        'mileage': result['car_info']['mileage'],
                        'price': result['car_info']['asking_price'],
                        'engine': result['car_info']['engine'],
                        'transmission': result['car_info']['transmission']
                    }
                }
            })
        else:
            # Ensure errors is a list
            errors = result.get('errors', [])
            if not isinstance(errors, list):
                errors = [str(errors)] if errors else ['An error occurred']
            
            # Filter out None/undefined values
            errors = [str(e) if e else 'Unknown error' for e in errors if e]
            
            return jsonify({
                'success': False,
                'errors': errors,
                'message': result.get('message', 'An error occurred')
            }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'errors': [f'Error processing description: {str(e)}']
        }), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for AI chat assistant"""
    data = request.get_json()
    customer_message = data.get('message', '').strip()
    car_info = data.get('car_info')
    
    if not customer_message:
        return jsonify({
            'success': False,
            'error': 'Please enter a customer message'
        }), 400
    
    try:
        result = get_chat_response(customer_message, car_info)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error generating response: {str(e)}'
        }), 500

@app.route('/api/chat-status', methods=['GET'])
def chat_status():
    """Get chat assistant status and API configuration"""
    return jsonify(get_api_status())

@app.route('/api/image-backgrounds', methods=['GET'])
def image_backgrounds():
    """Get available background presets"""
    try:
        backgrounds = image_processor.get_preset_backgrounds()
        return jsonify({
            'success': True,
            'backgrounds': backgrounds
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚗 CAR POSTING BOT - LOCALHOST SERVER")
    print("="*70)
    print("\n✅ Server starting...")
    print("📍 Open your browser: http://localhost:5000")
    print("📝 Note: Auto-reload is disabled for stability")
    print("   → Restart the server if you make code changes")
    print("\n" + "="*70 + "\n")
    # Disable debug mode to prevent auto-restarts that cause crashes
    app.run(debug=False, port=5000, use_reloader=False)
