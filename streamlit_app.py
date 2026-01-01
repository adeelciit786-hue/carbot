import streamlit as st
import json
from PIL import Image
from io import BytesIO

# ============ VERSION 4.1.1 - FIXED SYNTAX ERRORS ============
# Fixed: Removed broken character, optimized for mobile and all social platforms
# Status: Production Ready - Fast Load Times

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title='Digital Content Management Solution',
    page_icon='�',
    layout='wide',
    initial_sidebar_state='collapsed',
    menu_items={'about': "Digital Content Management Solution v5.0 - Multi-Platform Optimized"}
)

# Disable theme changing
st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1">', unsafe_allow_html=True)

# ==================== CUSTOM STYLING ====================
st.markdown('''
    <style>
    /* Root colors */
    :root {
        --primary: #6C63FF;
        --primary-dark: #5A52D5;
        --secondary: #FF6B9D;
        --accent: #FFA500;
        --success: #10B981;
        --danger: #F43F5E;
        --bg-light: #F8FAFC;
        --bg-card: #FFFFFF;
        --text-primary: #1E293B;
        --text-secondary: #64748B;
        --border-light: #E2E8F0;
    }
    
    /* Global styles */
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #F5F7FA 0%, #C3CFE2 100%);
    }
    
    * {
        transition: all 0.3s ease;
    }
    
    /* Remove default padding and margins */
    .main {
        padding: 0;
        background: linear-gradient(180deg, rgba(245,247,250,1) 0%, rgba(195,207,226,0.3) 100%);
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #6C63FF 0%, #D946EF 50%, #FF6B9D 100%);
        padding: 60px 30px;
        text-align: center;
        margin: -70px -50px 40px -50px;
        box-shadow: 0 20px 60px rgba(108, 99, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .header-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .header-container::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -50%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .header-container h1 {
        color: white;
        font-size: 3.2em;
        margin: 0;
        text-shadow: 0 8px 24px rgba(0,0,0,0.2);
        font-weight: 800;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
    }
    
    .header-container p {
        color: rgba(255,255,255,0.95);
        font-size: 1.3em;
        margin: 15px 0 0 0;
        font-weight: 500;
        position: relative;
        z-index: 1;
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0 10px 40px rgba(108, 99, 255, 0.08);
        margin-bottom: 30px;
        border: 1px solid rgba(108, 99, 255, 0.05);
        backdrop-filter: blur(10px);
    }
    
    .card:hover {
        box-shadow: 0 20px 60px rgba(108, 99, 255, 0.15);
        transform: translateY(-5px);
    }
    
    /* Section headings */
    .section-title {
        color: #6C63FF;
        font-size: 1.8em;
        margin-bottom: 25px;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .section-title::before {
        content: '';
        display: inline-block;
        width: 4px;
        height: 28px;
        background: linear-gradient(180deg, #6C63FF, #FF6B9D);
        border-radius: 2px;
    }
    
    /* Info grid */
    .info-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin: 30px 0;
    }
    
    .info-item {
        background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #E2E8F0;
        position: relative;
        overflow: hidden;
    }
    
    .info-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #6C63FF, #FF6B9D);
    }
    
    .info-item:hover {
        border-color: #6C63FF;
        box-shadow: 0 10px 30px rgba(108, 99, 255, 0.15);
        transform: translateY(-3px);
    }
    
    .info-label {
        color: #64748B;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 10px;
        display: block;
    }
    
    .info-value {
        color: #1E293B;
        font-size: 20px;
        font-weight: 700;
        word-break: break-word;
    }
    
    /* Selling angle box */
    .selling-angle {
        background: linear-gradient(135deg, #6C63FF 0%, #D946EF 50%, #FF6B9D 100%);
        color: white;
        padding: 30px;
        border-radius: 18px;
        font-size: 20px;
        font-weight: 700;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 20px 50px rgba(108, 99, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .selling-angle::before {
        content: '✨';
        position: absolute;
        font-size: 80px;
        opacity: 0.1;
        right: -20px;
        top: -20px;
    }
    
    /* Category badge */
    .category-badge {
        display: inline-block;
        background: linear-gradient(135deg, #6C63FF, #D946EF);
        color: white;
        padding: 12px 24px;
        border-radius: 25px;
        font-size: 15px;
        margin-bottom: 25px;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(108, 99, 255, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Content box */
    .content-box {
        background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #6C63FF;
        margin: 20px 0;
        font-family: 'Fira Code', 'Courier New', monospace;
        font-size: 14px;
        white-space: pre-wrap;
        word-wrap: break-word;
        line-height: 1.8;
        max-height: 500px;
        overflow-y: auto;
        color: #1E293B;
    }
    
    /* Success message */
    .success-msg {
        background: linear-gradient(135deg, #D1FAE5, #A7F3D0);
        color: #065F46;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #10B981;
        margin-bottom: 20px;
        font-weight: 600;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.15);
    }
    
    /* Error message */
    .error-msg {
        background: linear-gradient(135deg, #FFE4E6, #FFCDD2);
        color: #BE185D;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #F43F5E;
        margin-bottom: 20px;
        font-weight: 600;
        box-shadow: 0 8px 20px rgba(244, 63, 94, 0.15);
    }
    
    /* Tabs styling */
    .tab-buttons {
        display: flex;
        gap: 12px;
        margin-bottom: 25px;
        border-bottom: 3px solid #E2E8F0;
        flex-wrap: wrap;
        padding-bottom: 15px;
    }
    
    .tab-btn {
        padding: 12px 24px;
        background: #F1F5F9;
        border: none;
        border-radius: 10px;
        color: #64748B;
        cursor: pointer;
        font-weight: 700;
        transition: all 0.3s ease;
        font-size: 14px;
    }
    
    .tab-btn:hover {
        background: #E2E8F0;
        color: #6C63FF;
        transform: translateY(-2px);
    }
    
    .tab-btn.active {
        color: white;
        background: linear-gradient(135deg, #6C63FF, #D946EF);
        box-shadow: 0 8px 20px rgba(108, 99, 255, 0.3);
    }
    
    /* Chat section */
    .chat-container {
        background: white;
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0 10px 40px rgba(108, 99, 255, 0.08);
        margin-bottom: 30px;
        border: 1px solid rgba(108, 99, 255, 0.05);
    }
    
    .chat-container:hover {
        box-shadow: 0 20px 60px rgba(108, 99, 255, 0.15);
    }
    
    /* Features list */
    .features-list {
        background: linear-gradient(135deg, #F8FAFC 0%, #F1F5F9 100%);
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border: 2px solid #E2E8F0;
    }
    
    .feature-item {
        padding: 12px 0;
        color: #1E293B;
        border-bottom: 1px solid rgba(226, 232, 240, 0.6);
        font-weight: 500;
    }
    
    .feature-item:last-child {
        border-bottom: none;
    }
    
    .feature-item:before {
        content: "✓ ";
        color: #10B981;
        font-weight: bold;
        margin-right: 10px;
        font-size: 16px;
    }
    
    /* Message styling */
    .user-message {
        background: linear-gradient(135deg, #6C63FF, #D946EF);
        color: white;
        padding: 18px;
        border-radius: 15px;
        margin: 12px 0;
        text-align: right;
        box-shadow: 0 8px 20px rgba(108, 99, 255, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .assistant-message {
        background: linear-gradient(135deg, #F1F5F9, #E2E8F0);
        color: #1E293B;
        padding: 18px;
        border-radius: 15px;
        margin: 12px 0;
        text-align: left;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    /* Streamlit button overrides */
    .stButton > button {
        background: linear-gradient(135deg, #6C63FF, #D946EF) !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(108, 99, 255, 0.3) !important;
        transition: all 0.3s ease !important;
        font-size: 15px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 30px rgba(108, 99, 255, 0.4) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0) !important;
    }
    
    /* Text input styling */
    .stTextArea > div > div > textarea {
        border-radius: 12px !important;
        border: 2px solid #E2E8F0 !important;
        font-size: 15px !important;
        font-family: 'Segoe UI', sans-serif !important;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #6C63FF !important;
        box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.1) !important;
    }
    
    /* Divider styling */
    .divider {
        border: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #E2E8F0, transparent);
        margin: 40px 0;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .info-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .header-container h1 {
            font-size: 2.2em;
        }
        
        .header-container p {
            font-size: 1em;
        }
        
        .section-title {
            font-size: 1.4em;
        }
    }
    </style>
    ''', unsafe_allow_html=True)

