# 🚗 CAR POSTING BOT - START WITH OPENAI
# 
# This script sets up OpenAI API and starts the server
# 
# BEFORE RUNNING:
# 1. Get your OpenAI API key from: https://platform.openai.com/api-keys
# 2. Replace "sk-your-api-key-here" with your actual key below

$apiKey = "sk-your-api-key-here"  # ← REPLACE WITH YOUR ACTUAL KEY

# Check if API key is set
if ($apiKey -eq "sk-your-api-key-here") {
    Write-Host ""
    Write-Host "⚠️  IMPORTANT: API Key Not Configured!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Get your key from: https://platform.openai.com/api-keys" -ForegroundColor Cyan
    Write-Host "2. Replace 'sk-your-api-key-here' in this file with your actual key"
    Write-Host ""
    Write-Host "The bot will work with template-based responses until you set the API key."
    Write-Host ""
    exit
}

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  🚗 CAR POSTING BOT - WITH OPENAI INTEGRATION              ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Set environment variable
$env:OPENAI_API_KEY = $apiKey
Write-Host "✅ OpenAI API configured" -ForegroundColor Green

# Check if openai package is installed
try {
    python -c "import openai" 2>$null
    Write-Host "✅ OpenAI package found" -ForegroundColor Green
} catch {
    Write-Host "📦 Installing OpenAI package..." -ForegroundColor Yellow
    pip install openai
}

Write-Host ""
Write-Host "🚀 Starting server..." -ForegroundColor Green
Write-Host "📍 Open: http://localhost:5000" -ForegroundColor Cyan
Write-Host "💬 AI chat is now powered by GPT-3.5-Turbo" -ForegroundColor Green
Write-Host ""

cd "c:\Users\adeel\Trading2"
python app.py
