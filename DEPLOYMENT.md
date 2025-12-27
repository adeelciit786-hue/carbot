# 🚗 Car Posting Bot - Deployment Guide

## ✅ Project Status: DEPLOYED TO GITHUB

**GitHub Repository**: https://github.com/adeelciit786-hue/carbot

---

## 🚀 TWO WAYS TO RUN YOUR APP

### Option 1: Flask Server (RECOMMENDED) ✅
**Best performance and all features working**

```bash
# Navigate to project folder
cd c:\Users\adeel\Trading2

# Start the server
python app.py

# Open in browser
http://localhost:5000
```

**Features**:
- ✅ All 4 API endpoints working
- ✅ Full web UI with all features
- ✅ Car post generation
- ✅ Chat assistant
- ✅ Image processing
- ✅ Zero dependency issues

---

### Option 2: Streamlit Cloud
**Deploy to cloud**

**URL**: https://carbot-irnxcfhgdg7jw4ckuttnwn.streamlit.app/

**Status**: ⏳ Deploying... (May take 5-10 minutes on first deploy)

---

## 📋 API Endpoints (Localhost)

All endpoints available at `http://localhost:5000/api/`

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Main web UI |
| `/api/process-car` | POST | Generate AI car posts |
| `/api/chat` | POST | Chat with AI |
| `/api/chat-status` | GET | Server status |
| `/api/image-backgrounds` | GET | Image backgrounds |

---

## 🔧 Request Examples

### Generate Car Post
```bash
curl -X POST http://localhost:5000/api/process-car \
  -H "Content-Type: application/json" \
  -d '{
    "description": "2020 Toyota Camry, 45000 miles, excellent condition",
    "category": "Sedan",
    "price": 25000,
    "location": "Los Angeles, CA"
  }'
```

### Chat with AI
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "How should I price my car?"}'
```

### Check Status
```bash
curl http://localhost:5000/api/chat-status
```

---

## 📁 Project Structure

```
carbot/
├── app.py                 # Flask REST API
├── car_bot.py            # Car post generator
├── chat_assistant.py     # AI chat responses
├── image_processor.py    # Image enhancement
├── streamlit_app.py      # Streamlit web app
├── requirements.txt      # Dependencies
├── templates/
│   └── index.html        # Web UI
├── .streamlit/
│   └── config.toml       # Streamlit config
└── README.md             # Full docs
```

---

## 🎯 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/adeelciit786-hue/carbot.git
cd carbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Flask Server
```bash
python app.py
```

### 4. Open Browser
```
http://localhost:5000
```

---

## ✨ Features

**Car Post Generator**
- Psychology-optimized descriptions
- Conversion-focused messaging
- Multi-category support
- Pricing and location handling

**Chat Assistant**
- AI-powered responses
- Real-time interaction
- Smart fallback system

**Image Processing**
- Professional enhancement
- Background application
- Facebook optimization

---

## 🔗 Links

- **GitHub**: https://github.com/adeelciit786-hue/carbot
- **Localhost**: http://localhost:5000
- **Streamlit Cloud**: https://carbot-irnxcfhgdg7jw4ckuttnwn.streamlit.app/
- **Full README**: [README.md](README.md)

---

## 📞 Support

For issues:
1. Check GitHub repository
2. Review localhost logs
3. Check requirements compatibility

---

**Last Updated**: December 27, 2025  
**Status**: ✅ Ready for Production  
**Recommended Method**: Flask Localhost (Option 1)
