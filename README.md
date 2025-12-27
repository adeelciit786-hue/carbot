# 🚗 Car Posting Bot - AI-Powered Sales Optimization

A comprehensive Python/Flask application that automatically generates psychology-driven car sales posts with conversion-optimized captions, strategic hashtags, and intelligent buyer engagement scripts.

## ✨ Features

### 🎯 Smart Caption Generation
- **8 Psychology-Optimized Templates**: Budget, Mid-Range, Premium, Hot Deal, Family, Fuel-Efficient, Low-Mileage, Popular
- **Emotional Triggers**: Built-in scarcity, urgency, and trust signals
- **Automatic Formatting**: Year and car model prominently featured for Facebook SEO
- **Copy-Paste Ready**: Professional captions ready to post immediately

### 🏷️ Advanced Hashtag Strategy
- **30 Conversion-Focused Hashtags**: Organized in 10 strategic tiers
- **Buyer Intent Targeting**: Core search terms, brand-specific, category, price, mileage, transmission, engine, year, location, urgency
- **Automatic Generation**: Hashtags customized per car based on specifications
- **Expected Impact**: 5x better discoverability vs random hashtags

### 📊 Intelligent Car Analysis
- **8-Factor Selling Angle Algorithm**: Analyzes price positioning, mileage condition, engine power, brand status, practical benefits, trust signals, urgency triggers
- **Automatic Categorization**: Detects car type and applies optimal selling strategy
- **Feature Extraction**: Identifies 20+ features and highlights key selling points

### 💬 Buyer Engagement System
- **Inquiry Response Scripts**: 5 pre-written conversation frameworks
- **Conversion-Optimized Responses**: Template and AI-powered (OpenAI/Gemini support)
- **Intent Detection**: Automatically identifies buyer questions (price, availability, features, objections)
- **Closing Strategies**: "Lock-in" tactics for viewings and negotiation handling

---

## 🚀 Quick Start

### 1. Run the Web Interface

```bash
python app.py
```

Then open http://localhost:5000

### 2. Or Run Interactive Mode

```bash
python run_bot.py
```

### 3. Or Test with Examples

```bash
python car_bot.py
```

This runs the example Jeep Compass and shows you the output format.

---

## Input Format - What to Include

When describing a car, include these details:

```
2018 Jeep Compass TrailHawk GCC with a 2.4L 4-cylinder in Good Condition 

It has been driven only 103,000 kilometers and is free from any issues or faults. 
The car drives smoothly without any problems or defects. 
It has been initially serviced at the agency and later at a local garage.

The car comes with a 2.4L 4-cylinder engine that provides around 700 kilometers per full tank. 
It also has brand-new tires installed.

This is a mid-option model with features such as leather seats, cruise control, alloy rims, 
DRL, fog lamps, parking sensors, Bluetooth, AUX, 4x4, push-button start, keyless entry, 
keyless start, electronic handbrake, and a touch screen display.

I am selling this car for just 30,000 AED.
```

### MUST INCLUDE:
- ✅ **Year & Make/Model** (e.g., "2018 Jeep Compass")
- ✅ **Mileage** (e.g., "103,000 kilometers")
- ✅ **Engine Type** (e.g., "2.4L 4-cylinder")
- ✅ **Condition** (Good/Excellent/Fair)
- ✅ **Price** (e.g., "30,000 AED")
- ✅ **Features** (List all key features)
- ✅ **Transmission** (Automatic/Manual - auto-detected if not specified)

### NICE TO INCLUDE:
- 📍 Location
- ⛽ Fuel range per tank
- 🔧 Service history
- 📸 Photo count
- 🚗 Special features (4x4, sunroof, etc.)

---

## Bot Output - What You Get

### 1. **Selling Angle**
The bot identifies the best way to market your car:
- "Exceptional value for money" 
- "Almost new with minimal wear"
- "Perfect 4x4 adventure vehicle"

### 2. **Category**
Auto-selected from 8 templates:
- Budget Car (Daily Driver) - Under 35,000 AED
- Mid-Range Car - Reliable & Popular
- Premium / Luxury - High-end vehicles
- Hot Deal / Quick-Sell - Urgent sales
- Family Car - Spacious vehicles
- Fuel-Efficient / City Car - Good MPG
- Low-Mileage Car - Less than 50k km
- Popular / Trending Car - High-demand models

### 3. **Copy-Paste Caption**
Ready-to-post caption for Facebook:
```
Hot Deal — Used Car in UAE

Make / Model: Jeep Compass TrailHawk
Year: 2018
Mileage: 103,000 km
Transmission: Automatic
Price: AED 30,000

✓ Great price for quick sale
✓ Low mileage & reliable
✓ Perfect for city driving
✓ Limited availability - Act fast!

Car available for viewing
Inspection before deal
No advance payment
DM me for details
URGENT - Limited availability
```

### 4. **Hashtags**
Auto-generated, targeted hashtags:
```
#UsedCarsUAE #DubaiCars #CarsDubai #JeepUAE #HotDeal #Dubai #UAE #UsedCarMarket
```

### 5. **Features List**
Formatted bullet-point list of all features

### 6. **Posting Instructions**
Exact step-by-step platform posting order:
1. Facebook Marketplace (with price & location)
2. Your Personal Profile (public)
3. Facebook Groups (3-5 specific groups)

