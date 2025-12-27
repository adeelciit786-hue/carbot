import streamlit as st
import json
from PIL import Image
from io import BytesIO

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title='🚗 Car Posting Bot',
    page_icon='🚗',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# ==================== CUSTOM STYLING ====================
st.markdown('''
    <style>
    /* Remove default padding and margins */
    .main {
        padding: 0;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px 20px;
        text-align: center;
        margin: -70px -50px 30px -50px;
    }
    
    .header-container h1 {
        color: white;
        font-size: 2.5em;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-container p {
        color: rgba(255,255,255,0.9);
        font-size: 1.1em;
        margin: 10px 0 0 0;
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    
    /* Section headings */
    .section-title {
        color: #667eea;
        font-size: 1.5em;
        margin-bottom: 20px;
        font-weight: bold;
    }
    
    /* Info grid */
    .info-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin: 20px 0;
    }
    
    .info-item {
        background: #f8f8f8;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    
    .info-label {
        color: #999;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    
    .info-value {
        color: #333;
        font-size: 18px;
        font-weight: 600;
    }
    
    /* Selling angle box */
    .selling-angle {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
        margin: 20px 0;
    }
    
    /* Category badge */
    .category-badge {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        margin-bottom: 20px;
    }
    
    /* Content box */
    .content-box {
        background: #f8f8f8;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 15px 0;
        font-family: 'Courier New', monospace;
        font-size: 13px;
        white-space: pre-wrap;
        word-wrap: break-word;
        line-height: 1.6;
        max-height: 500px;
        overflow-y: auto;
    }
    
    /* Success message */
    .success-msg {
        background: #efe;
        color: #3c3;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #3c3;
        margin-bottom: 20px;
        font-weight: 600;
    }
    
    /* Error message */
    .error-msg {
        background: #fee;
        color: #c33;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #c33;
        margin-bottom: 20px;
    }
    
    /* Tabs styling */
    .tab-buttons {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
        border-bottom: 2px solid #e0e0e0;
        flex-wrap: wrap;
    }
    
    .tab-btn {
        padding: 12px 20px;
        background: none;
        border: none;
        border-bottom: 3px solid transparent;
        color: #666;
        cursor: pointer;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .tab-btn.active {
        color: #667eea;
        border-bottom-color: #667eea;
    }
    
    /* Chat section */
    .chat-container {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    
    /* Features list */
    .features-list {
        background: #f8f8f8;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .feature-item {
        padding: 8px 0;
        color: #333;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .feature-item:last-child {
        border-bottom: none;
    }
    
    .feature-item:before {
        content: "✓ ";
        color: #667eea;
        font-weight: bold;
        margin-right: 8px;
    }
    
    /* Message styling */
    .user-message {
        background: #667eea;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: right;
    }
    
    .assistant-message {
        background: #f0f0f0;
        color: #333;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: left;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .info-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .header-container h1 {
            font-size: 1.8em;
        }
    }
    </style>
    ''', unsafe_allow_html=True)

# ==================== MODULE IMPORTS ====================
bot = None
chat_assist = None
image_processor = None

try:
    from car_bot import CarPostingBot, CarCategory
    bot = CarPostingBot()
except Exception as e:
    st.error(f'🚗 Car Bot Error: {str(e)[:50]}')

try:
    from chat_assistant import ChatAssistant
    chat_assist = ChatAssistant()
except Exception as e:
    st.error(f'💬 Chat Error: {str(e)[:50]}')

try:
    from image_processor import CarImageProcessor
    image_processor = CarImageProcessor()
except Exception as e:
    st.error(f'🖼️ Image Processor Error: {str(e)[:50]}')

# ==================== SESSION STATE ====================
if 'car_post_result' not in st.session_state:
    st.session_state.car_post_result = None
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = 'caption'
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# ==================== HEADER ====================
st.markdown('''
    <div class="header-container">
        <h1>🚗 CAR POSTING BOT</h1>
        <p>Generate Perfect Facebook Posts in Seconds</p>
    </div>
    ''', unsafe_allow_html=True)

# ==================== MAIN LAYOUT ====================
col1, col2 = st.columns(2)

