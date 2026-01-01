"""
Social Media Platform Optimizer
Generates platform-optimized captions for TikTok, YouTube, Instagram, and Snapchat
with SEO, trending keywords, and viral potential analysis
"""

import re
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum


class PlatformType(Enum):
    TIKTOK = "TikTok"
    YOUTUBE = "YouTube"
    INSTAGRAM = "Instagram"
    SNAPCHAT = "Snapchat"


@dataclass
class CaptionMetrics:
    platform: str
    caption: str
    estimated_reach: str
    virality_score: int  # 1-10
    trending_keywords: List[str]
    hashtags_count: int
    character_count: int
    engagement_potential: str


class TikTokCaptionGenerator:
    """Generate optimized captions for TikTok (max 2200 chars)"""
    
    TRENDING_TIKTOK_KEYWORDS = [
        "#FYP", "#ForYou", "#Viral", "#Trending", "#CarTok",
        "#CarReview", "#LuxuryCar", "#CarLife", "#AutomotiveContent",
        "#DealOfTheDay", "#CarDeals", "#LuxuryAuto", "#NewCar",
        "#CarCommunity", "#MotorHead", "#DriveWithMe", "#CarEnthusiast"
    ]
    
    VIRAL_HOOKS = [
        "POV: You just found the deal of your life 💰",
        "This car is INSANE 🤯",
        "Tell me you wouldn't drive this? 🏎️",
        "Reason you're scrolling: THIS CAR 👀",
        "First person to DM gets this deal 🔥",
        "If you see this, you're lucky 💎",
        "This price won't last 24 hours ⏰",
        "Your dream car just dropped 🚗✨",
    ]
    
    def generate(self, car_description: str, year: str, make_model: str, 
                 price: str, mileage: str) -> CaptionMetrics:
        """Generate TikTok optimized caption"""
        
        # Select attention-grabbing hook
        hook = self.VIRAL_HOOKS[hash(car_description) % len(self.VIRAL_HOOKS)]
        
        caption = f"""{hook}

{year} {make_model}
💰 Price: AED {price}
📍 Mileage: {mileage} km
⚡ Zero Issues

✨ Why This Car Slaps:
• Pristine Condition
• Perfect Maintenance History
• Ready to Drive TODAY
• DM for Test Drive

#TikTok #CarTok #LuxuryCar #DealOfTheDay
#AutomotiveContent #CarLife #Viral
#FYP #CarCommunity #MustHave"""
        
        trending_keywords = self._extract_trending_keywords(car_description)
        engagement_potential = self._analyze_virality(car_description)
        
        return CaptionMetrics(
            platform=PlatformType.TIKTOK.value,
            caption=caption,
            estimated_reach="500K - 2M",
            virality_score=self._calculate_virality_score(caption),
            trending_keywords=trending_keywords,
            hashtags_count=len(re.findall(r'#\w+', caption)),
            character_count=len(caption),
            engagement_potential=engagement_potential
        )
    
    def _extract_trending_keywords(self, text: str) -> List[str]:
        """Extract trending keywords from description"""
        keywords = []
        text_lower = text.lower()
        
        # Luxury indicators
        if any(word in text_lower for word in ['luxury', 'premium', 'leather', 'sunroof']):
            keywords.append("#LuxuryLife")
        
        # Speed/Performance indicators
        if any(word in text_lower for word in ['sport', 'turbo', 'fast', 'powerful']):
            keywords.append("#PerformanceCar")
        
        # Deal indicators
        if any(word in text_lower for word in ['deal', 'price', 'offer', 'sale']):
            keywords.append("#BestDeal")
        
        # Condition indicators
        if any(word in text_lower for word in ['new', 'pristine', 'perfect', 'excellent']):
            keywords.append("#MintCondition")
        
        return keywords
    
    def _calculate_virality_score(self, caption: str) -> int:
        """Calculate virality score 1-10"""
        score = 5
        
        # More emojis = more engagement
        emoji_count = len(re.findall(r'[😀-🙏🌀-🗿🚀-🛿]', caption))
        score += min(emoji_count // 3, 2)
        
        # Urgency indicators boost virality
        urgency_words = ['today', 'now', 'fast', 'limited', 'hurry', '24 hours']
        urgency_count = sum(1 for word in urgency_words if word in caption.lower())
        score += min(urgency_count, 2)
        
        # Call to action boost
        if any(cta in caption.lower() for cta in ['dm', 'comment', 'share', 'tag']):
            score += 1
        
        return min(score, 10)
    
    def _analyze_virality(self, text: str) -> str:
        """Analyze virality potential"""
        score = self._calculate_virality_score(text)
        
        if score >= 9:
            return "🔥 VIRAL POTENTIAL - HIGH"
        elif score >= 7:
            return "⚡ STRONG ENGAGEMENT"
        elif score >= 5:
            return "👍 GOOD REACH"
        else:
            return "📊 MODERATE"


class YouTubeCaptionGenerator:
    """Generate optimized captions for YouTube (detailed, SEO-focused)"""
    
    YOUTUBE_KEYWORDS = [
        "Car Review", "Car Tour", "Car For Sale", "Luxury Car",
        "Used Car", "Best Deal", "Car Buying", "Automotive",
        "Car Enthusiast", "Car Features", "Test Drive", "Car Inspection"
    ]
    
    def generate(self, car_description: str, year: str, make_model: str,
                 price: str, mileage: str, features: str = "") -> CaptionMetrics:
        """Generate YouTube optimized caption"""
        
        caption = f"""{year} {make_model} - Complete Review & Walkthrough

🎬 IN THIS VIDEO:
✅ Exterior Design & Condition
✅ Interior Features & Comfort
✅ Engine Performance Specs
✅ Transmission & Handling
✅ Safety Features Review
✅ Maintenance History
✅ Test Drive Experience
✅ Price & Deal Analysis

📊 CAR SPECIFICATIONS:
• Year: {year}
• Model: {make_model}
• Mileage: {mileage} km
• Current Price: AED {price}
• Condition: Excellent
• Availability: Immediate

💡 WHY YOU SHOULD WATCH:
This is one of the finest vehicles available in the market right now. 
In this comprehensive review, we cover everything you need to know before 
making your purchase decision.

🔗 TIMESTAMPS:
0:00 - Introduction
1:30 - Exterior Overview
5:00 - Interior Tour
8:30 - Dashboard & Tech
12:00 - Engine Check
15:00 - Test Drive
18:00 - Final Thoughts

📞 CONTACT DETAILS:
WhatsApp: +971-58-8168584
Email: sales@autobots.ae
📍 Location: Dubai, UAE

🔔 SUBSCRIBE for more car reviews and automotive content!
👍 LIKE if you'd buy this car
💬 COMMENT what you think about this vehicle"""
        
        seo_keywords = self._extract_seo_keywords(make_model, year)
        
        return CaptionMetrics(
            platform=PlatformType.YOUTUBE.value,
            caption=caption,
            estimated_reach="10K - 500K",
            virality_score=self._calculate_seo_score(caption),
            trending_keywords=seo_keywords,
            hashtags_count=2,
            character_count=len(caption),
            engagement_potential="🎬 SEO-OPTIMIZED - DISCOVERY FOCUSED"
        )
    
    def _extract_seo_keywords(self, make_model: str, year: str) -> List[str]:
        """Extract SEO-optimized keywords"""
        keywords = [
            f"{year} {make_model}",
            f"{make_model} review",
            "Car for sale",
            "Used car review",
            "Luxury car",
        ]
        return keywords
    
    def _calculate_seo_score(self, caption: str) -> int:
        """Calculate SEO score"""
        score = 5
        
        # Longer descriptions are better for SEO
        if len(caption) > 500:
            score += 2
        if len(caption) > 1000:
            score += 1
        
        # Timestamps improve ranking
        if '0:00' in caption or 'TIMESTAMPS' in caption:
            score += 2
        
        # Keywords in description
        keywords = ['review', 'features', 'price', 'specifications', 'condition']
        keyword_count = sum(1 for kw in keywords if kw.lower() in caption.lower())
        score += min(keyword_count, 2)
        
        return min(score, 10)


class InstagramCaptionGenerator:
    """Generate optimized captions for Instagram (visual storytelling + hashtags)"""
    
    INSTAGRAM_HASHTAGS = [
        "#LuxuryCars", "#CarOfTheDay", "#AutomobileLovers",
        "#CarCommunity", "#DreamCar", "#InstaAuto", "#Automotive",
        "#CarEnthusiast", "#DubaiCars", "#UAECars", "#CarLife",
        "#Luxurylifestyle", "#CarPhotography", "#AutoAficionado"
    ]
    
    def generate(self, car_description: str, year: str, make_model: str,
                 price: str, mileage: str) -> CaptionMetrics:
        """Generate Instagram optimized caption"""
        
        caption = f"""✨ {year} {make_model} ✨

The car you've been waiting for is finally here! 🚗💎

• Immaculate Condition
• {mileage} km Only
• Full Service History
• One Owner
• No Hidden Issues

💰 Competitive Price: AED {price}
⏰ Limited Availability

This stunning vehicle represents the pinnacle of automotive excellence. 
Every detail has been meticulously maintained, and the overall condition 
is nothing short of exceptional.

Perfect for:
✅ Luxury Car Enthusiasts
✅ Business Professionals
✅ Car Collectors
✅ Those Who Appreciate Quality

📸 Swipe to see all photos!
👉 Link in bio for more details

🔗 DM for inquiries
📞 WhatsApp: +971-58-8168584
📍 Dubai, UAE

---
#{self.INSTAGRAM_HASHTAGS[0]} #{self.INSTAGRAM_HASHTAGS[1]} #{self.INSTAGRAM_HASHTAGS[2]}
#{self.INSTAGRAM_HASHTAGS[3]} #{self.INSTAGRAM_HASHTAGS[4]} #{self.INSTAGRAM_HASHTAGS[5]}
#{self.INSTAGRAM_HASHTAGS[6]} #{self.INSTAGRAM_HASHTAGS[7]} #{self.INSTAGRAM_HASHTAGS[8]}
#{self.INSTAGRAM_HASHTAGS[9]} #{self.INSTAGRAM_HASHTAGS[11]} #{self.INSTAGRAM_HASHTAGS[12]}"""
        
        trending = self._get_trending_hashtags(car_description)
        
        return CaptionMetrics(
            platform=PlatformType.INSTAGRAM.value,
            caption=caption,
            estimated_reach="100K - 1M",
            virality_score=self._calculate_instagram_score(caption),
            trending_keywords=trending,
            hashtags_count=len(re.findall(r'#\w+', caption)),
            character_count=len(caption),
            engagement_potential="❤️ HIGH ENGAGEMENT - VISUAL FOCUSED"
        )
    
    def _get_trending_hashtags(self, text: str) -> List[str]:
        """Get trending hashtags based on content"""
        hashtags = []
        text_lower = text.lower()
        
        if 'mercedes' in text_lower or 'bmw' in text_lower or 'audi' in text_lower:
            hashtags.append("#LuxuryBrand")
        if 'pristine' in text_lower or 'perfect' in text_lower:
            hashtags.append("#ShowroomCondition")
        if 'low' in text_lower and 'mileage' in text_lower:
            hashtags.append("#LowMileage")
        
        return hashtags
    
    def _calculate_instagram_score(self, caption: str) -> int:
        """Calculate Instagram engagement score"""
        score = 5
        
        # Emojis are crucial for Instagram
        emoji_count = len(re.findall(r'[😀-🙏🌀-🗿🚀-🛿]', caption))
        score += min(emoji_count // 2, 3)
        
        # Hashtags (15-30 is optimal)
        hashtag_count = len(re.findall(r'#\w+', caption))
        if 15 <= hashtag_count <= 30:
            score += 2
        
        # Line breaks for readability
        if caption.count('\n') > 5:
            score += 1
        
        return min(score, 10)


class SnapchatCaptionGenerator:
    """Generate optimized captions for Snapchat (short, urgent, time-limited)"""
    
    def generate(self, car_description: str, year: str, make_model: str,
                 price: str, mileage: str) -> CaptionMetrics:
        """Generate Snapchat optimized caption"""
        
        caption = f"""🔥 ALERT! 🔥

{year} {make_model}
Just Posted!

💰 AED {price}
📍 {mileage} km
✨ Mint Condition

TAP FOR DETAILS ➡️
DM NOW 💬

⏰ THIS WON'T LAST
First Come, First Served!

Best Deal Today 🚗"""
        
        return CaptionMetrics(
            platform=PlatformType.SNAPCHAT.value,
            caption=caption,
            estimated_reach="50K - 500K",
            virality_score=8,  # Snapchat is inherently viral
            trending_keywords=["#Snapchat", "#UrgentDeal", "#LimitedTime"],
            hashtags_count=3,
            character_count=len(caption),
            engagement_potential="⚡ URGENT - TIME-SENSITIVE MESSAGING"
        )


class SocialMediaOptimizer:
    """Main optimizer class - coordinates all platform generators"""
    
    def __init__(self):
        self.tiktok = TikTokCaptionGenerator()
        self.youtube = YouTubeCaptionGenerator()
        self.instagram = InstagramCaptionGenerator()
        self.snapchat = SnapchatCaptionGenerator()
    
    def generate_all_platforms(self, car_description: str, year: str, 
                              make_model: str, price: str, mileage: str,
                              features: str = "") -> Dict[str, CaptionMetrics]:
        """Generate optimized captions for all platforms"""
        
        return {
            PlatformType.TIKTOK.value: self.tiktok.generate(
                car_description, year, make_model, price, mileage
            ),
            PlatformType.YOUTUBE.value: self.youtube.generate(
                car_description, year, make_model, price, mileage, features
            ),
            PlatformType.INSTAGRAM.value: self.instagram.generate(
                car_description, year, make_model, price, mileage
            ),
            PlatformType.SNAPCHAT.value: self.snapchat.generate(
                car_description, year, make_model, price, mileage
            ),
        }
    
    def get_best_performing_caption(self, all_captions: Dict[str, CaptionMetrics]) -> Dict:
        """Get the caption with highest virality/engagement score"""
        best = max(all_captions.items(), 
                  key=lambda x: x[1].virality_score)
        
        return {
            'platform': best[0],
            'caption': best[1].caption,
            'score': best[1].virality_score,
            'engagement': best[1].engagement_potential
        }
    
    def rank_platforms_by_performance(self, all_captions: Dict[str, CaptionMetrics]) -> List[Dict]:
        """Rank all platforms by expected performance"""
        ranked = sorted(
            all_captions.items(),
            key=lambda x: x[1].virality_score,
            reverse=True
        )
        
        return [
            {
                'rank': i + 1,
                'platform': platform,
                'score': metrics.virality_score,
                'estimated_reach': metrics.estimated_reach,
                'engagement': metrics.engagement_potential,
                'hashtags': metrics.hashtags_count
            }
            for i, (platform, metrics) in enumerate(ranked)
        ]
