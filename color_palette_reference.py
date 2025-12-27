#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Background Color Palette Reference
Shows exact RGB values used for each background preset
"""

BACKGROUND_PALETTES = {
    'Luxury Residential': {
        'villa_green': {
            'description': 'Luxury Villa with Garden',
            'color1': (20, 100, 20),
            'color2': (100, 180, 80),
            'type': 'gradient',
            'mood': 'Lush, sophisticated garden atmosphere'
        },
        'villa_modern': {
            'description': 'Modern Villa Architecture',
            'color1': (40, 40, 60),
            'color2': (120, 150, 180),
            'type': 'gradient',
            'mood': 'Contemporary, cool modern aesthetic'
        },
        'villa_pool': {
            'description': 'Villa with Swimming Pool',
            'color1': (0, 120, 180),
            'color2': (100, 200, 220),
            'type': 'gradient',
            'mood': 'Refreshing, luxury pool vibes'
        }
    },
    
    'Waterfront & Beach': {
        'marina_blue': {
            'description': 'Dubai Marina Waterfront',
            'color1': (0, 80, 150),
            'color2': (80, 140, 220),
            'type': 'gradient',
            'mood': 'Professional, elegant waterfront'
        },
        'marina_gold': {
            'description': 'Marina at Sunset',
            'color1': (150, 100, 0),
            'color2': (255, 200, 50),
            'type': 'gradient',
            'mood': 'Warm, golden sunset ambiance'
        },
        'beach_golden': {
            'description': 'Golden Beach Paradise',
            'color1': (200, 150, 0),
            'color2': (255, 240, 100),
            'type': 'gradient',
            'mood': 'Bright, tropical beach atmosphere'
        },
        'beach_sunset': {
            'description': 'Beach Golden Hour',
            'color1': (180, 50, 20),
            'color2': (255, 150, 80),
            'type': 'gradient',
            'mood': 'Warm, romantic sunset colors'
        }
    },
    
    'Urban & Downtown': {
        'cityscape': {
            'description': 'Dubai Cityscape',
            'color1': (60, 60, 80),
            'color2': (150, 150, 180),
            'type': 'gradient',
            'mood': 'Professional, urban sophistication'
        },
        'downtown_night': {
            'description': 'Downtown Dubai Night',
            'color1': (20, 20, 40),
            'color2': (80, 90, 120),
            'type': 'gradient',
            'mood': 'Dark, mysterious night vibe'
        },
        'emirates_towers': {
            'description': 'Emirates District',
            'color1': (70, 100, 140),
            'color2': (180, 200, 220),
            'type': 'gradient',
            'mood': 'Cool professional, upscale district'
        }
    },
    
    'Nature & Desert': {
        'desert_sunset': {
            'description': 'Desert Sunset Dunes',
            'color1': (180, 60, 20),
            'color2': (255, 140, 50),
            'type': 'gradient',
            'mood': 'Warm, dramatic desert sunset'
        },
        'desert_golden': {
            'description': 'Desert Golden Hour',
            'color1': (150, 100, 0),
            'color2': (255, 200, 80),
            'type': 'gradient',
            'mood': 'Golden, warm desert landscape'
        },
        'dunes_drive': {
            'description': 'Desert Driving Scene',
            'color1': (180, 130, 60),
            'color2': (240, 200, 120),
            'type': 'gradient',
            'mood': 'Adventure, sandy desert tones'
        }
    },
    
    'Modern Amenities': {
        'parking_modern': {
            'description': 'Modern Parking Complex',
            'color1': (150, 150, 160),
            'color2': (200, 200, 210),
            'type': 'gradient',
            'mood': 'Clean, modern minimalist'
        },
        'parking_luxury': {
            'description': 'Luxury Parking Garage',
            'color1': (180, 180, 190),
            'color2': (220, 220, 230),
            'type': 'gradient',
            'mood': 'Elegant, professional gray'
        },
        'showroom_modern': {
            'description': 'Modern Showroom',
            'color1': (120, 120, 140),
            'color2': (180, 180, 200),
            'type': 'gradient',
            'mood': 'Professional, showroom aesthetic'
        }
    },
    
    'Professional & Clean': {
        'simple_white': {
            'description': 'Premium White Elegant',
            'color': (255, 255, 255),
            'type': 'solid',
            'mood': 'Pure, clean, classic elegance'
        },
        'simple_gray': {
            'description': 'Professional Gray',
            'color': (200, 200, 200),
            'type': 'solid',
            'mood': 'Neutral, professional, timeless'
        },
        'simple_black': {
            'description': 'Luxury Black Minimal',
            'color': (30, 30, 40),
            'type': 'solid',
            'mood': 'Sophisticated, luxury, dramatic'
        },
        'gradient_blue': {
            'description': 'Professional Blue Gradient',
            'color1': (30, 60, 120),
            'color2': (100, 150, 220),
            'type': 'gradient',
            'mood': 'Professional, corporate, trustworthy'
        },
        'gradient_gold': {
            'description': 'Luxury Gold Gradient',
            'color1': (180, 120, 0),
            'color2': (255, 220, 100),
            'type': 'gradient',
            'mood': 'Premium, luxurious, sophisticated'
        }
    },
    
    'Special Effects': {
        'spotlight': {
            'description': 'Professional Spotlight',
            'base_color': (40, 40, 50),
            'type': 'effect',
            'effect': 'Radial gradient - dark edges, bright center',
            'mood': 'Focus, professional product photography'
        },
        'vignette': {
            'description': 'Professional Vignette',
            'base_color': (120, 120, 140),
            'type': 'effect',
            'effect': 'Darkened edges, bright center',
            'mood': 'Refined, gallery-style presentation'
        }
    }
}

def print_color_palette():
    """Print detailed color palette information"""
    
    print("=" * 80)
    print("BACKGROUND COLOR PALETTE REFERENCE")
    print("=" * 80)
    print()
    
    for category, presets in BACKGROUND_PALETTES.items():
        print(f"\n{'='*80}")
        print(f"📍 {category}")
        print(f"{'='*80}")
        
        for preset_id, info in presets.items():
            print(f"\n  🎨 {preset_id}")
            print(f"     Name: {info['description']}")
            
            if info['type'] == 'gradient':
                r1, g1, b1 = info['color1']
                r2, g2, b2 = info['color2']
                print(f"     Type: Gradient (top to bottom)")
                print(f"     Start: RGB({r1:3d}, {g1:3d}, {b1:3d})")
                print(f"     End:   RGB({r2:3d}, {g2:3d}, {b2:3d})")
            elif info['type'] == 'solid':
                r, g, b = info['color']
                print(f"     Type: Solid Color")
                print(f"     Color: RGB({r:3d}, {g:3d}, {b:3d})")
            elif info['type'] == 'effect':
                r, g, b = info['base_color']
                print(f"     Type: Special Effect")
                print(f"     Base: RGB({r:3d}, {g:3d}, {b:3d})")
                print(f"     Effect: {info['effect']}")
            
            print(f"     Mood: {info['mood']}")
    
    print()
    print("=" * 80)
    print("📊 STATISTICS")
    print("=" * 80)
    
    total = sum(len(presets) for presets in BACKGROUND_PALETTES.values())
    gradients = sum(1 for cat in BACKGROUND_PALETTES.values() 
                   for p in cat.values() if p['type'] == 'gradient')
    solids = sum(1 for cat in BACKGROUND_PALETTES.values() 
                for p in cat.values() if p['type'] == 'solid')
    effects = sum(1 for cat in BACKGROUND_PALETTES.values() 
                 for p in cat.values() if p['type'] == 'effect')
    
    print(f"\nTotal Presets: {total}")
    print(f"  • Gradients:      {gradients}")
    print(f"  • Solid Colors:   {solids}")
    print(f"  • Special Effects: {effects}")
    print(f"\nCategories: {len(BACKGROUND_PALETTES)}")
    print()

def print_color_swatches():
    """Print color swatches using ANSI colors"""
    print("\n" + "=" * 80)
    print("🎨 COLOR SWATCHES (Terminal ANSI representation)")
    print("=" * 80)
    print()
    
    # Note: Actual terminal colors depend on terminal capabilities
    # This is representational only
    
    for category, presets in BACKGROUND_PALETTES.items():
        print(f"\n{category}")
        for preset_id, info in presets.items():
            if info['type'] == 'gradient':
                r1, g1, b1 = info['color1']
                r2, g2, b2 = info['color2']
                print(f"  {preset_id:20s} │ RGB({r1:3d},{g1:3d},{b1:3d}) → RGB({r2:3d},{g2:3d},{b2:3d})")
            elif info['type'] == 'solid':
                r, g, b = info['color']
                print(f"  {preset_id:20s} │ RGB({r:3d},{g:3d},{b:3d})")
            elif info['type'] == 'effect':
                r, g, b = info['base_color']
                print(f"  {preset_id:20s} │ RGB({r:3d},{g:3d},{b:3d}) + {info['effect']}")

if __name__ == '__main__':
    print_color_palette()
    print_color_swatches()
    print()
