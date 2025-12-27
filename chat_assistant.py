"""
AI-Powered Chat Assistant for Car Sales
Generates smart, humanized responses to customer inquiries
"""

import os
import json
from typing import Dict, Optional

# Try to import OpenAI first, fallback to Google Gemini
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class ChatAssistant:
    """AI Chat Assistant for customer interactions"""
    
    def __init__(self):
        self.api_type = self._detect_api()
        self.client = self._initialize_client()
        
        # System prompt - CONVERSION-OPTIMIZED FOR CAR SALES
        self.system_prompt = """You are Aadi, a professional car sales assistant for a UAE-based used car dealer.
Your mission: Build trust, qualify buyers, close viewings, and create urgency.

CORE PRINCIPLES:
✅ Keep responses SHORT (2-3 sentences MAX) - mobile-first
✅ Be HUMAN & CONVERSATIONAL - never sound like a bot
✅ Show GENUINE INTEREST - ask qualifying questions
✅ Build TRUST - mention inspection, documentation
✅ Create URGENCY - mention other inquiries, limited availability
✅ Be PROFESSIONAL but FRIENDLY - use names when you have them
✅ Never be PUSHY - let the car sell itself
✅ ALWAYS give clear CTAs - "Can you visit today?" "What time works?"

CONVERSATION RULES:
- Acknowledge their specific question first
- Answer directly (not wordy)
- Add ONE compelling reason to act
- End with ONE clear action step
- Use emojis sparingly (1-2 max)
- Never mention "Caroofix" or bot names
- Be as if Aadi is a real person
- If unsure about car details, ask buyer to visit

EXAMPLE RESPONSES:
❌ "Thank you for your inquiry. Our car is available for viewing..."
✅ "Thanks! What time works best for you to see it in person?"

❌ "The price is non-negotiable due to market conditions..."
✅ "Price is firm - it's already 15% below market. Want to check it out tomorrow?"

❌ "Multiple people are interested in this vehicle..."
✅ "Got 3 other inquiries today on this one - can you visit in the next 2 hours?"

Remember: You're matching buyers with their perfect cars. Act like it matters.
NEVER break character. ALWAYS be professional. ALWAYS create action."""

    def _detect_api(self) -> str:
        """Detect which API is available and configured"""
        openai_key = os.getenv('OPENAI_API_KEY')
        gemini_key = os.getenv('GEMINI_API_KEY')
        
        if openai_key and OPENAI_AVAILABLE:
            return 'openai'
        elif gemini_key and GEMINI_AVAILABLE:
            return 'gemini'
        else:
            return 'local'  # Fallback to template-based responses

    def _initialize_client(self):
        """Initialize the appropriate AI client"""
        if self.api_type == 'openai':
            return OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        elif self.api_type == 'gemini':
            genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
            return None  # Gemini doesn't need a client object
        return None

    def generate_response(self, customer_message: str, car_info: Optional[Dict] = None) -> Dict:
        """Generate AI response to customer message"""
        
        if not customer_message.strip():
            return {
                'success': False,
                'error': 'Please enter a customer message'
            }

        try:
            if self.api_type == 'openai':
                return self._generate_openai_response(customer_message, car_info)
            elif self.api_type == 'gemini':
                return self._generate_gemini_response(customer_message, car_info)
            else:
                return self._generate_template_response(customer_message, car_info)
        except Exception as e:
            return {
                'success': False,
                'error': f'Error generating response: {str(e)}'
            }

    def _generate_openai_response(self, customer_message: str, car_info: Optional[Dict] = None) -> Dict:
        """Generate response using OpenAI GPT"""
        
        # Build context from car info if provided
        context = ""
        if car_info:
            context = f"\nCar context: {car_info.get('make_model')} ({car_info.get('year')}) - AED {car_info.get('price')}"
        
        user_prompt = f"""Customer message: "{customer_message}"{context}

Generate a SHORT, friendly, and professional response (2-3 sentences max) to this customer inquiry.
Be conversational and human-like. Show genuine interest in helping them."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=150
            )
            
            generated_text = response.choices[0].message.content.strip()
            
            return {
                'success': True,
                'response': generated_text,
                'api_used': 'OpenAI GPT-3.5',
                'tokens_used': response.usage.total_tokens
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'OpenAI API error: {str(e)}'
            }

    def _generate_gemini_response(self, customer_message: str, car_info: Optional[Dict] = None) -> Dict:
        """Generate response using Google Gemini"""
        
        context = ""
        if car_info:
            context = f"\nCar context: {car_info.get('make_model')} ({car_info.get('year')}) - AED {car_info.get('price')}"
        
        user_prompt = f"""Customer message: "{customer_message}"{context}

