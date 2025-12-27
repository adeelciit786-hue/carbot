import streamlit as st
import json
import os
from PIL import Image
from io import BytesIO
import requests
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="🚗 Car Posting Bot",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.25rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Load modules locally
from car_bot import CarPostingBot, CarCategory
from chat_assistant import ChatAssistant
from image_processor import CarImageProcessor

# Initialize session state
if 'car_post' not in st.session_state:
    st.session_state.car_post = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None

# Initialize modules
@st.cache_resource
def init_modules():
    bot = CarPostingBot()
    chat = ChatAssistant()
    image = CarImageProcessor()
    return bot, chat, image

bot, chat_assist, image_processor = init_modules()

# Header
st.markdown("# 🚗 Car Posting Bot Dashboard")
st.markdown("**Create optimized car sales posts with AI-powered descriptions and chat assistance**")
st.divider()

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📝 Car Post Generator", "💬 Chat Assistant", "🖼️ Image Processing", "ℹ️ About"])

# ============== TAB 1: CAR POST GENERATOR ==============
with tab1:
    st.subheader("Generate AI-Optimized Car Posts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Car details input
        car_description = st.text_area(
            "📋 Car Description",
            placeholder="e.g., 2020 Toyota Camry, 45000 miles, white, excellent condition...",
            height=120,
            help="Provide details about the car you want to sell"
        )
        
        car_category = st.selectbox(
            "🏷️ Car Category",
            [cat.name for cat in CarCategory],
            help="Select the category that best matches your vehicle"
        )
        
        price = st.number_input(
            "💰 Price (Optional)",
            min_value=0,
            value=0,
            step=1000,
            help="Enter the asking price (optional)"
        )
        
        location = st.text_input(
            "📍 Location (Optional)",
            placeholder="e.g., Los Angeles, CA",
            help="Where the car is located"
        )
    
    with col2:
        st.info(
            "✨ **Features:**\n"
            "• Psychology-optimized descriptions\n"
            "• Conversion-focused messaging\n"
            "• Urgency and scarcity triggers\n"
            "• Emotional appeal optimization\n"
            "• Category-specific templates"
        )
    
    # Generate button
    if st.button("🚀 Generate Car Post", use_container_width=True, type="primary"):
        if not car_description.strip():
            st.error("❌ Please enter a car description")
        else:
            with st.spinner("🔄 Generating optimized post..."):
                try:
                    post_data = {
                        "description": car_description,
                        "category": car_category,
                        "price": price if price > 0 else None,
                        "location": location if location else None
                    }
                    
                    st.session_state.car_post = bot.generate_post(post_data)
                    st.success("✅ Post generated successfully!")
                except Exception as e:
                    st.error(f"❌ Error generating post: {str(e)}")
    
    # Display generated post
    if st.session_state.car_post:
        st.divider()
        st.subheader("📌 Generated Car Post")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            post = st.session_state.car_post
            
            # Title
            st.markdown(f"**{post.get('title', 'Car for Sale')}**")
            
            # Main description
            st.write(post.get('description', ''))
            
            # Key highlights
            if post.get('highlights'):
                st.markdown("**Key Highlights:**")
                for highlight in post['highlights']:
                    st.markdown(f"• {highlight}")
            
            # Call to action
            if post.get('call_to_action'):
                st.success(f"💬 {post['call_to_action']}")
        
        with col2:
            # Statistics
            st.metric("Conversion Score", post.get('conversion_score', 'N/A'))
            st.metric("Category", post.get('category', 'N/A'))
            
            # Copy button
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.code(post.get('description', ''))
        
        # Export options
        st.divider()
        col1, col2, col3 = st.columns(3)
        
        with col1:
            json_str = json.dumps(st.session_state.car_post, indent=2)
            st.download_button(
                label="📥 Download as JSON",
                data=json_str,
                file_name="car_post.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col2:
            text_str = f"{post.get('title', 'Car for Sale')}\n\n{post.get('description', '')}"
            st.download_button(
                label="📄 Download as Text",
                data=text_str,
                file_name="car_post.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col3:
            if st.button("🔄 Generate New Post", use_container_width=True):
                st.session_state.car_post = None
                st.rerun()

# ============== TAB 2: CHAT ASSISTANT ==============
with tab2:
    st.subheader("💬 AI Chat Assistant")
    st.write("Ask questions about car selling, pricing, marketing strategies, and more!")
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])
    
    # Chat input
    user_input = st.chat_input("Type your question here...", key="chat_input")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Display user message
        st.chat_message("user").write(user_input)
        
        # Generate response
        with st.spinner("🤖 Thinking..."):
            try:
                response = chat_assist.get_response(user_input)
                
                # Add assistant message to history
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })
                
                # Display assistant message
                st.chat_message("assistant").write(response)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    # Clear chat button
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()

