# Vastra Kala Trends Business Information
BUSINESS_ID = "145759346060686"
BUSINESS_NAME = "VastraKala Trends"
BUSINESS_URL = "https://www.facebook.com/vastrakalatrends/"
PAGE_ID = "145759346060686"  # Usually same as Business ID

def create_facebook_feed():
    """Create Facebook feed for VastraKala Trends"""
    try:
        # Create RSS root with proper namespace
        rss = ET.Element('rss')
        rss.set('version', '2.0')
        rss.set('xmlns:g', 'http://base.google.com/ns/1.0')
        
        channel = ET.SubElement(rss, 'channel')
        
        # Channel info for Vastra Kala Trends
        ET.SubElement(channel, 'title').text = f"{BUSINESS_NAME} - Traditional Fashion Collection"
        ET.SubElement(channel, 'link').text = BUSINESS_URL
        ET.SubElement(channel, 'description').text = f"Handcrafted traditional fashion from {BUSINESS_NAME}. Authentic designs for modern trends."
        
        # Vastra Kala Trends Products (Replace with actual products)
        vastra_kala_products = [
            {
                'id': 'VKT-SAREE-001', 
                'title': 'Handwoven Silk Banarasi Saree - Premium Collection',
                'description': 'Authentic Banarasi silk saree with intricate zari work. Perfect for weddings and special occasions.',
                'price': '5499 INR',
                'image': 'https://example.com/banarasi-saree.jpg',
                'category': 'Traditional Sarees',
                'brand': 'Vastra Kala Trends'
            },
            {
                'id': 'VKT-SALWAR-002', 
                'title': 'Designer Embroidered Salwar Suit - Party Wear',
                'description': 'Beautifully embroidered salwar suit with dupatta. Elegant design for festive occasions.',
                'price': '2999 INR',
                'image': 'https://example.com/salwar-suit.jpg', 
                'category': 'Designer Wear',
                'brand': 'Vastra Kala Trends'
            },
            {
                'id': 'VKT-ACCESSORY-003', 
                'title': 'Handcrafted Potli Bag with Mirror Work',
                'description': 'Exquisitely handcrafted potli bag with traditional mirror work. Perfect complement to ethnic outfits.',
                'price': '1299 INR',
                'image': 'https://example.com/potli-bag.jpg',
                'category': 'Fashion Accessories',
                'brand': 'Vastra Kala Trends'
            }
        ]
        
        for product in vastra_kala_products:
            item = ET.SubElement(channel, 'item')
            
            # REQUIRED fields
            ET.SubElement(item, 'g:id').text = product['id']
            ET.SubElement(item, 'g:title').text = product['title']
            ET.SubElement(item, 'g:description').text = product['description']
            ET.SubElement(item, 'g:link').text = f"{BUSINESS_URL}products/{product['id']}"
            ET.SubElement(item, 'g:image_link').text = product['image']
            ET.SubElement(item, 'g:condition').text = 'new'
            ET.SubElement(item, 'g:availability').text = 'in stock'
            ET.SubElement(item, 'g:price').text = product['price']
            
            # RECOMMENDED fields
            ET.SubElement(item, 'g:brand').text = product['brand']
            ET.SubElement(item, 'g:google_product_category').text = '2271'  # Apparel & Accessories
            ET.SubElement(item, 'g:product_type').text = product['category']
            
        # Generate XML
        xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_str += ET.tostring(rss, encoding='unicode', method='xml')
        
        # Write to file
        with open('facebook_feed.xml', 'w', encoding='utf-8') as f:
            f.write(xml_str)
        
        logger.info(f"{BUSINESS_NAME} Facebook feed generated successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error creating feed: {e}")
        return False
