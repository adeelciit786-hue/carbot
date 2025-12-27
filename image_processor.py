# ============================================================================
# Car Image Processor - Professional Image Processing for Maximum Conversions
# Creates eye-catching collages optimized for Facebook & maximum lead generation
# ============================================================================

from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps
from pathlib import Path
import io
from typing import List, Tuple, Dict, Optional
import numpy as np


def image_to_bytes(image: Image.Image, format='JPEG', quality=88) -> bytes:
    """Convert PIL Image to bytes for web display"""
    try:
        if image is None:
            return None
        img_io = io.BytesIO()
        if format.upper() == 'JPEG':
            image.save(img_io, format=format, quality=quality, optimize=True)
        else:
            image.save(img_io, format=format)
        img_io.seek(0)
        return img_io.getvalue()
    except Exception as e:
        print(f"Error converting image to bytes: {e}")
        return None


class CarImageProcessor:
    """Professional car image processor optimized for conversion and engagement"""
    
    # Expanded UAE & Dubai-specific backgrounds for maximum appeal
    PRESET_BACKGROUNDS = {
        # Luxury Residential
        'villa_green': '🏡 Luxury Villa with Garden',
        'villa_modern': '🏡 Modern Villa Architecture',
        'villa_pool': '🏊 Villa with Swimming Pool',
        
        # Waterfront & Beach
        'marina_blue': '🌊 Dubai Marina Waterfront',
        'marina_gold': '🌅 Marina at Sunset',
        'beach_golden': '🏖️ Golden Beach Paradise',
        'beach_sunset': '🌅 Beach Golden Hour',
        
        # Urban & Downtown
        'cityscape': '🏙️ Dubai Cityscape',
        'downtown_night': '🌃 Downtown Dubai Night',
        'emirates_towers': '🏢 Emirates District',
        
        # Nature & Desert
        'desert_sunset': '🏜️ Desert Sunset Dunes',
        'desert_golden': '🌅 Desert Golden Hour',
        'dunes_drive': '🏜️ Desert Driving Scene',
        
        # Modern Amenities
        'parking_modern': '🅿️ Modern Parking Complex',
        'parking_luxury': '🅿️ Luxury Parking Garage',
        'showroom_modern': '🏛️ Modern Showroom',
        
        # Professional & Clean
        'simple_white': '⚪ Premium White Elegant',
        'simple_gray': '⚫ Professional Gray',
        'simple_black': '◼️ Luxury Black Minimal',
        'gradient_blue': '🔵 Professional Blue Gradient',
        'gradient_gold': '✨ Luxury Gold Gradient',
        
        # Special Effects
        'spotlight': '💡 Professional Spotlight',
        'vignette': '🎯 Professional Vignette',
    }
    
    def __init__(self):
        self.max_image_size = (1200, 1200)
        self.collage_size = (1200, 800)
        self.output_dir = Path('processed_images')
        self.output_dir.mkdir(exist_ok=True)
        
        # Enhancement settings optimized for eye-catching appeal
        self.enhancement_config = {
            'contrast': 1.25,      # 25% more contrast (was 15%)
            'brightness': 1.08,    # 8% brighter (was 5%)
            'saturation': 1.18,    # 18% more saturated (was 10%)
            'sharpness': 1.15,     # 15% sharper (was 10%)
            'vibrance': 1.12       # Extra color pop
        }
    
    def calculate_image_quality_score(self, image: Image.Image) -> float:
        """
        Analyze image quality to select best photos
        Scores: brightness, contrast, edges (detail), saturation
        Returns: score 0-100
        """
        try:
            img_array = np.array(image)
            
            # Calculate metrics
            brightness = np.mean(img_array) / 255.0
            contrast = np.std(img_array) / 127.5
            
            # Detect edges (measure detail/clarity)
            edges = image.filter(ImageFilter.FIND_EDGES)
            edge_array = np.array(edges)
            edge_strength = np.mean(edge_array) / 255.0
            
            # Calculate composite score
            score = (
                (brightness * 0.2) +
                (min(contrast / 2, 1.0) * 0.2) +
                (edge_strength * 0.3) +
                (0.3)
            ) * 100
            
            return min(score, 100)
        
        except Exception as e:
            print(f"Error calculating quality score: {e}")
            return 50
    

    
    def apply_background_to_image(self, image: Image.Image, background_preset: str = 'none') -> Image.Image:
        """Apply background preset to image - creates visual background effect"""
        try:
            if background_preset == 'none' or not background_preset:
                return image
            
            # Get original image dimensions
            orig_width, orig_height = image.width, image.height
            
            # Create MUCH LARGER canvas for background effect (3.5x size - car is only ~28% of image)
            canvas_width = int(orig_width * 3.5)
            canvas_height = int(orig_height * 3.5)
            
            # Create background based on preset
            bg = self._create_background_by_preset(canvas_width, canvas_height, background_preset)
            
            # Convert image to RGBA for transparency handling
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            
            # Convert background to RGBA
            bg = bg.convert('RGBA')
            
            # Center the car image on the background (will show lots of background)
            x_offset = (canvas_width - orig_width) // 2
            y_offset = (canvas_height - orig_height) // 2
            
            # Paste the car image on top of background
            bg.paste(image, (x_offset, y_offset), image)
            
            # Convert back to RGB for output
            return bg.convert('RGB')
        
        except Exception as e:
            print(f"Error applying background: {e}")
            return image
    
    def _create_background_by_preset(self, width: int, height: int, preset: str) -> Image.Image:
        """Create realistic textured background scenes for each preset"""
        try:
            # Luxury Residential
            if preset == 'villa_green':
                return self._create_villa_green_scene(width, height)
            elif preset == 'villa_modern':
                return self._create_villa_modern_scene(width, height)
            elif preset == 'villa_pool':
                return self._create_villa_pool_scene(width, height)
            
            # Waterfront & Beach
            elif preset == 'marina_blue':
                return self._create_marina_scene(width, height)
            elif preset == 'marina_gold':
                return self._create_marina_sunset_scene(width, height)
            elif preset == 'beach_golden':
                return self._create_beach_scene(width, height)
            elif preset == 'beach_sunset':
                return self._create_sunset_beach_scene(width, height)
            
            # Urban & Downtown
            elif preset == 'cityscape':
                return self._create_cityscape_scene(width, height)
            elif preset == 'downtown_night':
                return self._create_downtown_night_scene(width, height)
            elif preset == 'emirates_towers':
                return self._create_emirates_towers_scene(width, height)
            
            # Nature & Desert
            elif preset == 'desert_sunset':
                return self._create_desert_sunset_scene(width, height)
            elif preset == 'desert_golden':
                return self._create_desert_golden_scene(width, height)
            elif preset == 'dunes_drive':
                return self._create_dunes_scene(width, height)
            
            # Modern Amenities
            elif preset == 'parking_modern':
                return self._create_modern_parking_scene(width, height)
            elif preset == 'parking_luxury':
                return self._create_luxury_parking_scene(width, height)
            elif preset == 'showroom_modern':
                return self._create_showroom_scene(width, height)
            
            # Professional & Clean
            elif preset == 'simple_white':
                return Image.new('RGB', (width, height), (255, 255, 255))
            elif preset == 'simple_gray':
                return Image.new('RGB', (width, height), (200, 200, 200))
            elif preset == 'simple_black':
                return Image.new('RGB', (width, height), (30, 30, 40))
            elif preset == 'gradient_blue':
                return self._create_gradient_background(width, height, (30, 60, 120), (100, 150, 220))
            elif preset == 'gradient_gold':
                return self._create_gradient_background(width, height, (180, 120, 0), (255, 220, 100))
            
            # Special Effects
            elif preset == 'spotlight':
                bg = Image.new('RGB', (width, height), (40, 40, 50))
                return self._add_spotlight_effect(bg)
            elif preset == 'vignette':
                bg = Image.new('RGB', (width, height), (120, 120, 140))
                return self._add_vignette_effect(bg)
            
            else:
                # Default light background
                return Image.new('RGB', (width, height), (240, 240, 245))
        
        except Exception as e:
            print(f"Error creating background preset: {e}")
            return Image.new('RGB', (width, height), (240, 240, 245))
    
    # ==================== VILLA SCENES ====================
    
    def _create_villa_green_scene(self, width: int, height: int) -> Image.Image:
        """Create garden/villa green scene"""
        bg = self._create_gradient_background(width, height, (20, 100, 20), (80, 150, 60))
        return self._add_garden_texture(bg)
    
    def _create_villa_modern_scene(self, width: int, height: int) -> Image.Image:
        """Create modern villa architecture scene"""
        bg = self._create_gradient_background(width, height, (40, 40, 60), (120, 150, 180))
        return self._add_building_pattern(bg)
    
    def _create_villa_pool_scene(self, width: int, height: int) -> Image.Image:
        """Create villa with pool water scene"""
        bg = self._create_gradient_background(width, height, (0, 80, 160), (100, 200, 220))
        return self._add_water_texture(bg)
    
    # ==================== WATERFRONT SCENES ====================
    
    def _create_marina_scene(self, width: int, height: int) -> Image.Image:
        """Create Dubai Marina waterfront scene"""
        bg = self._create_gradient_background(width, height, (0, 60, 120), (100, 180, 220))
        return self._add_water_ripples(bg)
    
    def _create_marina_sunset_scene(self, width: int, height: int) -> Image.Image:
        """Create marina sunset scene"""
        bg = self._create_gradient_background(width, height, (150, 80, 20), (255, 200, 80))
        return self._add_sunset_reflection(bg)
    
    def _create_beach_scene(self, width: int, height: int) -> Image.Image:
        """Create golden beach scene"""
        bg = self._create_gradient_background(width, height, (200, 150, 50), (255, 240, 150))
        return self._add_sand_texture(bg)
    
    def _create_sunset_beach_scene(self, width: int, height: int) -> Image.Image:
        """Create sunset beach scene"""
        bg = self._create_gradient_background(width, height, (180, 60, 20), (255, 150, 80))
        return self._add_sunset_sky_effect(bg)
    
    # ==================== CITYSCAPE SCENES ====================
    
    def _create_cityscape_scene(self, width: int, height: int) -> Image.Image:
        """Create Dubai cityscape scene"""
        bg = self._create_gradient_background(width, height, (60, 80, 100), (150, 170, 200))
        return self._add_cityscape_buildings(bg)
    
    def _create_downtown_night_scene(self, width: int, height: int) -> Image.Image:
        """Create downtown night scene"""
        bg = self._create_gradient_background(width, height, (15, 20, 40), (60, 80, 120))
        return self._add_night_lights(bg)
    
    def _create_emirates_towers_scene(self, width: int, height: int) -> Image.Image:
        """Create emirates towers district scene"""
        bg = self._create_gradient_background(width, height, (70, 100, 140), (180, 210, 240))
        return self._add_skyscraper_silhouettes(bg)
    
    # ==================== DESERT SCENES ====================
    
    def _create_desert_sunset_scene(self, width: int, height: int) -> Image.Image:
        """Create desert sunset dunes scene"""
        bg = self._create_gradient_background(width, height, (160, 50, 20), (255, 150, 50))
        return self._add_dune_pattern(bg)
    
    def _create_desert_golden_scene(self, width: int, height: int) -> Image.Image:
        """Create golden desert scene"""
        bg = self._create_gradient_background(width, height, (140, 100, 30), (255, 200, 80))
        return self._add_sand_dunes(bg)
    
    def _create_dunes_scene(self, width: int, height: int) -> Image.Image:
        """Create desert dunes driving scene"""
        bg = self._create_gradient_background(width, height, (160, 120, 60), (240, 200, 120))
        return self._add_sand_ripples(bg)
    
    # ==================== PARKING/SHOWROOM SCENES ====================
    
    def _create_modern_parking_scene(self, width: int, height: int) -> Image.Image:
        """Create modern parking complex scene"""
        bg = self._create_gradient_background(width, height, (140, 140, 150), (200, 200, 210))
        return self._add_parking_markings(bg)
    
    def _create_luxury_parking_scene(self, width: int, height: int) -> Image.Image:
        """Create luxury parking garage scene"""
        bg = self._create_gradient_background(width, height, (180, 180, 190), (220, 220, 230))
        return self._add_garage_pattern(bg)
    
    def _create_showroom_scene(self, width: int, height: int) -> Image.Image:
        """Create modern showroom scene"""
        bg = self._create_gradient_background(width, height, (120, 120, 140), (190, 190, 210))
        return self._add_showroom_lights(bg)
    
    # ==================== TEXTURE & PATTERN METHODS ====================
    
    def _add_garden_texture(self, image: Image.Image) -> Image.Image:
        """Add garden foliage texture - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGE random foliage/leaf patterns - MORE VISIBLE
        for _ in range(400):  # Doubled from 200
            x = random.randint(0, width)
            y = random.randint(int(height * 0.3), height)  # Lower half
            size = random.randint(15, 50)  # Much larger leaves
            alpha = random.randint(80, 150)  # More opaque
            color = (random.randint(0, 80), random.randint(80, 160), random.randint(0, 80), alpha)
            draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
        
        return image
    
    def _add_building_pattern(self, image: Image.Image) -> Image.Image:
        """Add modern building/architecture pattern - BOLD VERSION"""
        from PIL import ImageDraw
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGE building window patterns - VERY VISIBLE
        window_size = 40  # Much larger from 20
        for y in range(0, int(height * 0.8), window_size + 15):
            for x in range(0, width, window_size + 15):
                draw.rectangle([x, y, x+window_size, y+window_size], fill=(255, 240, 100, 100))
                # Add dark border to windows
                draw.rectangle([x, y, x+window_size, y+window_size], outline=(100, 100, 80, 150), width=2)
        
        return image
    
    def _add_water_texture(self, image: Image.Image) -> Image.Image:
        """Add water ripple texture - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGER water ripples - VERY VISIBLE
        for _ in range(200):  # Doubled
            x = random.randint(0, width)
            y = random.randint(int(height * 0.2), height)
            radius = random.randint(20, 80)  # Much larger
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], outline=(255, 255, 255, 80), width=3)
        
        return image
    
    def _add_water_ripples(self, image: Image.Image) -> Image.Image:
        """Add marina water ripples - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Horizontal water lines - MORE VISIBLE
        for y in range(0, height, 8):  # Closer together from 15
            opacity = random.randint(60, 150)  # Much more opaque
            draw.line([(0, y), (width, y)], fill=(255, 255, 255, opacity), width=2)
        
        return image
    
    def _add_sunset_reflection(self, image: Image.Image) -> Image.Image:
        """Add sunset reflection effect - BOLD VERSION"""
        from PIL import ImageDraw
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGER sun reflection on water - VERY VISIBLE
        center_x = width // 2
        center_y = int(height * 0.5)
        
        for radius in range(200, 0, 10):  # Much larger sun
            alpha = int(250 * (1 - radius/200))
            draw.ellipse(
                [center_x-radius, center_y-radius, center_x+radius, center_y+radius],
                outline=(255, 200, 50, alpha),
                width=5
            )
        
        return image
    
    def _add_sand_texture(self, image: Image.Image) -> Image.Image:
        """Add sandy beach texture - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add MUCH MORE sand grain texture - VERY VISIBLE
        for _ in range(800):  # Tripled from 300
            x = random.randint(0, width)
            y = random.randint(0, height)
            size = random.randint(2, 8)  # Larger grains
            alpha = random.randint(60, 150)  # More opaque
            color = (220, 200, 120, alpha)
            draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
        
        return image
    
    def _add_sunset_sky_effect(self, image: Image.Image) -> Image.Image:
        """Add dramatic sunset sky effect - BOLD VERSION"""
        from PIL import ImageDraw
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGE sun glow - VERY VISIBLE
        sun_x, sun_y = width // 2, int(height * 0.25)
        for radius in range(300, 0, 5):  # Much larger
            alpha = int(150 * (1 - radius/300))
            draw.ellipse(
                [sun_x-radius, sun_y-radius, sun_x+radius, sun_y+radius],
                outline=(255, 150, 30, alpha),
                width=4
            )
        
        return image
    
    def _add_cityscape_buildings(self, image: Image.Image) -> Image.Image:
        """Add cityscape building silhouettes - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGE building silhouettes - VERY VISIBLE
        num_buildings = 12  # More buildings
        building_width = width // num_buildings
        
        for i in range(num_buildings):
            x = i * building_width
            building_height = random.randint(int(height*0.25), int(height*0.75))
            draw.rectangle(
                [x, height-building_height, x+building_width, height],
                fill=(60, 80, 100, 150)
            )
            
            # Add LARGER windows - VERY VISIBLE
            for wy in range(height-building_height, height, 20):
                for wx in range(x+8, x+building_width, 20):
                    draw.rectangle([wx, wy, wx+12, wy+12], fill=(255, 240, 100, 120))
        
        return image
    
    def _add_night_lights(self, image: Image.Image) -> Image.Image:
        """Add night city lights effect - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add MANY scattered lights - VERY VISIBLE
        for _ in range(300):  # Doubled
            x = random.randint(0, width)
            y = random.randint(0, height)
            brightness = random.randint(180, 255)
            size = random.randint(3, 8)
            draw.ellipse(
                [x-size, y-size, x+size, y+size],
                fill=(brightness, brightness-30, brightness-80, 180)
            )
        
        return image
    
    def _add_skyscraper_silhouettes(self, image: Image.Image) -> Image.Image:
        """Add tall skyscraper silhouettes - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGER skyscraper silhouettes - VERY VISIBLE
        num_towers = 10  # More towers
        tower_width = width // num_towers
        
        for i in range(num_towers):
            x = i * tower_width
            tower_height = random.randint(int(height*0.35), int(height*0.85))
            draw.rectangle(
                [x, height-tower_height, x+tower_width, height],
                fill=(80, 110, 140, 160)
            )
            
            # Add MANY windows
            for wy in range(height-tower_height, height, 15):
                for wx in range(x+5, x+tower_width, 15):
                    draw.rectangle([wx, wy, wx+8, wy+8], fill=(255, 240, 100, 100))
        
        return image
    
    def _add_dune_pattern(self, image: Image.Image) -> Image.Image:
        """Add sand dune wave pattern - BOLD VERSION"""
        from PIL import ImageDraw
        import math
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add PROMINENT wavy dune lines - VERY VISIBLE
        for wave in range(8):  # More waves
            points = []
            for x in range(0, width+50, 30):  # Closer points for smoother curves
                y = int(height * (0.3 + 0.12 * wave) + 40 * math.sin(x/80 + wave))  # Larger amplitude
                points.append((x, y))
            
            if len(points) > 1:
                draw.line(points, fill=(180, 140, 60, 120), width=6)  # Thicker lines
        
        return image
    
    def _add_sand_dunes(self, image: Image.Image) -> Image.Image:
        """Add realistic sand dune formations - BOLD VERSION"""
        from PIL import ImageDraw
        import math
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGE dune formations - VERY VISIBLE
        for dune_idx in range(6):  # More dunes
            base_y = int(height * (0.25 + dune_idx * 0.12))
            
            for x in range(0, width, 20):  # Closer spacing
                amplitude = 60 + dune_idx * 30  # Larger amplitude
                wave_freq = 0.008
                y_offset = int(amplitude * math.sin(x * wave_freq + dune_idx))
                
                draw.ellipse(
                    [x-20, base_y+y_offset-15, x+20, base_y+y_offset+15],
                    fill=(200, 160, 80, 100)
                )
        
        return image
    
    def _add_sand_ripples(self, image: Image.Image) -> Image.Image:
        """Add sand ripple texture - BOLD VERSION"""
        from PIL import ImageDraw
        import math
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add PROMINENT ripple lines - VERY VISIBLE
        for y in range(0, height, 6):  # Closer together from 10
            points = []
            for x in range(0, width, 15):  # Closer points
                offset = int(8 * math.sin(x/40 + y/50))  # Larger offset
                points.append((x, y + offset))
            
            if len(points) > 1:
                draw.line(points, fill=(180, 140, 70, 100), width=2)
        
        return image
    
    def _add_parking_markings(self, image: Image.Image) -> Image.Image:
        """Add parking lot road markings - BOLD VERSION"""
        from PIL import ImageDraw
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add PROMINENT parking space lines - VERY VISIBLE
        line_spacing = 30  # Closer from 40
        for y in range(0, height, line_spacing):
            draw.line([(0, y), (width, y)], fill=(255, 255, 255, 150), width=4)  # Thicker
        
        # Add center dividing lines
        draw.line([(width//2, 0), (width//2, height)], fill=(255, 255, 0, 150), width=4)
        
        # Add side markings
        draw.line([(0, 0), (0, height)], fill=(200, 150, 50, 150), width=3)
        draw.line([(width-1, 0), (width-1, height)], fill=(200, 150, 50, 150), width=3)
        
        return image
    
    def _add_garage_pattern(self, image: Image.Image) -> Image.Image:
        """Add garage concrete pattern - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGE concrete tile pattern - VERY VISIBLE
        tile_size = 50  # From 60
        for y in range(0, height, tile_size):
            for x in range(0, width, tile_size):
                shade = random.randint(160, 190)
                draw.rectangle([x, y, x+tile_size, y+tile_size], outline=(shade, shade, shade, 150), width=3)
        
        # Add diagonal cross-hatching for concrete effect
        for x in range(0, width, 100):
            draw.line([(x, 0), (x+height, height)], fill=(150, 150, 150, 80), width=2)
        
        return image
    
    def _add_showroom_lights(self, image: Image.Image) -> Image.Image:
        """Add showroom lighting effects - BOLD VERSION"""
        from PIL import ImageDraw
        import random
        
        draw = ImageDraw.Draw(image, 'RGBA')
        width, height = image.size
        
        # Add LARGER spotlight glints - VERY VISIBLE
        for _ in range(40):  # Doubled
            x = random.randint(0, width)
            y = random.randint(0, int(height * 0.6))
            size = random.randint(10, 40)  # Much larger
            draw.ellipse([x-size, y-size, x+size, y+size], fill=(255, 255, 255, 120))
            # Add halo
            draw.ellipse([x-size-10, y-size-10, x+size+10, y+size+10], outline=(255, 255, 200, 80), width=3)
        
        return image
    
    def _create_gradient_background(self, width: int, height: int, color1: Tuple, color2: Tuple) -> Image.Image:
        """Create a gradient background from color1 to color2"""
        try:
            bg = Image.new('RGB', (width, height), color1)
            for y in range(height):
                ratio = y / height
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                
                pixels = bg.load()
                for x in range(width):
                    pixels[x, y] = (r, g, b)
            
            return bg
        except Exception as e:
            print(f"Error creating gradient: {e}")
            return Image.new('RGB', (width, height), color1)
    
    def _add_spotlight_effect(self, image: Image.Image) -> Image.Image:
        """Add spotlight effect to image"""
        try:
            width, height = image.width, image.height
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            pixels = overlay.load()
            
            center_x, center_y = width // 2, height // 2
            max_distance = ((width // 2) ** 2 + (height // 2) ** 2) ** 0.5
            
            for y in range(height):
                for x in range(width):
                    dist = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                    alpha = int(200 * (dist / max_distance))  # Darken edges
                    pixels[x, y] = (0, 0, 0, min(alpha, 200))
            
            image.paste(overlay, (0, 0), overlay)
            return image
        except Exception as e:
            print(f"Error adding spotlight: {e}")
            return image
    
    def _add_vignette_effect(self, image: Image.Image) -> Image.Image:
        """Add vignette effect (darkened edges)"""
        try:
            width, height = image.width, image.height
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            pixels = overlay.load()
            
            for y in range(height):
                for x in range(width):
                    dist_x = abs(x - width // 2) / (width // 2)
                    dist_y = abs(y - height // 2) / (height // 2)
                    dist = (dist_x ** 2 + dist_y ** 2) ** 0.5
                    alpha = int(150 * dist)
                    pixels[x, y] = (0, 0, 0, min(alpha, 150))
            
            image.paste(overlay, (0, 0), overlay)
            return image
        except Exception as e:
            print(f"Error adding vignette: {e}")
            return image

    def process_images(self, image_files: List, background_preset: str = 'none') -> Dict:
        """Main image processing with comprehensive error handling"""
        try:
            # Validate input
            if not image_files:
                return {
                    'success': False,
                    'error': 'No images provided. Please upload at least 2 images.'
                }
            
            if len(image_files) < 2:
                return {
                    'success': False,
                    'error': f'Need at least 2 images. You uploaded {len(image_files)} image(s).'
                }
            
            if len(image_files) > 25:
                return {
                    'success': False,
                    'error': 'Maximum 25 images allowed. Please reduce your selection.'
                }
            
            # Open and validate images
            images = []
            errors = []
            
            for idx, img_file in enumerate(image_files):
                try:
                    img = Image.open(img_file)
                    
                    # Validate dimensions
                    if img.size[0] < 200 or img.size[1] < 200:
                        errors.append(f"Image {idx+1}: Too small (minimum 200×200px)")
                        continue
                    
                    if img.size[0] > 10000 or img.size[1] > 10000:
                        errors.append(f"Image {idx+1}: Too large (maximum 10000×10000px)")
                        continue
                    
                    img = img.convert('RGB')
                    images.append(img)
                
                except IOError:
                    errors.append(f"Image {idx+1}: Invalid format (JPG, PNG, GIF, WebP)")
                except MemoryError:
                    errors.append(f"Image {idx+1}: Too large to process")
                except Exception as e:
                    errors.append(f"Image {idx+1}: {str(e)}")
            
            if len(images) < 2:
                error_msg = "Not enough valid images. "
                if errors:
                    error_msg += " | ".join(errors)
                return {
                    'success': False,
                    'error': error_msg
                }
            
            # Enhance all images
            enhanced_images = []
            for img in images:
                enhanced = self.enhance_image_professional(img)
                enhanced_images.append(enhanced)
            
            # Apply background to enhanced images
            background_applied_images = []
            for img in enhanced_images:
                with_bg = self.apply_background_to_image(img, background_preset)
                background_applied_images.append(with_bg)
            
            # Optimize for Facebook
            optimized_images = []
            for idx, img in enumerate(background_applied_images):
                optimized = self.optimize_for_facebook_professional(img, idx)
                optimized_images.append(optimized)
            
            # Convert all images to bytes for web transmission
            individual_bytes = []
            for img in optimized_images:
                img_bytes = image_to_bytes(img, format='JPEG', quality=88)
                if img_bytes:
                    individual_bytes.append(img_bytes)
            
            return {
                'success': True,
                'individual_images': individual_bytes,
                'image_count': len(images),
                'processed_count': len(images),
                'quality_scores': quality_scores,
                'warnings': errors if errors else [],
                'metadata': {
                    'best_for_collage': True,
                    'total_images': len(images),
                    'selected_for_post': len(best_images),
                    'quality_rating': f"{sum(quality_scores)/len(quality_scores):.1f}/100",
                    'optimization': 'Professional - Maximum Conversion',
                    'background': background_preset if background_preset != 'none' else 'Original',
                    'facebook_ready': True
                }
            }
        
        except MemoryError:
            return {
                'success': False,
                'error': 'Processing failed: Not enough memory. Try fewer/smaller images.'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Processing error: {str(e)}'
            }
    
    def enhance_image_professional(self, image: Image.Image) -> Image.Image:
        """Professional enhancement for maximum eye appeal"""
        try:
            # Contrast
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(self.enhancement_config['contrast'])
            
            # Brightness
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(self.enhancement_config['brightness'])
            
            # Saturation
            enhancer = ImageEnhance.Color(image)
            image = enhancer.enhance(self.enhancement_config['saturation'])
            
            # Sharpness
            enhancer = ImageEnhance.Sharpness(image)
            image = enhancer.enhance(self.enhancement_config['sharpness'])
            
            # Detail
            image = image.filter(ImageFilter.DETAIL)
            
            return image
        
        except Exception as e:
            print(f"Error in professional enhancement: {e}")
            return image
    
    def optimize_for_facebook_professional(self, image: Image.Image, position: int) -> Image.Image:
        """Optimize for Facebook dimensions"""
        try:
            if position == 0:
                target_width = 1200
                target_height = 630
            else:
                target_width = 1080
                target_height = 1080
            
            img_copy = image.copy()
            img_copy.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
            
            canvas = Image.new('RGB', (target_width, target_height), color=(248, 248, 248))
            
            x = (target_width - img_copy.width) // 2
            y = (target_height - img_copy.height) // 2
            canvas.paste(img_copy, (x, y))
            
            canvas = self.add_elegant_border(canvas)
            
            return canvas
        
        except Exception as e:
            print(f"Error optimizing for Facebook: {e}")
            return image
    

    
    def add_image_frame(self, image: Image.Image) -> Image.Image:
        """Add professional white frame"""
        try:
            framed = ImageOps.expand(image, border=4, fill='white')
            framed = ImageOps.expand(framed, border=1, fill=(210, 210, 210))
            return framed
        except Exception as e:
            print(f"Error adding frame: {e}")
            return image
    
    def save_for_web(self, image: Image.Image, filename: str) -> str:
        """Save optimized for web"""
        try:
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            filepath = self.output_dir / filename
            image.save(
                filepath,
                'JPEG',
                quality=88,
                optimize=True,
                progressive=True
            )
            
            return str(filepath)
        
        except Exception as e:
            print(f"Error saving image: {e}")
            return None
    
    def get_preset_backgrounds(self) -> Dict:
        """Return all available backgrounds"""
        return self.PRESET_BACKGROUNDS
    
    def apply_custom_background(self, image: Image.Image, background_desc: str) -> Image.Image:
        """Apply custom background (placeholder for rembg)"""
        try:
            return self.enhance_image_professional(image)
        except Exception as e:
            print(f"Error applying background: {e}")
            return image


def process_car_images(image_files: List, background_preference: Optional[str] = None) -> Dict:
    """Process car images for professional posting"""
    processor = CarImageProcessor()
    result = processor.process_images(image_files)
    return result

