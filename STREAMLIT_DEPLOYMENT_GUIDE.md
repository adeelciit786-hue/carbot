# Streamlit Deployment Guide

## Deploy to Streamlit Cloud

### Step 1: Add Streamlit Configuration File

Create `.streamlit/config.toml` in your repository:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[client]
showErrorDetails = true
toolbarMode = "viewer"
```

### Step 2: Push to GitHub

```bash
git add streamlit_app.py requirements.txt
git commit -m "Add Streamlit deployment"
git push origin main
```

### Step 3: Deploy to Streamlit Cloud

1. **Create Streamlit Account**: Go to https://streamlit.io/cloud
2. **Sign In with GitHub**: Use your GitHub credentials (adeelciit786-hue)
3. **New App**: Click "New app"
4. **Configure Deployment**:
   - Repository: `adeelciit786-hue/carbot`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
5. **Deploy**: Click "Deploy"

### Step 4: Configure Secrets (if using API keys)

In Streamlit Cloud Dashboard:
1. Go to App settings (⋮ menu)
2. Secrets: Add environment variables
3. Add API keys for OpenAI, Google Gemini (optional)

```
OPENAI_API_KEY = "your-key-here"
GOOGLE_API_KEY = "your-key-here"
```

## Access Your App

Once deployed:
- **URL**: `https://<your-username>-carbot-<random>.streamlit.app`
- **Direct Link**: https://adeelciit786-hue-carbot.streamlit.app

## Local Testing

Before deploying, test locally:

```bash
pip install streamlit
streamlit run streamlit_app.py
```

Then open: http://localhost:8501

## Features Available in Streamlit

✅ Car Post Generator
✅ Chat Assistant  
✅ Image Processing
✅ Download Options
✅ Full UI with tabs

## Troubleshooting

**App not loading?**
- Check internet connection
- Verify GitHub repository is public
- Check requirements.txt for Python version compatibility

**Images not processing?**
- Ensure Pillow and NumPy are in requirements.txt
- Check file permissions

**Chat not responding?**
- Add OpenAI/Google API keys to Streamlit secrets
- Check internet connectivity

**Port conflicts (local testing)?**
```bash
streamlit run streamlit_app.py --server.port 8502
```

## Auto-Rerun & Updates

Streamlit Cloud automatically:
- Pulls latest code from GitHub
- Rebuilds app when you push changes
- Maintains session state during reruns

## Performance Tips

1. Use `@st.cache_resource` for heavy modules ✅ (already implemented)
2. Minimize API calls
3. Optimize image sizes
4. Use `st.spinner()` for long operations ✅ (already implemented)

## Next Steps

1. Push code to GitHub: `git push origin main`
2. Visit Streamlit Cloud: https://streamlit.io/cloud
3. Deploy your app in < 2 minutes
4. Share link: https://adeelciit786-hue-carbot.streamlit.app

---

**Your app is now ready for Streamlit deployment!** 🚀