# ============== TAB 3: IMAGE PROCESSING ==============
with tab3:
    st.subheader("🖼️ Image Processing & Enhancement")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("**Upload and enhance car images for better presentation**")
        
        uploaded_file = st.file_uploader(
            "Choose a car image",
            type=["jpg", "jpeg", "png"],
            help="Upload a car photo for enhancement"
        )
        
        if uploaded_file:
            # Display original image
            st.markdown("**Original Image:**")
            image = Image.open(uploaded_file)
            st.image(image, use_column_width=True)
            
            # Image dimensions
            st.info(f"📐 Dimensions: {image.width}x{image.height} pixels")
    
    with col2:
        if uploaded_file:
            st.write("**Enhancement Options:**")
            
            enhancement_type = st.selectbox(
                "Select enhancement type",
                ["Enhance Quality", "Optimize for Facebook", "Apply Background"],
                help="Choose the type of enhancement"
            )
            
            if enhancement_type == "Enhance Quality":
                brightness = st.slider("Brightness", -50, 50, 0)
                contrast = st.slider("Contrast", -50, 50, 0)
            elif enhancement_type == "Apply Background":
                background = st.selectbox(
                    "Choose background",
                    ["Professional Gray", "Ocean Blue", "Urban Gray"]
                )
            
            # Process button
            if st.button("✨ Process Image", use_container_width=True, type="primary"):
                with st.spinner("⏳ Processing image..."):
                    try:
                        image = Image.open(uploaded_file)
                        
                        if enhancement_type == "Enhance Quality":
                            processed = image_processor.enhance_image_professional(
                                image,
                                brightness=brightness,
                                contrast=contrast
                            )
                        elif enhancement_type == "Optimize for Facebook":
                            processed = image_processor.optimize_for_facebook_professional(image)
                        else:
                            # Apply background
                            processed = image_processor.apply_background_to_image(
                                image,
                                background_color=(70, 70, 70)  # Gray background
                            )
                        
                        st.session_state.processed_image = processed
                        st.success("✅ Image processed successfully!")
                    except Exception as e:
                        st.error(f"❌ Error processing image: {str(e)}")
    
    # Display processed image
    if st.session_state.processed_image:
        st.divider()
        st.markdown("**Processed Image:**")
        st.image(st.session_state.processed_image, use_column_width=True)
        
        # Download button
        img_byte_arr = BytesIO()
        st.session_state.processed_image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        st.download_button(
            label="📥 Download Processed Image",
            data=img_byte_arr,
            file_name="processed_car_image.png",
            mime="image/png",
            use_container_width=True
        )

# ============== TAB 4: ABOUT ==============
with tab4:
    st.markdown("""
    ## 🚗 Car Posting Bot
    
    **Your AI-powered solution for creating optimized car sales posts**
    
    ### ✨ Features
    
    - **🤖 AI-Powered Generation**: Create conversion-optimized car posts using psychology-driven templates
    - **💬 Chat Assistant**: Get instant answers about car selling strategies and pricing
    - **🖼️ Image Processing**: Enhance car images with professional quality settings
    - **📊 Analytics**: Track conversion scores and engagement metrics
    
    ### 🎯 How It Works
    
    1. **Enter Car Details**: Provide information about the vehicle you're selling
    2. **Generate Post**: AI creates an optimized sales post with proven conversion triggers
    3. **Chat for Help**: Ask questions about strategies, pricing, or marketing
    4. **Process Images**: Enhance photos for better presentation
    5. **Export & Share**: Download posts and use them on any platform
    
    ### 🔧 Technology
    
    - **Backend**: Python Flask REST API
    - **Frontend**: Streamlit (this app)
    - **AI**: OpenAI & Google Gemini integration
    - **Image Processing**: Pillow (PIL) & NumPy
    - **Hosting**: Streamlit Cloud
    
    ### 📚 Documentation
    
    - [GitHub Repository](https://github.com/adeelciit786-hue/carbot)
    - [Quick Start Guide](https://github.com/adeelciit786-hue/carbot/blob/main/QUICK_START.md)
    - [Full Documentation](https://github.com/adeelciit786-hue/carbot/blob/main/README.md)
    
    ### 📞 Support
    
    For issues or feature requests, please visit our GitHub repository.
    
    ---
    
    **Made with ❤️ for car sellers worldwide**
    """)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    <p>🚗 Car Posting Bot | 
    <a href='https://github.com/adeelciit786-hue/carbot' target='_blank'>GitHub</a> | 
    <a href='https://github.com/adeelciit786-hue/carbot/blob/main/README.md' target='_blank'>Docs</a></p>
</div>
""", unsafe_allow_html=True)
