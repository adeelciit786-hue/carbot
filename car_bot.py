import re
from dataclasses import dataclass
from typing import Optional, Dict, List
from enum import Enum
from functools import lru_cache

class CarCategory(Enum):
    BUDGET = "Budget Car (Daily Driver)"
    MID_RANGE = "Mid-Range Car (Reliable / Popular)"
    PREMIUM = "Premium / Luxury"
    HOT_DEAL = "Hot Deal / Quick-Sell"
    FAMILY = "Family Car"
    FUEL_EFFICIENT = "Fuel-Efficient / City Car"
    LOW_MILEAGE = "Low-Mileage Car"
    POPULAR = "Popular / Trending Car"

@dataclass
class CarInfo:
    make_model: str
    year: int
    mileage: int
    engine: str
    transmission: str
    asking_price: int
    lowest_acceptable: Optional[int]
    location: str
    availability: str
    inspection_option: bool
    photo_count: int
    condition: str
    features: List[str]
    notes: str
    raw_input: str

class CarPostingBot:
    
    # Caption Templates - CONVERSION-OPTIMIZED WITH PSYCHOLOGY & URGENCY
    # Each template includes: Emotional benefit, Scarcity/Urgency, Social proof, CTA
    TEMPLATES = {
        CarCategory.BUDGET: """{year} {make_model} — Steal Deal Alert! Budget-Friendly in UAE 🔥

🎯 WHY YOU'LL LOVE IT:
✅ Price Won't Last Long — Well Below Market Value
✅ Fuel-Efficient — Save AED 200+ Monthly on Fuel
✅ Daily Commuter's Dream — Smooth, Reliable, Zero Issues
✅ Inspection Certified — No Hidden Problems

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

🔴 URGENCY: Limited Availability • Multiple Inquiries Already
✅ Same-Day Inspection Available
✅ No Advance Payment • Drive Home Today
✅ Full Documentation Ready

💬 Questions? DM Now or Call/WhatsApp: 058-8168584
⏱️ This won't be available tomorrow — Act now!""",

        CarCategory.MID_RANGE: """{year} {make_model} — Verified Quality at Smart Price 💎

🎯 WHY FAMILIES CHOOSE THIS:
✅ Family-Trusted Brand — Known for Reliability
✅ Excellent Condition — Well-Maintained by Single Owner
✅ Low Mileage = Less Repair Risk — Only {mileage} km
✅ Great Value Money — You Get What You Pay For

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

✨ CONFIDENCE BUILDERS:
✅ Professional Inspection Included
✅ Full Service History Available
✅ No Accidents — Clean Record
✅ Same-Day Test Drive Possible

🔴 ACTING FAST: 4 Inquiries This Week • 2 Viewings Scheduled
💬 Don't Wait — Call 058-8168584 Now
⏱️ Best options sell first — Don't miss out!""",

        CarCategory.PREMIUM: """{year} {make_model} — Luxury That Makes a Statement ✨👑

🎯 WHAT YOU'RE GETTING:
✅ Premium Craftsmanship — Every Detail Perfect
✅ Status & Comfort Combined — Feel the Difference
✅ Low Mileage Luxury — Barely Used, Fully Maintained
✅ Turn Heads Everywhere — This Is NOT a Boring Car

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

🏆 EXCLUSIVE DETAILS:
✅ Complete Service Records
✅ Extended Warranty Available
✅ Premium Interior — Pristine Condition
✅ One Owner — No Damage History

🔴 COLLECTOR'S TIP: Prices on These Rising • Won't Find Better
💬 Serious Inquiries Only — Call 058-8168584
⏱️ Premium cars like this don't wait long!""",

        CarCategory.HOT_DEAL: """{year} {make_model} — UNBEATABLE PRICE - Ending TODAY! 🚨🔥

⚡ THIS PRICE IS CRAZY GOOD:
✅ 15-20% Below Market — I'm SERIOUS About Selling Fast
✅ Reliable Workhorse — No Issues, Drives Smooth
✅ Low Mileage — {mileage} km Only
✅ Ready to Drive Home — Nothing Needs Fixing

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

🔥 WHY THE RUSH:
✅ Need Cash NOW • Priced to Sell FAST
✅ Inspection Today Possible
✅ Drive Away This Evening

⚠️ SERIOUS ALERT: This Price Won't Last 24 Hours
📞 FIRST COME, FIRST SERVED
💬 Call/WhatsApp NOW: 058-8168584
⏱️ Don't Think - Just Call! Multiple People Interested!""",

        CarCategory.FAMILY: """{year} {make_model} — Perfect Family Safe Haven 👨‍👩‍👧‍👦

🎯 YOUR FAMILY WILL LOVE:
✅ Spacious Interior — Comfortable for Road Trips
✅ Safety Certified — Kids Feel Secure
✅ Reliable Engine — 500+ km Range Per Tank
✅ Easy to Drive — Smooth, Responsive, Forgiving

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

👨‍👩‍👧 FAMILY-FRIENDLY FEATURES:
✅ Clean Interior — No Stains, No Odors
✅ Child Safety Locks Present
✅ Boot Space — For Family Luggage
✅ Excellent Condition — Peace of Mind

💡 PARENT'S CHOICE: Reliable = Less Stress
🔴 Families are Calling Now — Limited Time
💬 Book Your Test Drive: 058-8168584
⏱️ Best family cars go first!""",

        CarCategory.FUEL_EFFICIENT: """{year} {make_model} — Save BIG on Fuel Every Month 💰

🎯 YOUR WALLET WILL THANK YOU:
✅ Exceptional Mileage — 15-18 km/L (Save AED 300+ Monthly)
✅ City Traffic Pro — Loves Stop-Start Driving
✅ Low Maintenance Costs — No Expensive Repairs
✅ Smooth & Quiet Ride — Modern Efficiency

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

💰 MATH THAT MATTERS:
✅ AED 3,600 Fuel Savings Annually
✅ Low Tax Bracket — Cheap Registration
✅ Affordable Parts & Repairs
✅ Holds Value Well

🌱 ECO-CONSCIOUS CHOICE: Reduce Carbon Footprint
🔴 Smart Buyers Know — These Sell Fastest
💬 Join the Smart Buyers: 058-8168584
⏱️ Efficiency matters more every day!""",

        CarCategory.LOW_MILEAGE: """{year} {make_model} — Almost New • All New Car Benefits ✨

🎯 RARE FIND - ALMOST UNTOUCHED:
✅ {mileage} km Only — Practically Brand New
✅ Original Wear & Tear Minimal — Looks Fresh
✅ Engine Fresh — No Major Wear Yet
✅ All Systems Operating at Peak

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

🏆 INVESTMENT QUALITY:
✅ Future Resale Value Protected
✅ Warranty Still Potentially Active
✅ Interior Like Showroom Condition
✅ No Hidden Mechanical Issues

💎 COLLECTOR'S FIND: Low Mileage Cars Rise in Value
🔴 Rare to See This Mileage • Only One Available
💬 Reserve Now: 058-8168584
⏱️ The lower the mileage, the faster they sell!""",

        CarCategory.POPULAR: """{year} {make_model} — Most Trusted Car in UAE 🏆

🎯 POPULAR FOR A REASON:
✅ Thousands of Happy Owners — You'll Never Be Stuck for Support
✅ Spare Parts Everywhere — Always Available & Cheap
✅ Mechanics Know This Car — Quick & Affordable Repairs
✅ Reliable Workhorse — Proven Track Record

📊 QUICK SPECS:
Year: {year} | Mileage: {mileage} km | Trans: {transmission} | Price: AED {price}

⭐ WHY PEOPLE CHOOSE THIS:
✅ Resale Value Strong — Buyers Want These
✅ Insurance Rates Low — This Model is Cheap to Insure
✅ Community Support — Online Forums Are Active
✅ Proven Reliability — Minimal Issues Expected

🌟 TRUSTED CHOICE: Millions of Owners Worldwide
🔴 Hot Seller • Popular Models Move Fast
💬 Call Before It's Gone: 058-8168584
⏱️ Popular doesn't mean slow to sell!"""
    }

    def __init__(self):
        self.popular_models = ['Corolla', 'Civic', 'Accord', 'CR-V', 'Elantra', 'Sunny', 'Altima', 
                               'Pathfinder', 'Rogue', 'Qashqai', 'X-Trail', 'Compass', 'Wrangler',
                               '3 Series', '5 Series', 'C-Class', 'E-Class', 'A4', 'A6', 'Golf']

    def parse_car_description(self, description: str) -> Dict:
        """Parse car description to extract key information with comprehensive matching"""
        info = {
            'raw_input': description,
            'make_model': None,
            'year': None,
            'mileage': None,
            'engine': None,
            'transmission': None,
            'asking_price': None,
            'lowest_acceptable': None,
            'condition': None,
            'features': [],
            'fuel_range': None,
            'notes': []
        }

        first_line = description.split('\n')[0].strip()
        
        # ============================================================================
        # STEP 1: Extract YEAR (for "make" field in marketplace)
        # ============================================================================
        year_match = re.search(r'\b(\d{4})\b', first_line)
        if year_match:
            info['year'] = int(year_match.group(1))
        
        # ============================================================================
        # STEP 2: Extract CAR NAME (for "model" field - Brand + Model for SEO)
        # ============================================================================
        # List of car brands for better matching
        brands = ['Jeep', 'Mercedes', 'BMW', 'Audi', 'Honda', 'Toyota', 'Nissan', 
                  'Chevrolet', 'Hyundai', 'Kia', 'Lincoln', 'Cadillac', 'Ford', 
                  'Range', 'Lexus', 'Porsche', 'Volvo', 'Volkswagen', 'Mazda']
        
        # Strategy 1: "YEAR Brand Model" pattern - e.g., "2018 Jeep Compass"
        # Stop at: year patterns, GCC, with, full, American, trim levels, for, etc.
        pattern1 = r'\d{4}\s+(' + '|'.join(brands) + r')\s+([A-Za-z0-9]+(?:\s+[A-Za-z0-9]+)?)(?:\s+(?:GCC|with|Full|American|TrailHawk|Limited|LT|SE|Premium|Standard|for|in|—)|\d{4}|$)'
        match1 = re.search(pattern1, description, re.IGNORECASE)
        
        # Strategy 2: "Brand Model YEAR" pattern - e.g., "Jeep Wrangler 2016"
        # Stop at: YEAR, GCC, with, etc.
        pattern2 = r'(' + '|'.join(brands) + r')\s+([A-Za-z0-9]+(?:\s+[A-Za-z0-9]+)?)\s+\d{4}'
        match2 = re.search(pattern2, description, re.IGNORECASE)
        
        # Strategy 3: From first line - any "Brand Model" mention
        # Stop at: year, GCC, with, dash, etc.
        pattern3 = r'(' + '|'.join(brands) + r')\s+([A-Za-z0-9]+(?:\s+[A-Za-z0-9]+)?)(?:\s+\d{4}|GCC|with|—|-|for|in|$)'
        match3 = re.search(pattern3, first_line, re.IGNORECASE)
        
        # Try strategies in order
        car_name = None
        if match1:
            brand = match1.group(1).strip()
            model = match1.group(2).strip()
            # Clean up model (remove extra words)
            model = re.sub(r'\s+(with|Full|American|GCC|Specs|Specs).*', '', model, flags=re.IGNORECASE).strip()
            car_name = f"{brand} {model}"
        elif match2:
            brand = match2.group(1).strip()
            model = match2.group(2).strip()
            model = re.sub(r'\s+(GCC|with|Full|Limited|LT|SE|Premium|Specs).*', '', model, flags=re.IGNORECASE).strip()
            car_name = f"{brand} {model}"
        elif match3:
            brand = match3.group(1).strip()
            model = match3.group(2).strip()
            model = re.sub(r'\s+\d{4}.*', '', model, flags=re.IGNORECASE).strip()
            car_name = f"{brand} {model}"
        
        # Fallback: Extract just Brand + Model from first line
        if not car_name:
            for brand in brands:
                if brand.lower() in first_line.lower():
                    idx = first_line.lower().find(brand.lower())
                    after_brand = first_line[idx:].split()[1:3]  # Get next 2 words
                    if after_brand:
                        model = ' '.join(after_brand)
                        model = re.sub(r'\d{4}.*', '', model, flags=re.IGNORECASE).strip()
                        car_name = f"{brand} {model}"
                        break
        
        if car_name:
            # Clean up: remove non-essential suffixes
            car_name = re.sub(r'\s+(GCC|with|Full|American|TrailHawk|Limited|LT|SE|Premium|Standard|Specs|Condition).*', '', 
                             car_name, flags=re.IGNORECASE).strip()
            info['make_model'] = car_name
        
        # Final fallback: if still nothing, try very basic pattern
        if not info['make_model']:
            basic_match = re.search(r'([A-Z][a-zA-Z]+)\s+([A-Z][a-zA-Z0-9]+)', first_line)
            if basic_match:
                info['make_model'] = f"{basic_match.group(1)} {basic_match.group(2)}"

        # Extract Mileage
        mileage_match = re.search(r'(\d{2,3}),?(\d{3})\s*(?:kilometers|km)', description, re.IGNORECASE)
        if mileage_match:
            info['mileage'] = int(mileage_match.group(1) + mileage_match.group(2))

        # Extract Engine/Transmission - improved to detect V6, V8, etc.
        # Try V6/V8 patterns first
        v_engine_match = re.search(r'(V[68]|v[68])\s+(\d\.?\d+L)', description, re.IGNORECASE)
        if v_engine_match:
            engine_type = v_engine_match.group(1).upper()
            engine_size = v_engine_match.group(2)
            info['engine'] = f"{engine_size} {engine_type}"
        else:
            # Try cylinder patterns
            engine_match = re.search(r'(\d\.?\d+L)\s+(\d+-?cylinder)', description, re.IGNORECASE)
            if engine_match:
                info['engine'] = f"{engine_match.group(1)} {engine_match.group(2)}"
        
        # Detect transmission
        if 'automatic' in description.lower() or '6-speed automatic' in description.lower():
            info['transmission'] = 'Automatic'
        elif 'manual' in description.lower():
            info['transmission'] = 'Manual'
        else:
            # Default to automatic for modern cars
            info['transmission'] = 'Automatic'

        # Extract Price
        price_match = re.search(r'(\d{2,3}),?(\d{3})\s*(?:AED|aed)', description)
        if price_match:
            info['asking_price'] = int(price_match.group(1) + price_match.group(2))

        # Extract Condition
        if 'good condition' in description.lower():
            info['condition'] = 'Good Condition'
        elif 'excellent condition' in description.lower():
            info['condition'] = 'Excellent Condition'
        elif 'fair condition' in description.lower():
            info['condition'] = 'Fair Condition'

        # Extract Features
        features_keywords = ['leather seats', 'cruise control', 'alloy rims', 'drl', 'fog lamps', 
                            'parking sensors', 'bluetooth', 'aux', '4x4', 'push-button start',
                            'keyless entry', 'electronic handbrake', 'touch screen', 'sunroof',
                            'backup camera', 'gps', 'navigation']
        
        for feature in features_keywords:
            if feature.lower() in description.lower():
                info['features'].append(feature.title())

        # Extract fuel range
        fuel_match = re.search(r'(\d+)\s*kilometers?\s*per\s*(?:full\s+)?tank', description, re.IGNORECASE)
        if fuel_match:
            info['fuel_range'] = fuel_match.group(1)

        # Extract notes
        if 'brand-new tires' in description.lower():
            info['notes'].append('Brand-new tires installed')
        if 'serviced at agency' in description.lower() or 'serviced' in description.lower():
            info['notes'].append('Regular service history')

        return info

    def validate_car_info(self, info: Dict) -> tuple[bool, List[str]]:
        """Validate that CRITICAL information is present - allow optional fields to be missing"""
        errors = []

        # Only CRITICAL fields required
        if not info['make_model']:
            errors.append("❌ Car make & model is REQUIRED")
        if not info['year']:
            errors.append("❌ Year is REQUIRED")
        if info['asking_price'] is None:
            errors.append("❌ Asking price is REQUIRED")
        
        # Optional fields - don't block posting if missing
        # These will just be omitted from the output
        
        return len(errors) == 0, errors

    def categorize_car(self, info: Dict) -> CarCategory:
        """Determine the best category for the car"""
        price = info['asking_price'] or 0
        mileage = info['mileage'] or 999999
        year = info['year'] or 2000
        features = info['features'] or []
        make_model = info['make_model'] or ''

        # Check if it's a hot deal (good price)
        if price < 35000:
            return CarCategory.HOT_DEAL

        # Check if it's low mileage
        if mileage < 50000:
            return CarCategory.LOW_MILEAGE

        # Check if it's popular model
        if any(model.lower() in make_model.lower() for model in self.popular_models):
            return CarCategory.POPULAR

        # Check if it's luxury/premium
        if any(brand in make_model for brand in ['BMW', 'Mercedes', 'Audi', 'Lexus', 'Range']):
            return CarCategory.PREMIUM

        # Check if it's family car (spacious features)
        if 'Pathfinder' in make_model or 'X-Trail' in make_model or 'CR-V' in make_model:
            return CarCategory.FAMILY

        # Check if it's fuel efficient
        if info['fuel_range'] and int(info['fuel_range']) > 500:
            return CarCategory.FUEL_EFFICIENT

        # Default to mid-range
        return CarCategory.MID_RANGE

    def generate_caption(self, info: Dict, category: CarCategory) -> str:
        """Generate the posting caption using psychology-optimized templates"""
        template = self.TEMPLATES[category]
        
        # Prepare template variables
        format_vars = {
            'year': info.get('year') or 'YEAR',
            'make_model': info.get('make_model') or 'Car Model',
            'mileage': info.get('mileage') or 'Unknown',
            'transmission': info.get('transmission') or 'Auto',
            'price': info.get('asking_price') or 'Contact'
        }
        
        # Format the complete template with all variables
        try:
            caption = template.format(**format_vars)
        except KeyError as e:
            # Fallback if template has unexpected keys
            caption = template
        
        return caption

    def generate_hashtags(self, info: Dict, category: CarCategory) -> str:
        """
        Generate CONVERSION-FOCUSED hashtags using psychology & buyer intent
        Includes: Search terms, Social reach, Urgency, Trust, Location
        """
        hashtags = set()
        
        make_model = info['make_model'] or ''
        year = info['year'] or 0
        price = info['asking_price'] or 0
        mileage = info['mileage'] or 0
        engine = info['engine'] or ''
        transmission = str(info['transmission'] or '').lower()
        
        # TIER 1: CORE BUYER INTENT HASHTAGS (Highest ROI)
        hashtags.update([
            '#UsedCarsUAE',      # Exact intent
            '#DubaiCars',        # Location
            '#CarsDubai',        # Location variation
            '#BuyCarsUAE',       # Action word
            '#UsedCarMarket',    # Market awareness
            '#CarSalesUAE',      # Specific intent
        ])
        
        # TIER 2: BRAND & MODEL SPECIFICITY
        if make_model:
            parts = make_model.split()
            if parts:
                brand = parts[0]
                hashtags.add(f"#{brand}UAE")
                hashtags.add(f"#{brand}Cars")
                hashtags.add(f"#{brand}ForSale")
                # Add full model name
                model_tag = make_model.replace(' ', '')
                hashtags.add(f"#{model_tag}")
                hashtags.add(f"#Used{model_tag}")
                hashtags.add(f"#{model_tag}Dubai")  # Location + Model
        
        # TIER 3: CATEGORY-SPECIFIC (Buying Motivation)
        if category == CarCategory.BUDGET:
            hashtags.update([
                '#BudgetCars', '#AffordableCars', '#CheapCars',
                '#UnderAED25K', '#SmartBuyers', '#ValueForMoney'
            ])
        elif category == CarCategory.MID_RANGE:
            hashtags.update([
                '#MidRangeCars', '#ReliableCars', '#FamilyCarsDubai',
                '#VerifiedCars', '#SafeBuy', '#ConfidenceInBuying'
            ])
        elif category == CarCategory.PREMIUM:
            hashtags.update([
                '#LuxuryCars', '#PremiumCars', '#HighEndCars',
                '#StatusSymbol', '#PremiumQuality', '#LuxuryAutomarket'
            ])
        elif category == CarCategory.HOT_DEAL:
            hashtags.update([
                '#HotDeal', '#QuickSale', '#BestPrice',
                '#UrgentSale', '#LimitedOffer', '#DontMissOut',
                '#ActFast', '#PricedToSell'
            ])
        elif category == CarCategory.FAMILY:
            hashtags.update([
                '#FamilyCars', '#FamilyVehicles', '#SpaceAndComfort',
                '#SafeForFamily', '#TrustedFamily', '#PerfectForFamily'
            ])
        elif category == CarCategory.FUEL_EFFICIENT:
            hashtags.update([
                '#FuelEfficient', '#EcoFriendly', '#FuelSaver',
                '#LowConsumption', '#MoneySaver', '#SustainableDriving'
            ])
        elif category == CarCategory.LOW_MILEAGE:
            hashtags.update([
                '#LowMileage', '#AlmostNew', '#MinimalMileage',
                '#FactoryFresh', '#LikeNew', '#PristineCondition'
            ])
        elif category == CarCategory.POPULAR:
            hashtags.update([
                '#PopularCar', '#TrendingCars', '#MostWanted',
                '#TopSellingCar', '#CustomerFavorite', '#BestSeller'
            ])
        
        # TIER 4: PRICE POSITIONING
        if price < 15000:
            hashtags.add('#Under15k')
        elif price < 20000:
            hashtags.add('#Under20k')
        elif price < 35000:
            hashtags.add('#Under35k')
        elif price < 50000:
            hashtags.add('#Under50k')
        elif price > 100000:
            hashtags.add('#LuxuryPrice')
        
        # TIER 5: MILEAGE = CONDITION CONFIDENCE
        if mileage < 30000:
            hashtags.update(['#AlmostNew', '#VeryLowMileage'])
        elif mileage < 60000:
            hashtags.update(['#LowMileageVehicle', '#WellPreserved'])
        elif mileage < 100000:
            hashtags.add('#MediumMileage')
        elif mileage < 150000:
            hashtags.add('#HighlyReliable')
        
        # TIER 6: TRANSMISSION = CONVENIENCE FACTOR
        if 'automatic' in transmission:
            hashtags.add('#AutomaticCar')
            hashtags.add('#EasyDriving')
        elif 'manual' in transmission:
            hashtags.add('#ManualTransmission')
        
        # TIER 7: ENGINE POWER
        engine_upper = engine.upper() if engine else ''
        if 'V8' in engine_upper or '5.0' in engine or '4.7' in engine:
            hashtags.update(['#V8Engine', '#Powerful', '#PerformanceCar'])
        elif 'V6' in engine_upper or '3.5' in engine or '3.0' in engine:
            hashtags.update(['#V6Engine', '#GoodPower'])
        elif 'Hybrid' in engine or 'hybrid' in engine:
            hashtags.add('#HybridCar')
        
        # TIER 8: YEAR = TRUST SIGNAL
        if year >= 2020:
            hashtags.update(['#RecentModel', '#ModernCar', '#LatestTechnology'])
        elif year >= 2015:
            hashtags.update(['#RecentModel', '#Modern'])
        elif year >= 2010:
            hashtags.add('#WellMaintained')
        
        # TIER 9: LOCATION & MARKETPLACE
        hashtags.update(['#Dubai', '#UAE', '#FacebookMarketplace'])
        
        # TIER 10: URGENCY & ACTION (Psychology)
        hashtags.update(['#ActNow', '#OfferValid', '#InquireToday'])
        
        # Convert to list and return (30 hashtags for maximum reach)
        hashtag_list = sorted(list(hashtags))[:30]
        return ' '.join(hashtag_list)

    def generate_full_post(self, description: str) -> Dict:
        """Main function - generates complete posting information"""
        
        # Parse the description
        info = self.parse_car_description(description)
        
        # Validate
        is_valid, errors = self.validate_car_info(info)
        
        if not is_valid:
            return {
                'success': False,
                'errors': errors,
                'message': '⚠️  VALIDATION FAILED - Cannot post without complete information'
            }

        # Categorize
        category = self.categorize_car(info)
        
        # Generate caption
        caption = self.generate_caption(info, category)
        
        # Generate hashtags
        hashtags = self.generate_hashtags(info, category)

        # Posting instructions
        posting_instructions = self.get_posting_instructions(info, category)

        return {
            'success': True,
            'car_info': info,
            'category': category.value,
            'selling_angle': self.get_selling_angle(info, category),
            'caption': caption,
            'hashtags': hashtags,
            'posting_instructions': posting_instructions,
            'features_summary': self.format_features(info['features']),
            'inquiry_script': self.get_inquiry_script(),
            'delivery_script': self.get_delivery_script()
        }

    def get_selling_angle(self, info: Dict, category: CarCategory) -> str:
        """
        Generate psychologically-optimized selling angle based on car characteristics
        Uses: Value, Status, Safety, Savings, Reliability, Emotion
        """
        make_model = info['make_model'] or ''
        mileage = info['mileage'] if info['mileage'] else 999999
        price = info['asking_price'] or 0
        transmission = str(info['transmission'] or '').lower()
        engine = str(info['engine'] or '').lower()
        features = str(info['features'] or '').lower()

        angles = []
        
        # VALUE & FINANCIAL (Most Powerful)
        if price and price < 25000:
            angles.append('🔥 Unbeatable Deal — Well Below Market Price')
        elif price and price < 35000:
            angles.append('💰 Exceptional Value — Smart Money Choice')
        elif price and price < 50000:
            angles.append('✨ Premium Quality at Fair Price')
        
        # MILEAGE & CONDITION (Trust Factor)
        if mileage < 30000:
            angles.append('⚡ Almost New — Factory-Fresh Condition')
        elif mileage < 60000:
            angles.append('🎯 Minimal Wear — Barely Used Advantage')
        elif mileage < 100000:
            angles.append('✅ Well-Maintained — Peak Reliability')
        
        # PRACTICAL BENEFITS
        if engine and ('v8' in engine or '3.5' in engine or '2.7' in engine):
            angles.append('💪 Powerful Performance — Smooth Power Delivery')
        elif engine and ('hybrid' in engine or 'eco' in engine):
            angles.append('🌱 Eco-Friendly — Save Fuel & Environment')
        
        if 'automatic' in transmission:
            angles.append('🚗 Automatic Comfort — Effortless City Driving')
        
        # STATUS & EMOTION
        if 'premium' in make_model.lower() or 'benz' in make_model.lower() or 'bmw' in make_model.lower():
            angles.append('👑 Premium Status — Drive with Confidence')
        elif '4x4' in features or 'awd' in features.lower():
            angles.append('🏔️ Adventure Ready — Any Terrain, Any Time')
        elif 'leather' in features:
            angles.append('💎 Luxury Interior — Feel the Premium Comfort')
        
        # SAFETY & PEACE OF MIND
        angles.append('🛡️ Inspection Certified — Zero Hidden Issues')
        
        # SPEED & SCARCITY
        angles.append('⚠️ Urgent Sale — Priced to Move Fast')
        
        if not angles:
            angles.append('✅ Reliable Daily Driver — Trusted Quality')

        # Return the most impactful angle
        return angles[0] if angles else '✅ Quality Vehicle — Great Value Choice'

    def format_features(self, features: List[str]) -> str:
        """Format features nicely - show only if available"""
        if not features or len(features) == 0:
            return "• No specific features listed\n(Add feature details to description to display them here)"
        return '\n'.join([f"• {feature}" for feature in features])

    def get_posting_instructions(self, info: Dict, category: CarCategory) -> str:
        """Generate platform-specific posting instructions"""
        return """
📱 POSTING PLATFORM ORDER (MANDATORY):

1️⃣ FACEBOOK MARKETPLACE
   • Category: Vehicles → Cars
   • Location: Dubai
   • Price: Exact amount (AED {price})
   • Add all 6-10 photos
   • Images order: Front → Interior → Odometer

2️⃣ YOUR PERSONAL PROFILE
   • Post publicly
   • Add hashtags
   • Enable comments & DM

3️⃣ FACEBOOK GROUPS (Post in 3-5):
   • "Used Cars Dubai"
   • "UAE Buy & Sell Cars"
   • "Dubai Cars Marketplace"
   • "Emirates Car Sales"
   • Slight caption variation per group

📸 IMAGE REQUIREMENTS:
   ✓ Photo 1: Front angle
   ✓ Photo 2: Interior (drivers seat)
   ✓ Photo 3: Odometer
   ✓ Photo 4-10: Various angles, features, condition
   ✓ No watermarks, no blurry images
   ✓ Good lighting & clear condition

⏱️ TIMING:
   • Post in morning (8-10 AM)
   • Reply to messages immediately
   • Repost every 3-4 days
""".format(price=f"{info['asking_price']:,}" if info['asking_price'] else "Contact")

    def get_inquiry_script(self) -> str:
        """
        Get conversion-optimized inquiry handling script
        Focuses on: Qualification, Urgency, Action, Trust
        """
        return """
💬 BUYER INQUIRY RESPONSE FRAMEWORK:

═══════════════════════════════════════════════════════════════

FIRST MESSAGE - ACKNOWLEDGE & QUALIFY:

"Thanks for the interest! 🙌

Quick questions so I can help you best:
• Are you looking to buy THIS WEEK or planning ahead?
• Is this within your budget?
• When can you visit for inspection?

This car is getting inquiries quickly, so let's move fast if you're serious."

═══════════════════════════════════════════════════════════════

BUYER ASKS PRICE/DETAILS:

"The price is firm at AED [amount] - that's below market value honestly.

This car is:
✅ Inspection-certified (no hidden issues)
✅ Available for test drive today
✅ Ready to drive away once inspection passes

Want to see it? I can arrange viewing in the next 2 hours."

═══════════════════════════════════════════════════════════════

BUYER NEGOTIATES:

"I understand you want a better price, but here's the reality:

This price is 15% below what the dealer quoted me.
I priced it to move fast, not to negotiate.

If the price doesn't work, no problem - plenty of other interested buyers.
But if you want quality at this price, act NOW."

═══════════════════════════════════════════════════════════════

BUYER IS SERIOUS - CLOSE THE VIEWING:

"Great! Let's lock in a viewing.

📍 Location: [Your Location]
🕐 Time: [Morning/Afternoon] tomorrow
👤 Bring your ID

You can inspect thoroughly, take it for a test drive.
Inspection is completely free - zero pressure.

Shall we confirm tomorrow at [time]?"

═══════════════════════════════════════════════════════════════

AFTER VIEWING - FOLLOW UP:

"Hope you liked the car! 

What are your thoughts? Any concerns?

If all good, we can complete the paperwork and you drive away today.

Let me know if you need anything else."

═══════════════════════════════════════════════════════════════

IF BUYER SAYS "MAYBE" / "THINKING":

"Sure, take your time thinking. 

But here's what usually happens:
• I get 3-5 inquiries daily on good cars
• The serious buyers inspect and buy within 24 hours
• By tomorrow, this car might already be spoken for

If you're serious, don't wait.
If you need more time, completely fine too."

═══════════════════════════════════════════════════════════════
"""

    def get_delivery_script(self) -> str:
        """
        Get social proof & momentum-building script
        Focuses on: Community, Trust, FOMO, Repeated Purchases
        """
        return """
✅ AFTER-SALE SOCIAL PROOF STRATEGY:

═══════════════════════════════════════════════════════════════

STEP 1: ASK FOR DELIVERY PHOTO
Send buyer message:

"Hi! Hope you're enjoying the car! 🚗

Would you mind sharing a quick delivery photo? 
(You can blur the background/yourself if you want - just the car is fine)

I'm collecting photos from happy customers to show other buyers that we deliver on our promises.

It'll really help my business! 🙏"

═══════════════════════════════════════════════════════════════

STEP 2: POST ON YOUR PROFILE (WITH PHOTO)

"🎉 ANOTHER HAPPY CUSTOMER!

Just delivered this beauty to [Customer Initials].

They found exactly what they were looking for - reliable, great price, zero issues.

This car is now bringing smiles to a new family! 🚗😊

DM me if you want YOUR perfect car too.

We don't just sell cars - we deliver happiness."

Tag the customer if they're OK with it.

═══════════════════════════════════════════════════════════════

STEP 3: COLLECT TESTIMONIAL

Follow-up message after 2 weeks:

"Hi! How's the car treating you? 

Would you mind writing a quick line about your experience?
Something like: 'Got a great car at a fair price, process was smooth'

I want to share real customer feedback with other buyers."

═══════════════════════════════════════════════════════════════

STEP 4: POST TESTIMONIAL CAROUSEL

Create Facebook post with:
1. Delivery photo
2. Testimonial quote
3. Call-to-action

"Real customers. Real results. Real testimonials. 💯

[Quote from buyer about smooth process/quality/price]

If you want the same experience, DM me today.

Limited inventory - first come, first served! 🚗"

═══════════════════════════════════════════════════════════════

STEP 5: LEVERAGE FOR NEW LISTINGS

Create urgency post:

"⚠️ This car sold in 18 hours ⏱️

When we get quality cars at fair prices, they move FAST.

Got another car coming in tomorrow similar to this one.

Drop a 🚗 if you want me to notify you first!"

═══════════════════════════════════════════════════════════════

WHY THIS WORKS:
✅ Delivery photos = Social Proof = Trust
✅ Testimonials = Reduces buyer fear
✅ FOMO posts = Create urgency
✅ "Sold fast" posts = Attract more buyers
✅ Each sale = 5-10 new inquiries if done right

═══════════════════════════════════════════════════════════════
"""


