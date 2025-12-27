#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚗 CAR POSTING BOT - SAMPLE DATA TESTING
Tests the bot against real car descriptions to ensure quality parsing
"""

import json
import sys
from car_bot import CarPostingBot, print_result

def load_sample_cars():
    """Load sample car data from JSON"""
    try:
        with open('sample_cars.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ sample_cars.json not found!")
        return None

def test_all_samples():
    """Test bot against all sample cars"""
    bot = CarPostingBot()
    data = load_sample_cars()
    
    if not data:
        return
    
    samples = data['sample_cars']
    results = []
    
    print("\n" + "="*80)
    print("TESTING BOT WITH SAMPLE CAR DESCRIPTIONS")
    print("="*80)
    print(f"\nTotal samples to test: {len(samples)}\n")
    
    for i, car in enumerate(samples, 1):
        print(f"\n{'='*80}")
        print(f"TEST {i}/{len(samples)}: {car['category']}")
        print(f"{'='*80}")
        
        result = bot.generate_full_post(car['description'])
        
        if result['success']:
            print(f"✅ SUCCESS")
            print(f"\n📝 Car Info Parsed:")
            print(f"  • Make/Model: {result['car_info']['make_model']}")
            print(f"  • Year: {result['car_info']['year']}")
            print(f"  • Mileage: {result['car_info']['mileage']:,} km" if result['car_info']['mileage'] else "  • Mileage: Not detected")
            print(f"  • Price: AED {result['car_info']['asking_price']:,}" if result['car_info']['asking_price'] else "  • Price: Not detected")
            print(f"  • Engine: {result['car_info']['engine']}" if result['car_info']['engine'] else "  • Engine: Not detected")
            print(f"  • Transmission: {result['car_info']['transmission']}" if result['car_info']['transmission'] else "  • Transmission: Not detected")
            print(f"  • Features Found: {len(result['car_info']['features'])}")
            
            print(f"\n💰 Categorized As: {result['category']}")
            print(f"💡 Selling Angle: {result['selling_angle']}")
            
            print(f"\n📄 Caption Preview (first 200 chars):")
            caption_preview = result['caption'][:200] + "..." if len(result['caption']) > 200 else result['caption']
            print(f"   {caption_preview}")
            
            print(f"\n🏷️  Hashtags: {result['hashtags'][:50]}...")
            
            results.append({
                'car': car['category'],
                'success': True,
                'price_extracted': result['car_info']['asking_price'] == car['expected_price'],
                'expected': car['expected_price'],
                'actual': result['car_info']['asking_price']
            })
        else:
            print(f"❌ FAILED")
            for error in result['errors']:
                print(f"   {error}")
            results.append({
                'car': car['category'],
                'success': False
            })
    
    # Summary
    print("\n\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    
    successful = sum(1 for r in results if r['success'])
    total = len(results)
    success_rate = (successful / total * 100) if total > 0 else 0
    
    print(f"\n✅ Successful: {successful}/{total} ({success_rate:.0f}%)")
    print(f"❌ Failed: {total - successful}/{total}")
    
    print("\nDetailed Results:")
    for i, result in enumerate(results, 1):
        status = "✅" if result['success'] else "❌"
        print(f"{status} {i}. {result['car']}", end="")
        if result['success'] and 'price_extracted' in result:
            price_status = "✅" if result['price_extracted'] else "⚠️"
            print(f" | Price: {price_status} AED {result['actual']:,} (expected {result['expected']:,})")
        else:
            print()
    
    print("\n" + "="*80)
    if success_rate == 100:
        print("ALL TESTS PASSED!")
    elif success_rate >= 80:
        print(f"GOOD RESULTS ({success_rate:.0f}% success rate)")
    else:
        print(f"NEEDS IMPROVEMENT ({success_rate:.0f}% success rate)")
    print("="*80 + "\n")

def test_single_car(car_number):
    """Test a specific car by number"""
    bot = CarPostingBot()
    data = load_sample_cars()
    
    if not data:
        return
    
    samples = data['sample_cars']
    if car_number < 1 or car_number > len(samples):
        print(f"❌ Invalid car number. Choose 1-{len(samples)}")
        return
    
    car = samples[car_number - 1]
    
    print(f"\n{'='*80}")
    print(f"🧪 TESTING: {car['category']}")
    print(f"{'='*80}\n")
    
    result = bot.generate_full_post(car['description'])
    print_result(result)

if __name__ == "__main__":
    import sys
    
    print("\n" + "="*80)
    print("CAR POSTING BOT - SAMPLE DATA TESTING SUITE")
    print("="*80 + "\n")
    
    if len(sys.argv) > 1:
        try:
            car_num = int(sys.argv[1])
            test_single_car(car_num)
        except ValueError:
            print("Usage: python test_samples.py [car_number]")
            print("   or: python test_samples.py (to test all)")
    else:
        test_all_samples()
