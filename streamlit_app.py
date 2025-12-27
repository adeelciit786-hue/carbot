import streamlit as st
import json
import os
from PIL import Image
from io import BytesIO
from pathlib import Path

# Page configuration - MATCHES LOCALHOST
st.set_page_config(
    page_title='Car Posting Bot',
    page_icon='🚗',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom styling - MATCHES LOCALHOST APPEARANCE
st.markdown('''
    <style>
    .main {
        padding: 1rem;
    }
    .stTabs [data-baseweb=tab-list] button {
        font-size: 18px;
        font-weight: bold;
    }
    .car-info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    .info-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
        margin: 10px 0;
    }
    .info-item {
        background: #f0f2f6;
        padding: 12px;
        border-radius: 8px;
        border-left: 4px solid #667eea;
    }
    .info-label {
        font-weight: bold;
        color: #667eea;
        font-size: 12px;
        text-transform: uppercase;
    }
    .info-value {
        font-size: 18px;
        color: #333;
        margin-top: 5px;
    }
    .caption-box {
        background: #f9f9f9;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 10px 0;
    }
    .feature-list {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin: 15px 0;
    }
    .feature-item {
        background: #667eea;
        color: white;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 14px;
    }
    </style>
    ''', unsafe_allow_html=True)

# Load modules locally with error handling
bot = None
chat_assist = None
image_processor = None

try:
    from car_bot import CarPostingBot, CarCategory
    bot = CarPostingBot()
except Exception as e:
    st.warning(f'🚗 Car Bot not available: {str(e)[:50]}')

try:
    from chat_assistant import ChatAssistant
    chat_assist = ChatAssistant()
except Exception as e:
    st.warning(f'💬 Chat Assistant not available: {str(e)[:50]}')

try:
    from image_processor import CarImageProcessor
    image_processor = CarImageProcessor()
except Exception as e:
    st.warning(f'🖼️ Image Processor not available: {str(e)[:50]}')

# Initialize session state
if 'car_post' not in st.session_state:
    st.session_state.car_post = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None

# Header
st.markdown('# 🚗 Car Posting Bot Dashboard')
st.markdown('**Create optimized car sales posts with AI-powered descriptions and chat assistance**')
st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(['🚗 Car Post Generator', '💬 Chat Assistant', '🖼️ Image Processing', 'ℹ️ About'])

# ============== TAB 1: CAR POST GENERATOR ==============
with tab1:
    st.subheader('⚡ Generate AI-Optimized Car Posts')
    
    if not bot:
        st.error('🚗 Car Bot module not loaded. Please check the logs.')
    else:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown('### 📝 Enter Car Details')
            car_description = st.text_area(
                'Car Description',
                placeholder='e.g., 2020 Toyota Camry, 45000 miles, white, excellent condition, automatic transmission, leather seats...',
                height=150,
                help='Provide detailed information about the car'
            )
        
        with col2:
            st.markdown('### ✨ Features')
            st.info(
                """
                ✅ Psychology-optimized descriptions
                ✅ Conversion-focused messaging
                ✅ Urgency & scarcity triggers
                ✅ Emotional appeal
                ✅ Category-specific templates
                ✅ Auto-generated hashtags
                """,
                icon="⭐"
            )
        
        st.divider()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button('🚀 Generate Car Post', use_container_width=True, type='primary'):
                if not car_description.strip():
                    st.error('❌ Please enter a car description')
                else:
                    with st.spinner('⏳ Generating optimized post...'):
                        try:
                            result = bot.generate_full_post(car_description)
                            
                            if result['success']:
                                st.session_state.car_post = result
                                st.success('✅ Post generated successfully!')
                            else:
                                st.error(f"❌ Error: {result.get('message', 'Unknown error')}")
                                for error in result.get('errors', []):
                                    st.error(f"   {error}")
                        except Exception as e:
                            st.error(f'❌ Error: {str(e)}')
        
        # Display the generated post
        if st.session_state.car_post and st.session_state.car_post.get('success'):
            st.divider()
            st.markdown('---')
            
            post = st.session_state.car_post
            car_info = post.get('car_info', {})
            
            # SELLING ANGLE - PROMINENT
            st.markdown(
                f'<div class="car-info-box"><h2>💡 {post.get("selling_angle", "Quality Vehicle")}</h2></div>',
                unsafe_allow_html=True
            )
            
            # CAR INFO GRID
            st.markdown('### 📊 Car Information')
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown('<div class="info-item"><div class="info-label">Make & Model</div><div class="info-value">' + 
                           f'{car_info.get("make_model", "N/A")}</div></div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="info-item"><div class="info-label">Year</div><div class="info-value">' + 
                           f'{car_info.get("year", "N/A")}</div></div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="info-item"><div class="info-label">Mileage</div><div class="info-value">' + 
                           f'{car_info.get("mileage", "N/A"):,} km</div></div>', unsafe_allow_html=True)
            with col4:
                st.markdown('<div class="info-item"><div class="info-label">Price</div><div class="info-value">' + 
                           f'AED {car_info.get("asking_price", 0):,}</div></div>', unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown('<div class="info-item"><div class="info-label">Engine</div><div class="info-value">' + 
                           f'{car_info.get("engine", "N/A")}</div></div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="info-item"><div class="info-label">Transmission</div><div class="info-value">' + 
                           f'{car_info.get("transmission", "N/A")}</div></div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="info-item"><div class="info-label">Condition</div><div class="info-value">' + 
                           f'{car_info.get("condition", "Good")}</div></div>', unsafe_allow_html=True)
            with col4:
                st.markdown('<div class="info-item"><div class="info-label">Category</div><div class="info-value">' + 
                           f'{post.get("category", "N/A")}</div></div>', unsafe_allow_html=True)
            
            # FEATURES
            if car_info.get('features'):
                st.markdown('### 🎯 Key Features')
                features_html = '<div class="feature-list">'
                for feature in car_info.get('features', []):
                    features_html += f'<div class="feature-item">{feature}</div>'
                features_html += '</div>'
                st.markdown(features_html, unsafe_allow_html=True)
            
            st.divider()
            
            # TABS FOR DIFFERENT CONTENT
            post_tab1, post_tab2, post_tab3, post_tab4, post_tab5, post_tab6 = st.tabs(
                ['📝 Caption', '#️⃣ Hashtags', '💪 Features', '📋 Posting Guide', '💬 Inquiry Script', '🚚 Delivery Script']
            )
            
            with post_tab1:
                st.markdown('### Facebook Caption')
                caption_text = post.get('caption', '')
                st.markdown(f'<div class="caption-box">{caption_text}</div>', unsafe_allow_html=True)
                st.text_area('Copy caption:', value=caption_text, height=250, disabled=True)
                st.download_button(
                    label='📥 Download Caption (TXT)',
                    data=caption_text,
                    file_name='car_caption.txt',
                    mime='text/plain',
                    use_container_width=True
                )
            
            with post_tab2:
                st.markdown('### Search & Social Hashtags')
                hashtags_text = post.get('hashtags', '')
                st.markdown(f'**{hashtags_text}**')
                st.text_area('Copy hashtags:', value=hashtags_text, height=150, disabled=True)
                st.copy_button(
                    label='📋 Copy Hashtags',
                    text=hashtags_text,
                    use_container_width=True
                )
            
            with post_tab3:
                st.markdown('### Features Summary')
                features_summary = post.get('features_summary', '')
                st.text(features_summary)
            
            with post_tab4:
                st.markdown('### Platform Posting Instructions')
                instructions = post.get('posting_instructions', '')
                st.text(instructions)
            
            with post_tab5:
                st.markdown('### Inquiry Handling Script')
                inquiry_script = post.get('inquiry_script', '')
                st.text(inquiry_script)
            
            with post_tab6:
                st.markdown('### Delivery Handover Script')
                delivery_script = post.get('delivery_script', '')
                st.text(delivery_script)
            
            st.divider()
            
            # DOWNLOAD OPTIONS
            st.markdown('### 📥 Download Complete Post Package')
            col1, col2, col3 = st.columns(3)
            
            with col1:
                json_data = json.dumps({
                    'car_info': car_info,
                    'category': post.get('category'),
                    'caption': post.get('caption'),
                    'hashtags': post.get('hashtags'),
                    'features': post.get('features_summary'),
                    'posting_instructions': post.get('posting_instructions'),
                    'inquiry_script': post.get('inquiry_script'),
                    'delivery_script': post.get('delivery_script')
                }, indent=2)
                st.download_button(
                    label='📄 Download as JSON',
                    data=json_data,
                    file_name='car_post_complete.json',
                    mime='application/json',
                    use_container_width=True
                )
            
            with col2:
                all_text = f"""
CAR POSTING BOT - COMPLETE POST
{'='*60}

SELLING ANGLE:
{post.get('selling_angle', '')}

CAR INFORMATION:
{json.dumps(car_info, indent=2)}

CATEGORY: {post.get('category', '')}

CAPTION:
{post.get('caption', '')}

HASHTAGS:
{post.get('hashtags', '')}

POSTING INSTRUCTIONS:
{post.get('posting_instructions', '')}

INQUIRY SCRIPT:
{post.get('inquiry_script', '')}

DELIVERY SCRIPT:
{post.get('delivery_script', '')}
"""
                st.download_button(
                    label='📝 Download as TXT',
                    data=all_text,
                    file_name='car_post_complete.txt',
                    mime='text/plain',
                    use_container_width=True
                )

# ============== TAB 2: CHAT ASSISTANT ==============
with tab2:
    st.subheader('💬 AI Chat Assistant')
    st.write('Ask questions about car selling, pricing, marketing strategies, and more!')
    
    if not chat_assist:
        st.error('💬 Chat Assistant module not loaded.')
    else:
        # Display chat history
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.chat_history:
                if message['role'] == 'user':
                    st.chat_message('user').write(message['content'])
                else:
                    st.chat_message('assistant').write(message['content'])
        
        # Input area
        input_col1, input_col2 = st.columns([4, 1])
        
        with input_col1:
            user_input = st.text_input('Ask a question...', key='chat_input', label_visibility='collapsed')
        
        with input_col2:
            send_btn = st.button('💬 Send', use_container_width=True, type='primary')
        
        if send_btn and user_input:
            st.session_state.chat_history.append({'role': 'user', 'content': user_input})
            
            with st.spinner('⏳ Thinking...'):
                try:
                    response = chat_assist.get_response(user_input)
                    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
                    st.rerun()
                except Exception as e:
                    st.error(f'❌ Error: {str(e)}')
        
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button('🗑️ Clear Chat History', use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()

# ============== TAB 3: IMAGE PROCESSING ==============
with tab3:
    st.subheader('🖼️ Image Processing & Enhancement')
    
    if not image_processor:
        st.error('🖼️ Image Processor module not loaded.')
    else:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write('**Upload and enhance car images**')
            uploaded_file = st.file_uploader('Choose a car image', type=['jpg', 'jpeg', 'png'])
            
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.markdown('**Original Image:**')
                st.image(image, use_column_width=True)
                st.info(f'📐 Dimensions: {image.width}x{image.height} pixels')
        
        with col2:
            if uploaded_file:
                st.write('**Enhancement Options:**')
                enhancement_type = st.selectbox(
                    'Select enhancement type',
                    ['Enhance Quality', 'Optimize for Facebook', 'Apply Background']
                )
                
                if enhancement_type == 'Enhance Quality':
                    brightness = st.slider('Brightness', -50, 50, 0)
                    contrast = st.slider('Contrast', -50, 50, 0)
                
                if st.button('🎨 Process Image', use_container_width=True, type='primary'):
                    with st.spinner('⏳ Processing image...'):
                        try:
                            image = Image.open(uploaded_file)
                            
                            if enhancement_type == 'Enhance Quality':
                                processed = image_processor.enhance_image_professional(
                                    image, brightness=brightness, contrast=contrast
                                )
                            elif enhancement_type == 'Optimize for Facebook':
                                processed = image_processor.optimize_for_facebook_professional(image)
                            else:
                                processed = image_processor.apply_background_to_image(image, background_color=(70, 70, 70))
                            
                            st.session_state.processed_image = processed
                            st.success('✅ Image processed!')
                        except Exception as e:
                            st.error(f'❌ Error: {str(e)}')
        
        if st.session_state.processed_image:
            st.divider()
            st.markdown('**Processed Image:**')
            st.image(st.session_state.processed_image, use_column_width=True)
            
            img_byte_arr = BytesIO()
            st.session_state.processed_image.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            st.download_button(
                label='📥 Download Processed Image',
                data=img_byte_arr,
                file_name='processed_car_image.png',
                mime='image/png',
                use_container_width=True
            )

# ============== TAB 4: ABOUT ==============
with tab4:
    st.markdown('''
    ## 🚗 Car Posting Bot
    
    **Your AI-powered solution for creating optimized car sales posts**
    
    ### ✨ Features
    - ⚡ AI-Powered Caption Generation
    - 🎯 Psychology-Optimized Messaging
    - #️⃣ Auto-Generated Hashtags
    - 💬 AI Chat Assistant
    - 🖼️ Image Processing & Enhancement
    - 📊 Posting Analytics
    - 💡 Smart Selling Angles
    - 📱 Multi-Platform Support
    
    ### 📋 What You Get
    - **Psychology-Optimized Captions** - Designed to convert buyers
    - **Smart Hashtags** - 30+ hashtags for maximum reach
    - **Posting Instructions** - Platform-specific guidelines
    - **Inquiry Scripts** - Handle buyer questions professionally
    - **Delivery Scripts** - Close the deal confidently
    - **Feature Extraction** - Auto-detect key car features
    - **Category Classification** - Smart car categorization
    
    ### 🚀 Quick Start
    1. Enter your car details in the Car Post Generator tab
    2. Click "Generate Car Post"
    3. Review the generated content
    4. Download and post on your platforms
    5. Use the scripts for buyer interactions
    
    ### 📞 Support
    - GitHub: [carbot Repository](https://github.com/adeelciit786-hue/carbot)
    - Documentation: Check the GitHub repo for guides
    - Local Server: Run `python app.py` for Flask version
    
    ### 🔧 Technology Stack
    - **Backend**: Python, Flask, AI/LLM Integration
    - **Frontend**: Streamlit (Web App)
    - **Image Processing**: Pillow, NumPy
    - **Data Processing**: JSON, CSV
    
    ---
    
    **Version**: 2.0 | **Last Updated**: December 2025
    ''')

# Footer
st.divider()
st.markdown(
    '<div style="text-align: center; color: #666; margin-top: 2rem;"><p>🚗 Car Posting Bot | '
    '<a href="https://github.com/adeelciit786-hue/carbot">GitHub</a> | '
    '<a href="http://localhost:5000">Flask Version</a></p></div>',
    unsafe_allow_html=True
)