def print_result(result: Dict):
    """Pretty print the result"""
    if not result['success']:
        print("\n" + "="*70)
        print("❌ POSTING BLOCKED - INCOMPLETE INFORMATION")
        print("="*70)
        for error in result['errors']:
            print(error)
        print("\n" + result['message'])
        return

    print("\n" + "="*70)
    print("✅ CAR POSTING READY TO SHARE")
    print("="*70)
    
    print(f"\n📍 SELLING ANGLE: {result['selling_angle']}")
    print(f"🏷️  CATEGORY: {result['category']}")
    
    print("\n" + "="*70)
    print("📝 COPY-PASTE CAPTION:")
    print("="*70)
    print(result['caption'])
    
    print("\n" + "="*70)
    print("🏷️  HASHTAGS:")
    print("="*70)
    print(result['hashtags'])
    
    print("\n" + "="*70)
    print("✨ CAR FEATURES:")
    print("="*70)
    print(result['features_summary'])
    
    print("\n" + "="*70)
    print("📱 PLATFORM POSTING GUIDE:")
    print("="*70)
    print(result['posting_instructions'])
    
    print("\n" + "="*70)
    print("💬 INQUIRY HANDLING SCRIPT:")
    print("="*70)
    print(result['inquiry_script'])
    
    print("\n" + "="*70)
    print("✅ DELIVERY & SOCIAL PROOF SCRIPT:")
    print("="*70)
    print(result['delivery_script'])


# Usage example
if __name__ == "__main__":
    bot = CarPostingBot()
    
    # Example car description
    example_description = """2018 Jeep Compass TrailHawk GCC with a 2.4L 4-cylinder in Good Condition 

It has been driven only 103,000 kilometers and is free from any issues or faults. The car drives smoothly without any problems or defects. It has been initially serviced at the agency and later at a local garage.

The car comes with a 2.4L 4-cylinder engine that provides around 700 kilometers per full tank. It also has brand-new tires installed.

This is a mid-option model with features such as leather seats, cruise control, alloy rims, DRL, fog lamps, parking sensors, Bluetooth, AUX, 4x4, push-button start, keyless entry, keyless start, electronic handbrake, and a touch screen display.

I am selling this car for just 30,000 AED."""
    
    result = bot.generate_full_post(example_description)
    print_result(result)
