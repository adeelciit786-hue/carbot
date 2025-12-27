#!/usr/bin/env python3
"""
🚗 CAR POSTING BOT - INTERACTIVE VERSION
This is your main script to generate car postings
"""

from car_bot import CarPostingBot, print_result
import sys

def get_car_description():
    """Get car description from user input"""
    print("\n" + "="*70)
    print("🚗 ENTER CAR DESCRIPTION")
    print("="*70)
    print("\nPaste or type the complete car description.")
    print("Include: Make/Model, Year, Mileage, Engine, Price, Condition, Features")
    print("\nPress ENTER twice when done:\n")
    
    lines = []
    empty_count = 0
    
    while True:
        try:
            line = input()
            if line:
                lines.append(line)
                empty_count = 0
            else:
                empty_count += 1
                if empty_count >= 2:
                    break
        except EOFError:
            break
    
    return "\n".join(lines)

def main():
    """Main interactive loop"""
    bot = CarPostingBot()
    
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  🚗 CAR POSTING BOT - GENERATE PERFECT FACEBOOK POSTS  ".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    
    while True:
        description = get_car_description()
        
        if not description.strip():
            print("\n❌ No input received. Please try again.")
            continue
        
        print("\n⏳ Processing car information...")
        result = bot.generate_full_post(description)
        print_result(result)
        
        print("\n" + "="*70)
        option = input("Process another car? (yes/no): ").strip().lower()
        if option not in ['yes', 'y']:
            print("\n✅ Thank you for using Car Posting Bot!")
            print("📝 All your posts are ready to copy-paste to Facebook.\n")
            break

if __name__ == "__main__":
    main()
