from PIL import Image
import random
import os

class InteriorAnalyzer:
    """
    AI-powered interior design analyzer
    This is a simulated AI module with intelligent logic-based analysis
    In production, you would integrate with real computer vision models
    """
    
    def __init__(self):
        # Define style characteristics
        self.styles = {
            'modern': {
                'colors': ['#2C3E50', '#ECF0F1', '#3498DB', '#E74C3C', '#F39C12'],
                'furniture': ['Minimalist sofa', 'Glass coffee table', 'Modern pendant lights', 'Floating shelves'],
                'materials': ['Glass', 'Metal', 'Polished concrete', 'Leather']
            },
            'minimalist': {
                'colors': ['#FFFFFF', '#F5F5F5', '#E0E0E0', '#9E9E9E', '#424242'],
                'furniture': ['Low-profile sofa', 'Simple wooden table', 'Hidden storage units', 'Recessed lighting'],
                'materials': ['Light wood', 'White walls', 'Natural fabrics', 'Minimal decor']
            },
            'luxury': {
                'colors': ['#1A1A1A', '#C9B037', '#8B7355', '#FFFFFF', '#2C1810'],
                'furniture': ['Velvet sofa', 'Marble dining table', 'Crystal chandelier', 'Tufted headboard'],
                'materials': ['Marble', 'Velvet', 'Gold accents', 'Crystal', 'Silk']
            },
            'industrial': {
                'colors': ['#4A4A4A', '#8B7D6B', '#D4A574', '#1C1C1C', '#B87333'],
                'furniture': ['Leather sofa', 'Metal shelving', 'Edison bulb fixtures', 'Reclaimed wood table'],
                'materials': ['Exposed brick', 'Metal', 'Reclaimed wood', 'Concrete']
            },
            'scandinavian': {
                'colors': ['#FFFFFF', '#F0EAD6', '#D3D3D3', '#B8B8B8', '#8B4513'],
                'furniture': ['Wooden lounge chair', 'White storage units', 'Natural fiber rug', 'Simple pendant lamp'],
                'materials': ['Light wood', 'White', 'Natural textiles', 'Plants']
            },
            'traditional': {
                'colors': ['#8B4513', '#DEB887', '#F5DEB3', '#CD853F', '#2F4F4F'],
                'furniture': ['Classic sofa', 'Wooden dining set', 'Table lamps', 'Ornate mirror'],
                'materials': ['Dark wood', 'Patterned fabrics', 'Brass', 'Traditional rugs']
            }
        }
        
        # Room type detection keywords (based on image analysis simulation)
        self.room_types = ['Living Room', 'Bedroom', 'Kitchen', 'Dining Room', 'Office', 'Bathroom']
        
        # Budget-based recommendations
        self.budget_ranges = {
            'low': {'min': 500, 'max': 2000, 'quality': 'Budget-friendly'},
            'medium': {'min': 2000, 'max': 8000, 'quality': 'Mid-range'},
            'high': {'min': 8000, 'max': 50000, 'quality': 'Premium'}
        }
    
    def analyze_room(self, image_path, preferred_style='modern', budget='medium'):
        """
        Main analysis function
        Analyzes room image and provides comprehensive recommendations
        """
        # Load and analyze image
        image = Image.open(image_path)
        width, height = image.size
        
        # Detect dominant colors (simplified - analyzes image pixels)
        dominant_colors = self._detect_colors(image)
        
        # Detect room type (simulated based on image characteristics)
        room_type = self._detect_room_type(image)
        
        # Detect current style
        current_style = self._detect_current_style(dominant_colors)
        
        # Detect objects (simulated)
        detected_objects = self._detect_objects(room_type)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            room_type, 
            current_style, 
            preferred_style, 
            budget,
            detected_objects
        )
        
        # Calculate confidence score
        confidence = random.randint(85, 98)
        
        return {
            'room_type': room_type,
            'detected_style': current_style,
            'detected_objects': detected_objects,
            'dominant_colors': dominant_colors,
            'recommendations': recommendations,
            'color_palette': self.styles[preferred_style]['colors'],
            'confidence': confidence,
            'image_dimensions': f"{width}x{height}"
        }
    
    def _detect_colors(self, image):
        """Detect dominant colors from image"""
        # Resize for faster processing
        image = image.resize((150, 150))
        
        # Get colors from image (simplified algorithm)
        pixels = list(image.getdata())
        
        # Sample random pixels and convert to hex
        sampled_pixels = random.sample(pixels, min(50, len(pixels)))
        colors = []
        
        for pixel in sampled_pixels[:5]:
            if isinstance(pixel, tuple) and len(pixel) >= 3:
                hex_color = '#%02x%02x%02x' % (pixel[0], pixel[1], pixel[2])
                colors.append(hex_color)
        
        return colors if colors else ['#CCCCCC', '#999999', '#666666']
    
    def _detect_room_type(self, image):
        """Detect room type based on image analysis"""
        # Simulated detection - in production use ML model
        width, height = image.size
        aspect_ratio = width / height
        
        # Simple heuristic based on aspect ratio
        if aspect_ratio > 1.5:
            return random.choice(['Living Room', 'Dining Room'])
        elif aspect_ratio < 0.8:
            return random.choice(['Bedroom', 'Office'])
        else:
            return random.choice(self.room_types)
    
    def _detect_current_style(self, colors):
        """Detect current interior style"""
        # Analyze brightness of colors
        brightness_scores = []
        
        for color in colors[:3]:
            if color.startswith('#') and len(color) == 7:
                r = int(color[1:3], 16)
                g = int(color[3:5], 16)
                b = int(color[5:7], 16)
                brightness = (r + g + b) / 3
                brightness_scores.append(brightness)
        
        avg_brightness = sum(brightness_scores) / len(brightness_scores) if brightness_scores else 128
        
        # Style detection based on color analysis
        if avg_brightness > 200:
            return random.choice(['minimalist', 'scandinavian'])
        elif avg_brightness < 100:
            return random.choice(['luxury', 'industrial'])
        else:
            return random.choice(['modern', 'traditional'])
    
    def _detect_objects(self, room_type):
        """Detect objects in the room"""
        # Simulated object detection based on room type
        common_objects = {
            'Living Room': ['Sofa', 'Coffee table', 'TV unit', 'Curtains', 'Lighting fixtures', 'Rug'],
            'Bedroom': ['Bed', 'Nightstand', 'Wardrobe', 'Dresser', 'Lamp', 'Mirror'],
            'Kitchen': ['Cabinets', 'Countertop', 'Sink', 'Appliances', 'Lighting', 'Backsplash'],
            'Dining Room': ['Dining table', 'Chairs', 'Lighting fixture', 'Sideboard', 'Decor'],
            'Office': ['Desk', 'Office chair', 'Shelving', 'Computer', 'Lighting', 'Storage'],
            'Bathroom': ['Vanity', 'Mirror', 'Shower', 'Toilet', 'Lighting', 'Storage']
        }
        
        return random.sample(common_objects.get(room_type, ['Furniture', 'Lighting', 'Decor']), 
                           random.randint(4, 6))
    
    def _generate_recommendations(self, room_type, current_style, preferred_style, budget, objects):
        """Generate personalized recommendations"""
        style_data = self.styles[preferred_style]
        budget_data = self.budget_ranges[budget]
        
        recommendations = {
            'furniture': self._get_furniture_recommendations(room_type, style_data, budget),
            'colors': self._get_color_recommendations(style_data),
            'lighting': self._get_lighting_recommendations(room_type, style_data),
            'layout': self._get_layout_recommendations(room_type),
            'budget_estimate': self._get_budget_estimate(budget_data),
            'quick_wins': self._get_quick_wins(current_style, preferred_style),
            'materials': style_data['materials']
        }
        
        return recommendations
    
    def _get_furniture_recommendations(self, room_type, style_data, budget):
        """Get furniture recommendations"""
        base_furniture = style_data['furniture']
        
        recommendations = []
        for item in base_furniture[:3]:
            price = random.randint(200, 3000) * (1.5 if budget == 'high' else 1 if budget == 'medium' else 0.6)
            recommendations.append({
                'item': item,
                'estimated_price': f"${int(price):,}",
                'priority': random.choice(['High', 'Medium', 'Low'])
            })
        
        return recommendations
    
    def _get_color_recommendations(self, style_data):
        """Get color palette recommendations"""
        return {
            'primary': style_data['colors'][0],
            'secondary': style_data['colors'][1],
            'accent': style_data['colors'][2],
            'description': f"This palette creates a harmonious {style_data} atmosphere"
        }
    
    def _get_lighting_recommendations(self, room_type, style_data):
        """Get lighting recommendations"""
        lighting_types = {
            'Living Room': 'Layered lighting with ambient, task, and accent lights',
            'Bedroom': 'Soft, warm lighting with dimmers for relaxation',
            'Kitchen': 'Bright task lighting under cabinets and pendant lights',
            'Dining Room': 'Statement chandelier or pendant over dining table',
            'Office': 'Natural light supplemented with focused task lighting',
            'Bathroom': 'Bright, even lighting around mirror with ambient ceiling light'
        }
        
        return lighting_types.get(room_type, 'Well-balanced ambient and task lighting')
    
    def _get_layout_recommendations(self, room_type):
        """Get layout optimization tips"""
        layouts = {
            'Living Room': [
                'Create conversation zones with furniture arrangement',
                'Ensure clear traffic flow paths',
                'Position furniture away from walls for spacious feel',
                'Use area rugs to define different zones'
            ],
            'Bedroom': [
                'Center bed on main wall for focal point',
                'Leave 24-30 inches on each side of bed',
                'Position bed away from direct sunlight',
                'Create symmetry with nightstands'
            ],
            'Kitchen': [
                'Follow the work triangle principle',
                'Maximize counter space near stove and sink',
                'Ensure adequate clearance between cabinets',
                'Add task lighting in work areas'
            ]
        }
        
        return layouts.get(room_type, [
            'Maximize natural light flow',
            'Create clear pathways',
            'Balance furniture placement',
            'Use vertical space effectively'
        ])
    
    def _get_budget_estimate(self, budget_data):
        """Calculate budget estimate"""
        return {
            'range': f"${budget_data['min']:,} - ${budget_data['max']:,}",
            'quality': budget_data['quality'],
            'timeline': random.choice(['2-4 weeks', '4-6 weeks', '6-8 weeks'])
        }
    
    def _get_quick_wins(self, current_style, preferred_style):
        """Get quick improvement suggestions"""
        quick_wins = [
            'Add decorative pillows to refresh seating areas',
            'Incorporate plants for natural aesthetic',
            'Update light fixtures for modern look',
            'Add artwork or mirrors to enhance walls',
            'Declutter and reorganize for spacious feel',
            'Replace old curtains with modern window treatments'
        ]
        
        return random.sample(quick_wins, 4)
    
    def quick_detect(self, image_path):
        """Quick detection for AJAX calls"""
        image = Image.open(image_path)
        room_type = self._detect_room_type(image)
        colors = self._detect_colors(image)
        
        return {
            'room_type': room_type,
            'dominant_color': colors[0] if colors else '#CCCCCC',
            'detected': True
        }