Generate a SHORT, friendly, and professional response (2-3 sentences max) to this customer inquiry.
Be conversational and human-like. Show genuine interest in helping them."""

        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(
                f"{self.system_prompt}\n\n{user_prompt}"
            )
            
            generated_text = response.text.strip()
            
            return {
                'success': True,
                'response': generated_text,
                'api_used': 'Google Gemini',
                'tokens_used': 'N/A'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Gemini API error: {str(e)}'
            }

    def _generate_template_response(self, customer_message: str, car_info: Optional[Dict] = None) -> Dict:
        """
        Fallback: Generate CONVERSION-OPTIMIZED responses using smart templates
        No API needed - but still professional and persuasive
        """
        
        message_lower = customer_message.lower()
        
        # CONVERSION-OPTIMIZED RESPONSES by intent
        price_responses = [
            "That's the floor price honestly - it's already 15-20% below market! When can you visit to confirm it's worth it?",
            "Fixed price. It's a fair deal for the condition and mileage. Want to inspect it this week?",
            "The price reflects the quality. Trust me, at this level it'll get snapped up. Can you view it tomorrow?"
        ]
        
        viewing_responses = [
            "Perfect! I can arrange viewing same-day. What time works - morning or afternoon?",
            "Great! Let's lock it in. When's your preferred time and I'll confirm the location?",
            "Absolutely! I'm available most times. What day/time suits you best for a visit?"
        ]
        
        features_responses = [
            "It's loaded with the essentials and runs smooth. See it in person - that's when you'll really appreciate it. When can you come?",
            "Has everything you'd expect in this class. You can verify everything during inspection. When works for you?",
            "Well-equipped and maintained. Best to experience it yourself. Can you visit this week?"
        ]
        
        condition_responses = [
            "Condition is excellent - no major issues. Come inspect it yourself, that's what matters! When can you visit?",
            "It's been well-maintained with service records. You'll see the difference when you inspect it. When's good?",
            "Everything works perfectly. You can take it for a test drive before deciding. What time suits?"
        ]
        
        availability_responses = [
            "Available right now! When can you make it over?",
            "It's ready for viewing. What time works best for you?",
            "Still available but getting inquiries daily. Can you visit soon?"
        ]
        
        lowest_price_responses = [
            "Look, the price is final. It's already a steal. If you want it, act now before someone else does.",
            "I understand you want to negotiate, but at this price it's getting multiple inquiries. Either way, your choice!",
            "This IS the lowest price. Good deals don't last long in this market. When can you come see it?"
        ]
        
        interest_confirmed = [
            "Awesome! Let me know your details and I'll confirm the appointment right now.",
            "Great to hear! Send me your preferred time and I'll lock it in for you.",
            "Excellent! I'll make sure everything is ready. What time works for your visit?"
        ]
        
        objection_handling = [
            "Fair point! That's exactly why I recommend an inspection - see for yourself. No pressure, just come check it out.",
            "Totally understand your concern. The inspection will answer all your questions. Want to schedule it?",
            "Valid question - best way to be sure is to see it in person. When can you make that happen?"
        ]
        
        # INTENT DETECTION - Hierarchical (Most specific first)
        
        # PRICE NEGOTIATION
        if any(word in message_lower for word in ['lowest', 'best price', 'bottom price', 'final offer', 'negotiate', 'discount', 'reduce']):
            response = lowest_price_responses[0]
        
        # CONFIRMED INTEREST
        elif any(word in message_lower for word in ['yes', 'definitely', 'absolutely', 'count me in', 'let\'s do it', 'when can i']):
            response = interest_confirmed[0]
        
        # OBJECTIONS / CONCERNS
        elif any(word in message_lower for word in ['worried', 'concerned', 'doubt', 'hesitate', 'risk', 'uncertain']):
            response = objection_handling[0]
        
        # PRICE INQUIRIES
        elif any(word in message_lower for word in ['price', 'cost', 'how much', 'afford', 'expensive', 'cheaper', 'aed']):
            response = price_responses[0]
        
        # VIEWING REQUESTS
        elif any(word in message_lower for word in ['view', 'see', 'visit', 'inspection', 'check', 'look at', 'come over', 'arrange']):
            response = viewing_responses[0]
        
        # FEATURES/SPECS
        elif any(word in message_lower for word in ['feature', 'spec', 'equipped', 'amenities', 'does it have', 'included', 'options']):
            response = features_responses[0]
        
        # CONDITION/QUALITY
        elif any(word in message_lower for word in ['condition', 'quality', 'issue', 'problem', 'damage', 'repair', 'service']):
            response = condition_responses[0]
        
        # AVAILABILITY
        elif any(word in message_lower for word in ['available', 'ready', 'stock', 'still there']):
            response = availability_responses[0]
        
        else:
            # SMART DEFAULT - Create urgency while being helpful
            response = f"Thanks for reaching out! Interested in this one? Best to come view it - I can arrange that in the next 2 hours if you're serious. Just let me know! 🚗"
        
        return {
            'success': True,
            'response': response,
            'api_used': 'Template-Based (Optimized)',
            'tokens_used': 'N/A',
            'note': 'Using conversion-optimized templates. Set OPENAI_API_KEY or GEMINI_API_KEY for AI responses.'
        }

    def get_api_status(self) -> Dict:
        """Get current API configuration status"""
        return {
            'current_api': self.api_type,
            'openai_available': OPENAI_AVAILABLE,
            'gemini_available': GEMINI_AVAILABLE,
            'openai_configured': bool(os.getenv('OPENAI_API_KEY')),
            'gemini_configured': bool(os.getenv('GEMINI_API_KEY')),
            'message': f'Using {self.api_type.upper()} for response generation'
        }


# Initialize global assistant
assistant = ChatAssistant()


def get_chat_response(customer_message: str, car_info: Optional[Dict] = None) -> Dict:
    """Convenience function to get chat response"""
    return assistant.generate_response(customer_message, car_info)


def get_api_status() -> Dict:
    """Get API status"""
    return assistant.get_api_status()