### 7. **Inquiry Script**
Copy-paste response when buyers message:
```
Thanks for reaching out!

This car is available. You can view and inspect it before any payment.

I'm assisting buyers by connecting them with a verified dealer I work with.

May I know:
• Your budget
• Preferred location
• When you want to buy
```

### 8. **Delivery Script**
Post-delivery social proof template to build trust and attract more buyers

---

## Validation Rules (Auto-Check)

The bot BLOCKS posting if missing:
- ❌ Car make & model
- ❌ Year
- ❌ Mileage
- ❌ Engine/transmission
- ❌ Price
- ❌ Car condition

**Rule: Never post without full details** ✅

---

## How the Bot Categorizes Cars

The bot automatically selects the best category:

```
Is price < 35,000 AED? → HOT DEAL
Is mileage < 50,000 km? → LOW MILEAGE
Is it a popular model? → POPULAR
Is it BMW/Mercedes/Lexus? → PREMIUM
Is it Pathfinder/X-Trail/CR-V? → FAMILY
Fuel range > 500 km/tank? → FUEL EFFICIENT
Default → MID-RANGE
```

---

## Image Requirements (Before Posting)

Your 6-10 photos should follow this order:

1. **Front angle** - Clear view of front
2. **Interior** - Driver's seat perspective
3. **Odometer** - Close-up of mileage
4. **Side profile** - Full car view
5. **Rear angle** - Back of vehicle
6. **Engine bay** - Optional but impressive
7. **Features detail** - Leather seats, dashboard, etc.
8. **Overall condition** - Full car in good light
9. **Special features** - 4x4, sunroof, etc.
10. **Another angle** - Driver's side detail

**Quality Rules:**
- ✅ No watermarks
- ✅ No blurry photos
- ✅ Good lighting (daytime)
- ✅ Clear car condition
- ✅ Real photos (not stock images)

---

## Posting Timeline (Daily Routine)

**Morning (8-10 AM):**
- Run the bot with new car description
- Post to Facebook Marketplace
- Post to Personal Profile
- Post to 3-5 Facebook Groups

**Throughout the day:**
- Reply to messages IMMEDIATELY
- Use the inquiry script provided
- Qualify buyers carefully

**Every 3-4 days:**
- Repost high-interest cars
- Update availability status

**After delivery:**
- Request buyer testimonial photo
- Post delivery proof on profile
- This builds social proof = more inquiries

---

## Advanced Usage

### Batch Processing Multiple Cars

Create a text file `cars.txt` with multiple car descriptions, separated by:
```
---END CAR---
```

Then modify `run_bot.py` to read from file instead of input.

### Custom Hashtags

Edit the `generate_hashtags()` function in `car_bot.py` to add:
- Your personal branding hashtags
- Location-specific hashtags
- Campaign hashtags

### Template Customization

Edit the TEMPLATES dictionary in `car_bot.py` to:
- Add your phone number
- Change "DM me" to "Call me"
- Add WhatsApp link
- Customize feature bullets

---

## Example Output Variations

### Example 1: Budget Car (2012 Toyota Corolla)
```
🏷️ Category: BUDGET CAR
💰 Selling Angle: Perfect for city commute
```

### Example 2: Luxury Car (2020 BMW 5-Series)
```
🏷️ Category: PREMIUM
💰 Selling Angle: Sleek design & premium feel
```

### Example 3: Family Car (2019 Nissan Pathfinder)
```
🏷️ Category: FAMILY CAR
💰 Selling Angle: Spacious & safe for family trips
```

### Example 4: Fuel-Efficient (2017 Nissan Sunny)
```
🏷️ Category: FUEL EFFICIENT
💰 Selling Angle: Low fuel consumption for daily commute
```

---

## Troubleshooting

**Bot says "VALIDATION FAILED"?**
→ You're missing one of the required fields (make, year, mileage, engine, price, condition)
→ Add missing info to description and try again

**Hashtags not matching my car?**
→ Edit the `popular_models` list in `car_bot.py`
→ Add brand-specific logic to `generate_hashtags()`

**Want different caption style?**
→ Modify the TEMPLATES dictionary
→ Create new custom templates in `car_bot.py`

**Transmission not detected?**
→ Mention "Automatic" or "Manual" explicitly in description
→ Bot defaults to "Automatic" if not specified

---

## Pro Tips for Maximum Results

1. **First image is critical** - Front angle determines click-through
2. **Respond within 1 minute** - Speed wins in car buying
3. **Repost trending cars** - Every 3-4 days, same car gets 5x more views
4. **Ask qualification questions** - Filter serious buyers early
5. **Build social proof** - Delivery photos compound trust
6. **Never mention Caroofix** - You're the face of the deal
7. **Use exact prices** - Not ranges like "1 AED"
8. **Post at prime times** - 8-10 AM, 12-1 PM, 6-8 PM are peak

---

## Next Steps

1. Run `python run_bot.py`
2. Paste your car description
3. Copy the caption to Facebook Marketplace
4. Post photos in order specified
5. Copy hashtags exactly
6. Use the inquiry script when buyers message
7. Use delivery script after closing deals

**Your bot is ready. Start posting! 🚀**
