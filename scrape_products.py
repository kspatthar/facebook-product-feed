import xml.etree.ElementTree as ET
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_facebook_feed():
    """Create Facebook feed optimized for Dular Mart Carousel ads"""
    try:
        # Create RSS root with proper namespace
        rss = ET.Element('rss')
        rss.set('version', '2.0')
        rss.set('xmlns:g', 'http://base.google.com/ns/1.0')
        
        channel = ET.SubElement(rss, 'channel')
        
        # Channel info for Dular Mart
        ET.SubElement(channel, 'title').text = "Dular Mart - Baby Products Feed"
        ET.SubElement(channel, 'link').text = "https://www.facebook.com/dualmart"
        ET.SubElement(channel, 'description').text = "Premium baby products from Dular Mart - Perfect for Facebook Carousel Ads"
        
        # Dular Mart Products (Replace with your actual products)
        dular_mart_products = [
            {
                'id': 'DM-SILICONE-001', 
                'title': 'Dular Mart Premium Silicone Feeding Mat - Large Size',
                'description': 'Waterproof, non-slip silicone feeding mat with beautiful designs. Easy to clean, food-grade material. Perfect for messy eaters!',
                'price': '499 INR',
                'image': 'https://example.com/images/silicone-mat.jpg',  # Replace with actual image URL
                'category': 'Baby Feeding'
            },
            {
                'id': 'DM-STROLLER-002', 
                'title': 'Dular Mart Heavy Duty Stroller Hooks - Pack of 2',
                'description': 'Strong metal hooks for strollers, wheelchairs, and shopping carts. Hold up to 5kg each. Makes shopping hands-free!',
                'price': '299 INR',
                'image': 'https://example.com/images/stroller-hooks.jpg',  # Replace with actual image URL
                'category': 'Stroller Accessories'
            },
            {
                'id': 'DM-FEEDING-003', 
                'title': 'Dular Mart Complete Baby Feeding Set - 5 Pieces',
                'description': 'Complete feeding set includes bowl, spoon, fork, cup, and mat. BPA-free, dishwasher safe, beautiful colors.',
                'price': '899 INR',
                'image': 'https://example.com/images/feeding-set.jpg',  # Replace with actual image URL
                'category': 'Baby Feeding'
            },
            {
                'id': 'DM-BIB-004', 
                'title': 'Dular Mart Waterproof Baby Bibs - Pack of 3',
                'description': 'Soft waterproof bibs with food catcher pocket. Easy to clean, adjustable neck, cute designs.',
                'price': '349 INR',
                'image': 'https://example.com/images/baby-bibs.jpg',  # Replace with actual image URL
                'category': 'Baby Feeding'
            },
            {
                'id': 'DM-TOY-005', 
                'title': 'Dular Mart Educational Baby Toys - Sensory Set',
                'description': 'Montessori-inspired sensory toys for baby development. Safe, non-toxic materials, various textures.',
                'price': '599 INR',
                'image': 'https://example.com/images/baby-toys.jpg',  # Replace with actual image URL
                'category': 'Baby Toys'
            }
        ]
        
        for product in dular_mart_products:
            item = ET.SubElement(channel, 'item')
            
            # REQUIRED fields for carousel
            ET.SubElement(item, 'g:id').text = product['id']
            ET.SubElement(item, 'g:title').text = product['title']
            ET.SubElement(item, 'g:description').text = product['description']
            ET.SubElement(item, 'g:link').text = f"https://www.facebook.com/dualmart/products/{product['id']}"
            ET.SubElement(item, 'g:image_link').text = product['image']
            ET.SubElement(item, 'g:condition').text = 'new'
            ET.SubElement(item, 'g:availability').text = 'in stock'
            ET.SubElement(item, 'g:price').text = product['price']
            
            # RECOMMENDED fields
            ET.SubElement(item, 'g:brand').text = 'Dular Mart'
            ET.SubElement(item, 'g:google_product_category').text = '502088'  # Baby & Toddler
            ET.SubElement(item, 'g:product_type').text = product['category']
            
        # Generate XML
        xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_str += ET.tostring(rss, encoding='unicode', method='xml')
        
        # Write to file
        with open('facebook_feed.xml', 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        logger.info("Dular Mart Facebook feed generated successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error creating feed: {e}")
        return False

if __name__ == "__main__":
    success = create_facebook_feed()
    exit(0 if success else 1)