# ==================== MODULE IMPORTS ====================
# Caching for performance optimization
@st.cache_resource
def load_bot_modules():
    """Load bot modules once and cache them"""
    bot = None
    chat_assist = None
    image_processor = None
    social_optimizer = None
    
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
    
    try:
        from social_media_optimizer import SocialMediaOptimizer
        social_optimizer = SocialMediaOptimizer()
    except Exception as e:
        st.error(f'📱 Social Media Optimizer Error: {str(e)[:50]}')
    
    return bot, chat_assist, image_processor, social_optimizer

# Load modules using cache
bot, chat_assist, image_processor, social_optimizer = load_bot_modules()

# ==================== SESSION STATE ====================
if 'car_post_result' not in st.session_state:
    st.session_state.car_post_result = None
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = 'caption'
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'platform_content' not in st.session_state:
    st.session_state.platform_content = None
if 'selected_platform' not in st.session_state:
    st.session_state.selected_platform = 'TikTok'

# ==================== HEADER ====================
# Make title clickable - home button
if st.button('� Digital Content Management Solution', key='home_btn', use_container_width=True):
    st.session_state.chat_history = []
    st.rerun()

st.markdown('''
    <div class="header-container">
        <h1>� Digital Content Management Solution</h1>
        <p>Automotive Brands with Consistent, High-Quality Social Content</p>
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
                        
                        # Generate platform-specific content if optimizer is available
                        if social_optimizer and result.get('success'):
                            car_info = result.get('car_info', {})
                            platform_content = social_optimizer.generate_all_platforms(
                                car_description,
                                year=str(car_info.get('year', 'N/A')),
                                make_model=car_info.get('make_model', 'Car'),
                                price=str(car_info.get('asking_price', 'Contact')),
                                mileage=str(car_info.get('mileage', 'N/A')),
                                features=result.get('features_summary', '')
                            )
                            st.session_state.platform_content = platform_content
                        
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
    if st.session_state.platform_content:
        tabs = ['📄 Caption', '🎯 Platform-Specific Content', '🏷️ Hashtags', '✨ Features', '📱 Posting Guide', '💬 Inquiry Script', '✅ Delivery Script']
    else:
        tabs = ['📄 Caption', '🏷️ Hashtags', '✨ Features', '📱 Posting Guide', '💬 Inquiry Script', '✅ Delivery Script']
    
    selected_tab = st.radio('Select content:', tabs, horizontal=True, label_visibility='collapsed')
    
    st.markdown('---')
    
    if selected_tab == '📄 Caption':
        st.markdown('<div style="font-weight: 600; font-size: 18px; color: #1E293B; margin-bottom: 15px;">Copy-Paste Caption for All Social Media Platforms</div>', unsafe_allow_html=True)
        caption_text = post.get('caption', '')
        st.markdown(f'<div class="content-box" style="font-family: \'Segoe UI\', sans-serif; font-size: 15px; line-height: 1.6; letter-spacing: 0.3px; color: #1E293B;">{caption_text}</div>', unsafe_allow_html=True)
    
    elif selected_tab == '🎯 Platform-Specific Content' and st.session_state.platform_content:
        st.markdown('<div style="font-weight: 600; font-size: 18px; color: #1E293B; margin-bottom: 15px;">Optimized Content for Each Platform</div>', unsafe_allow_html=True)
        
        # Platform selection
        platform_tabs = ['📱 TikTok', '🎬 YouTube', '📸 Instagram', '👻 Snapchat']
        selected_platform = st.tabs(platform_tabs)
        
        platforms_dict = {
            'TikTok': st.session_state.platform_content.get('TikTok'),
            'YouTube': st.session_state.platform_content.get('YouTube'),
            'Instagram': st.session_state.platform_content.get('Instagram'),
            'Snapchat': st.session_state.platform_content.get('Snapchat'),
        }
        
        with selected_platform[0]:  # TikTok
            metrics = platforms_dict['TikTok']
            st.markdown(f'<div class="category-badge">⚡ {metrics.engagement_potential}</div>', unsafe_allow_html=True)
            st.metric('Virality Score', f'{metrics.virality_score}/10', '🔥 High')
            st.metric('Estimated Reach', metrics.estimated_reach)
            st.markdown(f'<div class="content-box">{metrics.caption}</div>', unsafe_allow_html=True)
            st.write('**Trending Keywords:**', ', '.join(metrics.trending_keywords))
        
        with selected_platform[1]:  # YouTube
            metrics = platforms_dict['YouTube']
            st.markdown(f'<div class="category-badge">🎬 {metrics.engagement_potential}</div>', unsafe_allow_html=True)
            st.metric('SEO Score', f'{metrics.virality_score}/10', '📊 Optimized')
            st.metric('Estimated Reach', metrics.estimated_reach)
            st.markdown(f'<div class="content-box">{metrics.caption}</div>', unsafe_allow_html=True)
            st.write('**SEO Keywords:**', ', '.join(metrics.trending_keywords))
        
        with selected_platform[2]:  # Instagram
            metrics = platforms_dict['Instagram']
            st.markdown(f'<div class="category-badge">❤️ {metrics.engagement_potential}</div>', unsafe_allow_html=True)
            st.metric('Engagement Score', f'{metrics.virality_score}/10', '📈 Strong')
            st.metric('Hashtags Count', metrics.hashtags_count)
            st.markdown(f'<div class="content-box">{metrics.caption}</div>', unsafe_allow_html=True)
        
        with selected_platform[3]:  # Snapchat
            metrics = platforms_dict['Snapchat']
            st.markdown(f'<div class="category-badge">⚡ {metrics.engagement_potential}</div>', unsafe_allow_html=True)
            st.metric('Urgency Score', f'{metrics.virality_score}/10', '🔥 Critical')
            st.metric('Estimated Reach', metrics.estimated_reach)
            st.markdown(f'<div class="content-box">{metrics.caption}</div>', unsafe_allow_html=True)
        
        # Performance ranking
        st.divider()
        st.markdown('<div style="font-weight: 600; font-size: 16px; color: #1E293B; margin-bottom: 15px;">Platform Performance Ranking</div>', unsafe_allow_html=True)
        
        if social_optimizer:
            ranking = social_optimizer.rank_platforms_by_performance(st.session_state.platform_content)
            ranking_data = []
            for rank in ranking:
                ranking_data.append({
                    '🏆 Rank': rank['rank'],
                    'Platform': rank['platform'],
                    'Score': f"{rank['score']}/10",
                    'Reach': rank['estimated_reach'],
                    'Type': rank['engagement']
                })
            st.dataframe(ranking_data, use_container_width=True, hide_index=True)
    
    elif selected_tab == '🏷️ Hashtags':
        st.subheader('Ready-to-Use Hashtags')
        hashtags_text = post.get('hashtags', '')
        st.markdown(f'<div class="content-box">{hashtags_text}</div>', unsafe_allow_html=True)
    
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
                    response_data = chat_assist.generate_response(customer_message)
                    if response_data.get('success'):
                        st.session_state.chat_history.append({
                            'role': 'user',
                            'content': customer_message
                        })
                        st.session_state.chat_history.append({
                            'role': 'assistant',
                            'content': response_data.get('response', 'Unable to generate response')
                        })
                        st.rerun()
                    else:
                        st.error(f"❌ {response_data.get('error', 'Unknown error')}")
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
    """<div style="text-align: center; padding: 40px 20px; background: linear-gradient(135deg, rgba(108, 99, 255, 0.05), rgba(217, 70, 239, 0.05)); border-radius: 20px; margin-top: 50px;">
    <h3 style="color: #6C63FF; margin-bottom: 15px; font-size: 1.3em;">� Digital Content Management Solution</h3>
    <p style="color: #64748B; margin: 10px 0; font-size: 14px;">
        Multi-Platform Social Media Content Generation for Automotive Brands
    </p>
    <p style="font-size: 12px; color: #94A3B8; margin-top: 15px;">
        <strong>v5.0</strong> • TikTok • YouTube • Instagram • Snapchat • SEO-Optimized
    </p>
    <p style="font-size: 11px; color: #CBD5E1; margin-top: 10px;">
        Crafted with excellence • Transforming Automotive Sales Through AI-Powered Content
    </p>
    </div>""",
    unsafe_allow_html=True
)