# ==================== LEFT COLUMN - INPUT ====================
with col1:
    st.markdown('<div class="section-title">📝 Enter Car Description</div>', unsafe_allow_html=True)
    
    car_description = st.text_area(
        'Car Description',
        placeholder='''Paste or type your complete car description here...

Example:
2018 Jeep Compass TrailHawk GCC with a 2.4L 4-cylinder in Good Condition 

It has been driven only 103,000 kilometers and is free from any issues or faults.

The car comes with a 2.4L 4-cylinder engine that provides around 700 kilometers per full tank. It also has brand-new tires installed.

This is a mid-option model with features such as leather seats, cruise control, alloy rims, DRL, fog lamps, parking sensors, Bluetooth, AUX, 4x4, push-button start, keyless entry, electronic handbrake, and a touch screen display.

I am selling this car for just 30,000 AED.''',
        height=450,
        label_visibility='collapsed'
    )
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        process_btn = st.button('🚀 Generate Post', use_container_width=True, type='primary')
    with col_btn2:
        clear_btn = st.button('🗑️ Clear', use_container_width=True)
    
    if clear_btn:
        st.session_state.car_post_result = None
        st.rerun()

# ==================== RIGHT COLUMN - OUTPUT ====================
with col2:
    st.markdown('<div class="section-title">✨ Generated Post</div>', unsafe_allow_html=True)
    
    if process_btn:
        if not car_description.strip():
            st.error('❌ Please enter a car description')
        else:
            with st.spinner('⏳ Processing car information...'):
                if bot:
                    try:
                        result = bot.generate_full_post(car_description)
                        st.session_state.car_post_result = result
                        st.rerun()
                    except Exception as e:
                        st.error(f'❌ Error: {str(e)}')
                else:
                    st.error('❌ Car Bot module not loaded')
    
    # Display output if available
    if st.session_state.car_post_result:
        result = st.session_state.car_post_result
        
        if result.get('success'):
            st.markdown('<div class="success-msg">✅ Car posting generated successfully!</div>', unsafe_allow_html=True)
            
            post = result
            car_info = result.get('car_info', {})
            
            # Selling angle
            st.markdown(
                f'<div class="selling-angle">💡 {post.get("selling_angle", "Quality Vehicle")}</div>',
                unsafe_allow_html=True
            )
            
            # Category badge
            st.markdown(
                f'<div class="category-badge">🏷️ {post.get("category", "N/A")}</div>',
                unsafe_allow_html=True
            )
            
            # Car info grid
            info_html = '<div class="info-grid">'
            info_html += f'''<div class="info-item">
                <div class="info-label">Make & Model</div>
                <div class="info-value">{car_info.get("make_model", "N/A")}</div>
            </div>'''
            info_html += f'''<div class="info-item">
                <div class="info-label">Year</div>
                <div class="info-value">{car_info.get("year", "N/A")}</div>
            </div>'''
            info_html += f'''<div class="info-item">
                <div class="info-label">Mileage</div>
                <div class="info-value">{f"{car_info.get('mileage', 0):,} km" if car_info.get('mileage') else "N/A"}</div>
            </div>'''
            info_html += f'''<div class="info-item">
                <div class="info-label">Price</div>
                <div class="info-value">AED {f"{car_info.get('asking_price', 0):,}" if car_info.get('asking_price') else "Contact"}</div>
            </div>'''
            info_html += f'''<div class="info-item">
                <div class="info-label">Engine</div>
                <div class="info-value">{car_info.get("engine", "N/A")}</div>
            </div>'''
            info_html += f'''<div class="info-item">
                <div class="info-label">Transmission</div>
                <div class="info-value">{car_info.get("transmission", "N/A")}</div>
            </div>'''
            info_html += '</div>'
            st.markdown(info_html, unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-msg">⚠️ Validation Failed</div>', unsafe_allow_html=True)
            for error in result.get('errors', []):
                st.error(f'✗ {error}')

# ==================== TABS SECTION ====================
if st.session_state.car_post_result and st.session_state.car_post_result.get('success'):
    st.divider()
    
    post = st.session_state.car_post_result
    
    # Tab selection
    tabs = ['📄 Caption', '🏷️ Hashtags', '✨ Features', '📱 Posting Guide', '💬 Inquiry Script', '✅ Delivery Script']
    selected_tab = st.radio('Select content:', tabs, horizontal=True, label_visibility='collapsed')
    
    st.markdown('---')
    
    if selected_tab == '📄 Caption':
        st.subheader('Copy-Paste Caption for Facebook')
        caption_text = post.get('caption', '')
        st.markdown(f'<div class="content-box">{caption_text}</div>', unsafe_allow_html=True)
        st.text_area('Copy caption:', value=caption_text, height=250, disabled=True, label_visibility='collapsed')
        col_copy = st.columns([1, 3])[0]
        with col_copy:
            st.button('📋 Copy Caption', key='copy_caption', use_container_width=True)
    
    elif selected_tab == '🏷️ Hashtags':
        st.subheader('Ready-to-Use Hashtags')
        hashtags_text = post.get('hashtags', '')
        st.markdown(f'<div class="content-box">{hashtags_text}</div>', unsafe_allow_html=True)
        st.text_area('Copy hashtags:', value=hashtags_text, height=150, disabled=True, label_visibility='collapsed')
        col_copy = st.columns([1, 3])[0]
        with col_copy:
            st.button('📋 Copy Hashtags', key='copy_hashtags', use_container_width=True)
    
    elif selected_tab == '✨ Features':
        st.subheader('Car Features')
        features_text = post.get('features_summary', '')
        st.markdown(f'<div class="content-box">{features_text}</div>', unsafe_allow_html=True)
    
    elif selected_tab == '📱 Posting Guide':
        st.subheader('Platform Posting Instructions')
        posting_text = post.get('posting_instructions', '')
        st.markdown(f'<div class="content-box">{posting_text}</div>', unsafe_allow_html=True)
    
    elif selected_tab == '💬 Inquiry Script':
        st.subheader('Buyer Inquiry Response Script')
        inquiry_text = post.get('inquiry_script', '')
        st.markdown(f'<div class="content-box">{inquiry_text}</div>', unsafe_allow_html=True)
        st.text_area('Copy script:', value=inquiry_text, height=300, disabled=True, label_visibility='collapsed')
        col_copy = st.columns([1, 3])[0]
        with col_copy:
            st.button('📋 Copy Script', key='copy_inquiry', use_container_width=True)
    
    elif selected_tab == '✅ Delivery Script':
        st.subheader('Post-Delivery Social Proof Script')
        delivery_text = post.get('delivery_script', '')
        st.markdown(f'<div class="content-box">{delivery_text}</div>', unsafe_allow_html=True)
        st.text_area('Copy script:', value=delivery_text, height=300, disabled=True, label_visibility='collapsed')
        col_copy = st.columns([1, 3])[0]
        with col_copy:
            st.button('📋 Copy Script', key='copy_delivery', use_container_width=True)

# ==================== CHAT SECTION ====================
st.divider()
st.markdown('<div class="chat-container" style="margin-top: 30px;">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💬 AI Chat Assistant</div>', unsafe_allow_html=True)
st.write('Paste customer messages and get smart, humanized responses instantly')

chat_col1, chat_col2 = st.columns([3, 1])

with chat_col1:
    customer_message = st.text_area(
        'Customer Message',
        placeholder='''Paste the customer's message here...

Example: Hi, what's the lowest price for this car? Can I view it tomorrow?

💡 Tip: Press Enter to submit''',
        height=120,
        label_visibility='collapsed'
    )

with chat_col2:
    generate_response = st.button('🤖 Generate\nResponse', use_container_width=True, type='primary', key='gen_response')

if generate_response:
    if not customer_message.strip():
        st.error('❌ Please enter a customer message')
    else:
        if chat_assist:
            with st.spinner('⏳ Generating response...'):
                try:
                    response = chat_assist.get_response(customer_message)
                    st.session_state.chat_history.append({
                        'role': 'user',
                        'content': customer_message
                    })
                    st.session_state.chat_history.append({
                        'role': 'assistant',
                        'content': response
                    })
                    st.rerun()
                except Exception as e:
                    st.error(f'❌ Error: {str(e)}')
        else:
            st.error('❌ Chat Assistant not loaded')

# Display chat history
if st.session_state.chat_history:
    st.markdown('---')
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f'<div class="user-message"><strong>You:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message"><strong>Assistant:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)
    
    if st.button('🗑️ Clear Chat History', use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# ==================== FOOTER ====================
st.divider()
st.markdown(
    '<div style="text-align: center; color: #666; margin-top: 40px; padding: 20px;">'
    '<p>🚗 Car Posting Bot | <a href="https://github.com/adeelciit786-hue/carbot">GitHub Repository</a> | '
    '<a href="http://localhost:5000">Flask Version</a></p>'
    '<p style="font-size: 12px; margin-top: 10px;">Version 2.0 | Exact Clone of Localhost Flask App</p>'
    '</div>',
    unsafe_allow_html=True
)
