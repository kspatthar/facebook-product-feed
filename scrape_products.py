import xml.etree.ElementTree as ET
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_facebook_feed():
    """Create a sample Facebook feed for testing"""
    try:
        # Create RSS root with proper namespace
        rss = ET.Element('rss')
        rss.set('version', '2.0')
        rss.set('xmlns:g', 'http://base.google.com/ns/1.0')
        
        channel = ET.SubElement(rss, 'channel')
        
        # Channel info
        ET.SubElement(channel, 'title').text = "Amazon Products Feed"
        ET.SubElement(channel, 'link').text = "https://www.amazon.in"
        ET.SubElement(channel, 'description').text = "Product feed for Facebook"
        
        # Create sample products
        sample_products = [
            {'id': 'TEST001', 'title': 'Silicone Feeding Mat', 'price': '499 INR'},
            {'id': 'TEST002', 'title': 'Stroller Hooks', 'price': '299 INR'},
            {'id': 'TEST003', 'title': 'Baby Feeding Set', 'price': '799 INR'}
        ]
        
        for product in sample_products:
            item = ET.SubElement(channel, 'item')
            ET.SubElement(item, 'g:id').text = product['id']
            ET.SubElement(item, 'g:title').text = product['title']
            ET.SubElement(item, 'g:description').text = product['title']
            ET.SubElement(item, 'g:link').text = f"https://www.amazon.in/dp/{product['id']}"
            ET.SubElement(item, 'g:image_link').text = "https://via.placeholder.com/500x500.png?text=Product+Image"
            ET.SubElement(item, 'g:condition').text = 'new'
            ET.SubElement(item, 'g:availability').text = 'in stock'
            ET.SubElement(item, 'g:price').text = product['price']
            ET.SubElement(item, 'g:brand').text = 'Amazon'
        
        # Generate XML
        xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_str += ET.tostring(rss, encoding='unicode', method='xml')
        
        # Write to file
        with open('facebook_feed.xml', 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        logger.info("Sample Facebook feed generated successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error creating feed: {e}")
        return False

if __name__ == "__main__":
    success = create_facebook_feed()
    exit(0 if success else 1)
