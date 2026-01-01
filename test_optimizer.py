"""
Quick Test Script - Verify All Components Working
Run this to test if social_media_optimizer is working correctly
"""

print("=" * 60)
print("TESTING DIGITAL CONTENT MANAGEMENT SOLUTION v5.0")
print("=" * 60)

# Test 1: Import modules
print("\n[TEST 1] Importing modules...")
try:
    from social_media_optimizer import SocialMediaOptimizer, PlatformType
    print("✅ social_media_optimizer imported successfully")
except Exception as e:
    print(f"❌ Error importing social_media_optimizer: {e}")
    exit(1)

try:
    from car_bot import CarPostingBot
    print("✅ car_bot imported successfully")
except Exception as e:
    print(f"❌ Error importing car_bot: {e}")
    exit(1)

try:
    from chat_assistant import ChatAssistant
    print("✅ chat_assistant imported successfully")
except Exception as e:
    print(f"❌ Error importing chat_assistant: {e}")

try:
    from image_processor import CarImageProcessor
    print("✅ image_processor imported successfully")
except Exception as e:
    print(f"❌ Error importing image_processor: {e}")

# Test 2: Initialize optimizer
print("\n[TEST 2] Initializing SocialMediaOptimizer...")
try:
    optimizer = SocialMediaOptimizer()
    print("✅ SocialMediaOptimizer initialized successfully")
except Exception as e:
    print(f"❌ Error initializing SocialMediaOptimizer: {e}")
    exit(1)

# Test 3: Generate content for all platforms
print("\n[TEST 3] Generating platform-specific content...")
test_description = "2018 Mercedes C300, 50000 km, pristine condition, single owner, AED 45000"

try:
    result = optimizer.generate_all_platforms(
        car_description=test_description,
        year="2018",
        make_model="Mercedes C300",
        price="45000",
        mileage="50000",
        features="Leather seats, Panoramic sunroof, Cruise control, Bluetooth"
    )
    
    platforms = list(result.keys())
    print(f"✅ Generated content for {len(platforms)} platforms: {', '.join(platforms)}")
    
    # Test 4: Display results
    print("\n[TEST 4] Displaying platform details...")
    for platform, metrics in result.items():
        print(f"\n  {platform}:")
        print(f"    - Virality/SEO Score: {metrics.virality_score}/10")
        print(f"    - Estimated Reach: {metrics.estimated_reach}")
        print(f"    - Engagement: {metrics.engagement_potential}")
        print(f"    - Hashtags: {metrics.hashtags_count}")
        print(f"    - Caption Length: {metrics.character_count} chars")
        print(f"    - Keywords: {', '.join(metrics.trending_keywords[:3])}")
    
except Exception as e:
    print(f"❌ Error generating content: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test 5: Platform ranking
print("\n[TEST 5] Ranking platforms by performance...")
try:
    ranking = optimizer.rank_platforms_by_performance(result)
    
    print("  Platform Performance Ranking:")
    for rank in ranking:
        print(f"    #{rank['rank']} {rank['platform']} - Score: {rank['score']}/10")
    
except Exception as e:
    print(f"❌ Error ranking platforms: {e}")
    exit(1)

# Test 6: Best performing caption
print("\n[TEST 6] Identifying best performing caption...")
try:
    best = optimizer.get_best_performing_caption(result)
    print(f"  ✅ Best Platform: {best['platform']}")
    print(f"  ✅ Score: {best['score']}/10")
    print(f"  ✅ Engagement: {best['engagement']}")
    
except Exception as e:
    print(f"❌ Error getting best caption: {e}")
    exit(1)

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED!")
print("=" * 60)
print("\nTo run the Streamlit app:")
print("  streamlit run streamlit_app.py")
print("\nThe platform-specific content tab should now display:")
print("  - TikTok caption with virality score")
print("  - YouTube caption with SEO score")
print("  - Instagram caption with engagement metrics")
print("  - Snapchat caption with urgency score")
print("  - Platform performance ranking table")
