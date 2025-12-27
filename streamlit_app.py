import streamlit as st
import json
import os
from PIL import Image
from io import BytesIO
from pathlib import Path

# Page configuration (v2.1)
st.set_page_config(
    page_title='Car Posting Bot',
    page_icon='',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom styling
st.markdown('''
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTabs [data-baseweb=tab-list] button [data-testid=stMarkdownContainer] p {
        font-size: 1.25rem;
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
    st.warning(f'Car Bot not available: {str(e)[:50]}')

try:
    from chat_assistant import ChatAssistant
    chat_assist = ChatAssistant()
except Exception as e:
    st.warning(f'Chat Assistant not available: {str(e)[:50]}')

try:
    from image_processor import CarImageProcessor
    image_processor = CarImageProcessor()
except Exception as e:
    st.warning(f'Image Processor not available: {str(e)[:50]}')

# Initialize session state
if 'car_post' not in st.session_state:
    st.session_state.car_post = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None

# Header
st.markdown('#  Car Posting Bot Dashboard')
st.markdown('**Create optimized car sales posts with AI-powered descriptions and chat assistance**')
st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([' Car Post Generator', ' Chat Assistant', ' Image Processing', 'ℹ About'])

# ============== TAB 1: CAR POST GENERATOR ==============
with tab1:
    st.subheader('Generate AI-Optimized Car Posts')
    
    if not bot:
        st.error(' Car Bot module not loaded. Please check the logs.')
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            car_description = st.text_area(
                ' Car Description',
                placeholder='e.g., 2020 Toyota Camry, 45000 miles, white, excellent condition...',
                height=120,
                help='Provide details about the car you want to sell'
            )
            
            car_category = st.selectbox(
                ' Car Category',
                [cat.name for cat in CarCategory],
                help='Select the category that best matches your vehicle'
            )
            
            price = st.number_input(
                ' Price (Optional)',
                min_value=0,
                value=0,
                step=1000,
                help='Enter the asking price (optional)'
            )
            
            location = st.text_input(
                ' Location (Optional)',
                placeholder='e.g., Los Angeles, CA',
                help='Where the car is located'
            )
        
        with col2:
            st.info(' **Features:**  Psychology-optimized descriptions  Conversion-focused messaging  Urgency and scarcity triggers  Emotional appeal optimization  Category-specific templates')
        
        if st.button(' Generate Car Post', use_container_width=True, type='primary'):
            if not car_description.strip():
                st.error(' Please enter a car description')
            else:
                with st.spinner(' Generating optimized post...'):
                    try:
                        post_data = {
                            'description': car_description,
                            'category': car_category,
                            'price': price if price > 0 else None,
                            'location': location if location else None
                        }
                        
                        st.session_state.car_post = bot.generate_post(post_data)
                        st.success(' Post generated successfully!')
                    except Exception as e:
                        st.error(f' Error: {str(e)}')
        
        if st.session_state.car_post:
            st.divider()
            st.subheader(' Generated Car Post')
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                post = st.session_state.car_post
                title = post.get('title', 'Car for Sale')
                st.markdown(f'**{title}**')
                st.write(post.get('description', ''))
                
                if post.get('highlights'):
                    st.markdown('**Key Highlights:**')
                    for highlight in post['highlights']:
                        st.markdown(f' {highlight}')
                
                if post.get('call_to_action'):
                    st.success(f" {post['call_to_action']}")
            
            with col2:
                st.metric('Conversion Score', post.get('conversion_score', 'N/A'))
                st.metric('Category', post.get('category', 'N/A'))
            
            st.divider()
            col1, col2, col3 = st.columns(3)
            
            with col1:
                json_str = json.dumps(st.session_state.car_post, indent=2)
                st.download_button(
                    label=' Download as JSON',
                    data=json_str,
                    file_name='car_post.json',
                    mime='application/json',
                    use_container_width=True
                )

# ============== TAB 2: CHAT ASSISTANT ==============
with tab2:
    st.subheader(' AI Chat Assistant')
    st.write('Ask questions about car selling, pricing, marketing strategies, and more!')
    
    if not chat_assist:
        st.error(' Chat Assistant module not loaded.')
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
            user_input = st.text_input('Type your question here...', key='chat_input', label_visibility='collapsed')
        
        with input_col2:
            send_btn = st.button(' Send', use_container_width=True, type='primary')
        
        if send_btn and user_input:
            st.session_state.chat_history.append({'role': 'user', 'content': user_input})
            
            with st.spinner(' Thinking...'):
                try:
                    response = chat_assist.get_response(user_input)
                    st.session_state.chat_history.append({'role': 'assistant', 'content': response})
                    st.rerun()
                except Exception as e:
                    st.error(f' Error: {str(e)}')
        
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col2:
            if st.button(' Clear Chat History', use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()

# ============== TAB 3: IMAGE PROCESSING ==============
with tab3:
    st.subheader(' Image Processing & Enhancement')
    
    if not image_processor:
        st.error(' Image Processor module not loaded.')
    else:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write('**Upload and enhance car images**')
            uploaded_file = st.file_uploader('Choose a car image', type=['jpg', 'jpeg', 'png'])
            
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.markdown('**Original Image:**')
                st.image(image, use_column_width=True)
                st.info(f' Dimensions: {image.width}x{image.height} pixels')
        
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
                
                if st.button(' Process Image', use_container_width=True, type='primary'):
                    with st.spinner(' Processing image...'):
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
                            st.success(' Image processed!')
                        except Exception as e:
                            st.error(f' Error: {str(e)}')
        
        if st.session_state.processed_image:
            st.divider()
            st.markdown('**Processed Image:**')
            st.image(st.session_state.processed_image, use_column_width=True)
            
            img_byte_arr = BytesIO()
            st.session_state.processed_image.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            st.download_button(
                label=' Download Processed Image',
                data=img_byte_arr,
                file_name='processed_car_image.png',
                mime='image/png',
                use_container_width=True
            )

# ============== TAB 4: ABOUT ==============
with tab4:
    st.markdown('''
    ##  Car Posting Bot
    
    **Your AI-powered solution for creating optimized car sales posts**
    
    ###  Features
    -  AI-Powered Generation
    -  Chat Assistant
    -  Image Processing
    -  Analytics
    
    ###  Resources
    - [GitHub Repository](https://github.com/adeelciit786-hue/carbot)
    - [Documentation](https://github.com/adeelciit786-hue/carbot/blob/main/README.md)
    ''')

st.divider()
st.markdown('<div style=\"text-align: center; color: #666; margin-top: 2rem;\"><p> Car Posting Bot | <a href=\"https://github.com/adeelciit786-hue/carbot\">GitHub</a></p></div>', unsafe_allow_html=True)
