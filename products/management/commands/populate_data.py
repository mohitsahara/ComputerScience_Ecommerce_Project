from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from products.models import Category, Brand, Product, ProductImage, Review
from orders.models import Coupon


class Command(BaseCommand):
    help = 'Populates the database with sample TechMart data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating categories...')
        cat_data = [
            {'name': 'Smartphones', 'slug': 'smartphones',
             'description': 'Latest smartphones from top brands',
             'image_url': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&auto=format&fit=crop'},
            {'name': 'Smartwatches', 'slug': 'smartwatches',
             'description': 'Premium smartwatches and fitness trackers',
             'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&auto=format&fit=crop'},
            {'name': 'Accessories', 'slug': 'accessories',
             'description': 'Cases, chargers, and more',
             'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&auto=format&fit=crop'},
            {'name': 'Tablets', 'slug': 'tablets',
             'description': 'iPads, Android tablets, and more',
             'image_url': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&auto=format&fit=crop'},
            {'name': 'Laptops', 'slug': 'laptops',
             'description': 'Ultrabooks, gaming laptops, and more',
             'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&auto=format&fit=crop'},
        ]
        categories = {}
        for c in cat_data:
            cat, _ = Category.objects.get_or_create(slug=c['slug'], defaults=c)
            categories[c['slug']] = cat

        self.stdout.write('Creating brands...')
        brand_data = [
            {'name': 'Apple', 'slug': 'apple', 'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg'},
            {'name': 'Samsung', 'slug': 'samsung', 'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/2/24/Samsung_Logo.svg'},
            {'name': 'Google', 'slug': 'google', 'logo_url': 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg'},
            {'name': 'OnePlus', 'slug': 'oneplus', 'logo_url': ''},
            {'name': 'Sony', 'slug': 'sony', 'logo_url': ''},
            {'name': 'Garmin', 'slug': 'garmin', 'logo_url': ''},
            {'name': 'Fitbit', 'slug': 'fitbit', 'logo_url': ''},
            {'name': 'Dell', 'slug': 'dell', 'logo_url': ''},
            {'name': 'Microsoft', 'slug': 'microsoft', 'logo_url': ''},
            {'name': 'ASUS', 'slug': 'asus', 'logo_url': ''},
        ]
        brands = {}
        for b in brand_data:
            brand, _ = Brand.objects.get_or_create(slug=b['slug'], defaults=b)
            brands[b['slug']] = brand

        self.stdout.write('Creating products...')
        products_data = [
            # Smartphones
            {
                'name': 'Apple iPhone 15 Pro Max',
                'slug': 'apple-iphone-15-pro-max',
                'category': categories['smartphones'],
                'brand': brands['apple'],
                'description': 'The ultimate iPhone with titanium design, A17 Pro chip, and a 48MP camera system. Experience the most powerful smartphone ever made.',
                'specs': '• Chip: A17 Pro\n• Display: 6.7" Super Retina XDR OLED\n• Camera: 48MP Main + 12MP Ultra Wide + 12MP Telephoto\n• Battery: 4422 mAh\n• Storage: 256GB / 512GB / 1TB\n• OS: iOS 17',
                'price': '1299.00',
                'discount_price': '1199.00',
                'stock': 25,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Apple iPhone 15',
                'slug': 'apple-iphone-15',
                'category': categories['smartphones'],
                'brand': brands['apple'],
                'description': 'iPhone 15 features a stunning 6.1-inch Super Retina XDR display, Dynamic Island, and a 48MP camera.',
                'specs': '• Chip: A16 Bionic\n• Display: 6.1" Super Retina XDR\n• Camera: 48MP Main + 12MP Ultra Wide\n• Battery: 3877 mAh\n• Storage: 128GB / 256GB / 512GB\n• OS: iOS 17',
                'price': '899.00',
                'discount_price': None,
                'stock': 40,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Samsung Galaxy S24 Ultra',
                'slug': 'samsung-galaxy-s24-ultra',
                'category': categories['smartphones'],
                'brand': brands['samsung'],
                'description': 'Samsung Galaxy S24 Ultra with built-in S Pen, 200MP camera, and Snapdragon 8 Gen 3 for maximum performance.',
                'specs': '• Chip: Snapdragon 8 Gen 3\n• Display: 6.8" Dynamic AMOLED 2X, 120Hz\n• Camera: 200MP Main + 12MP Ultra Wide + 10MP + 50MP\n• Battery: 5000 mAh\n• Storage: 256GB / 512GB / 1TB\n• OS: Android 14',
                'price': '1249.00',
                'discount_price': '1099.00',
                'stock': 30,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Samsung Galaxy S24',
                'slug': 'samsung-galaxy-s24',
                'category': categories['smartphones'],
                'brand': brands['samsung'],
                'description': 'The Samsung Galaxy S24 delivers AI-powered features, a brilliant display, and all-day battery life.',
                'specs': '• Chip: Exynos 2400\n• Display: 6.2" Dynamic AMOLED 2X, 120Hz\n• Camera: 50MP Main + 12MP Ultra Wide + 10MP Telephoto\n• Battery: 4000 mAh\n• Storage: 128GB / 256GB\n• OS: Android 14',
                'price': '799.00',
                'discount_price': '749.00',
                'stock': 50,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Google Pixel 8 Pro',
                'slug': 'google-pixel-8-pro',
                'category': categories['smartphones'],
                'brand': brands['google'],
                'description': 'Google Pixel 8 Pro with the most advanced Pixel camera ever, Tensor G3 chip, and 7 years of updates.',
                'specs': '• Chip: Google Tensor G3\n• Display: 6.7" LTPO OLED, 1-120Hz\n• Camera: 50MP Main + 48MP Ultra Wide + 48MP Telephoto\n• Battery: 5050 mAh\n• Storage: 128GB / 256GB / 512GB\n• OS: Android 14',
                'price': '999.00',
                'discount_price': '899.00',
                'stock': 20,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop',
            },
            {
                'name': 'OnePlus 12',
                'slug': 'oneplus-12',
                'category': categories['smartphones'],
                'brand': brands['oneplus'],
                'description': 'OnePlus 12 — flagship speed with 100W fast charging, Hasselblad cameras, and Snapdragon 8 Gen 3.',
                'specs': '• Chip: Snapdragon 8 Gen 3\n• Display: 6.82" AMOLED, 120Hz\n• Camera: 50MP Main + 48MP Ultra Wide + 64MP Periscope\n• Battery: 5400 mAh with 100W charging\n• Storage: 256GB / 512GB\n• OS: Android 14',
                'price': '799.00',
                'discount_price': '699.00',
                'stock': 35,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Sony Xperia 1 VI',
                'slug': 'sony-xperia-1-vi',
                'category': categories['smartphones'],
                'brand': brands['sony'],
                'description': 'Sony Xperia 1 VI with professional cinema display, triple lens camera by Zeiss, and studio-quality audio.',
                'specs': '• Chip: Snapdragon 8 Gen 3\n• Display: 6.5" 4K HDR OLED\n• Camera: 12MP Main + 12MP Ultra Wide + 12MP Telephoto (3x + 7x)\n• Battery: 5000 mAh\n• Storage: 256GB\n• OS: Android 14',
                'price': '1099.00',
                'discount_price': None,
                'stock': 15,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1601784551446-20c9e07cdbdb?w=600&auto=format&fit=crop',
            },
            # Smartwatches
            {
                'name': 'Apple Watch Series 9',
                'slug': 'apple-watch-series-9',
                'category': categories['smartwatches'],
                'brand': brands['apple'],
                'description': 'Apple Watch Series 9 with the new S9 chip, double tap gesture, and the brightest Apple Watch display ever.',
                'specs': '• Chip: S9 SiP\n• Display: Always-On Retina LTPO OLED\n• Health: Heart rate, ECG, Blood Oxygen, Temperature\n• Battery: 18 hours\n• Water Resistance: 50 metres\n• Sizes: 41mm / 45mm',
                'price': '429.00',
                'discount_price': '399.00',
                'stock': 40,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Apple Watch Ultra 2',
                'slug': 'apple-watch-ultra-2',
                'category': categories['smartwatches'],
                'brand': brands['apple'],
                'description': 'Apple Watch Ultra 2 for extreme environments. The most capable and rugged Apple Watch ever.',
                'specs': '• Chip: S9 SiP\n• Display: 49mm Always-On Retina\n• Battery: 36 hours (60 hours low-power)\n• Water Resistance: 100 metres\n• Durability: MIL-STD 810H\n• GPS: L1 + L5 precision',
                'price': '799.00',
                'discount_price': None,
                'stock': 20,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1551816230-ef5deaed4a26?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Samsung Galaxy Watch 6 Classic',
                'slug': 'samsung-galaxy-watch-6-classic',
                'category': categories['smartwatches'],
                'brand': brands['samsung'],
                'description': 'Samsung Galaxy Watch 6 Classic with rotating bezel, advanced health tracking, and a premium design.',
                'specs': '• Display: 1.5" Super AMOLED\n• Health: Heart rate, ECG, Blood Pressure, Body Comp\n• Battery: Up to 40 hours\n• Processor: Exynos W930\n• OS: Wear OS 4.0\n• Sizes: 43mm / 47mm',
                'price': '369.00',
                'discount_price': '329.00',
                'stock': 30,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Garmin Fenix 7 Pro',
                'slug': 'garmin-fenix-7-pro',
                'category': categories['smartwatches'],
                'brand': brands['garmin'],
                'description': 'Garmin Fenix 7 Pro — the ultimate multisport GPS watch with solar charging and built-in flashlight.',
                'specs': '• Display: 1.3" MIP transflective\n• GPS: Multi-band + Solar Charging\n• Battery: Up to 18 days (GPS mode: 89 hours)\n• Health: VO2 max, HRV, Body Battery\n• Water: 10 ATM\n• Sports: 60+ activity profiles',
                'price': '699.00',
                'discount_price': '629.00',
                'stock': 15,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Fitbit Sense 2',
                'slug': 'fitbit-sense-2',
                'category': categories['smartwatches'],
                'brand': brands['fitbit'],
                'description': 'Fitbit Sense 2 with advanced health tools including EDA sensor for stress management and ECG.',
                'specs': '• Display: 1.58" AMOLED\n• Health: EDA, ECG, Skin temperature, SpO2\n• Battery: 6 days\n• GPS: Built-in\n• Compatibility: Android & iOS\n• Water: 50 metres',
                'price': '249.00',
                'discount_price': '199.00',
                'stock': 45,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?w=600&auto=format&fit=crop',
            },
            # Accessories
            {
                'name': 'AirPods Pro (2nd Generation)',
                'slug': 'airpods-pro-2nd-gen',
                'category': categories['accessories'],
                'brand': brands['apple'],
                'description': 'AirPods Pro with Active Noise Cancellation, Transparency Mode, Adaptive Audio, and up to 30 hours battery life.',
                'specs': '• Chip: H2\n• ANC: Next-level Active Noise Cancellation\n• Battery: 6h + 24h (case)\n• Audio: Adaptive Audio, Personalised Spatial Audio\n• Resistance: IP54',
                'price': '279.00',
                'discount_price': '249.00',
                'stock': 60,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Samsung Galaxy Buds2 Pro',
                'slug': 'samsung-galaxy-buds2-pro',
                'category': categories['accessories'],
                'brand': brands['samsung'],
                'description': 'Galaxy Buds2 Pro with 360 Audio, ANC, and Hi-Fi 24-bit audio for the best wireless experience.',
                'specs': '• Driver: 10mm woofer + 5.5mm tweeter\n• ANC: Intelligent Active Noise Cancelling\n• Battery: 5h + 18h (case)\n• Audio: 360 Audio, Hi-Fi 24-bit\n• Resistance: IPX7',
                'price': '199.00',
                'discount_price': '169.00',
                'stock': 50,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600&auto=format&fit=crop',
            },
            # Tablets
            {
                'name': 'Apple iPad Pro 12.9" M2',
                'slug': 'apple-ipad-pro-129-m2',
                'category': categories['tablets'],
                'brand': brands['apple'],
                'description': 'iPad Pro with M2 chip, Liquid Retina XDR display, and Apple Pencil hover feature.',
                'specs': '• Chip: M2\n• Display: 12.9" Liquid Retina XDR\n• Storage: 128GB - 2TB\n• Camera: 12MP + 10MP Ultra Wide\n• Battery: 10 hours\n• Connectivity: Wi-Fi 6E + 5G',
                'price': '1099.00',
                'discount_price': '999.00',
                'stock': 25,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Samsung Galaxy Tab S9 Ultra',
                'slug': 'samsung-galaxy-tab-s9-ultra',
                'category': categories['tablets'],
                'brand': brands['samsung'],
                'description': 'Samsung Galaxy Tab S9 Ultra — the largest, most powerful Galaxy Tab ever with a massive 14.6" Dynamic AMOLED display and S Pen included.',
                'specs': '• Chip: Snapdragon 8 Gen 2\n• Display: 14.6" Dynamic AMOLED 2X, 120Hz\n• RAM: 12GB\n• Storage: 256GB / 512GB\n• Camera: 13MP + 8MP Ultra Wide\n• Battery: 11200 mAh\n• Connectivity: Wi-Fi 6E + 5G',
                'price': '1199.00',
                'discount_price': '1049.00',
                'stock': 18,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1542751371-adc38448a05e?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Microsoft Surface Pro 9',
                'slug': 'microsoft-surface-pro-9',
                'category': categories['tablets'],
                'brand': brands['microsoft'],
                'description': 'Surface Pro 9 — the most flexible 2-in-1 with Intel Core i7, a stunning 13" PixelSense Flow display, and the versatility of a laptop and tablet in one.',
                'specs': '• Processor: Intel Core i7-1255U\n• Display: 13" PixelSense Flow, 120Hz\n• RAM: 16GB\n• Storage: 256GB SSD\n• Battery: Up to 15.5 hours\n• Camera: 10MP rear, 5MP front\n• OS: Windows 11',
                'price': '1299.00',
                'discount_price': '1149.00',
                'stock': 22,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1593642632559-0c6d3fc62b89?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Apple iPad Air 10.9" M1',
                'slug': 'apple-ipad-air-109-m1',
                'category': categories['tablets'],
                'brand': brands['apple'],
                'description': 'iPad Air with M1 chip, stunning 10.9" Liquid Retina display, USB-C, Touch ID, and support for Apple Pencil and Magic Keyboard.',
                'specs': '• Chip: M1\n• Display: 10.9" Liquid Retina\n• Storage: 64GB / 256GB\n• Camera: 12MP Wide + 12MP Ultra Wide (front)\n• Battery: 10 hours\n• Connectivity: Wi-Fi 6 + 5G (optional)\n• OS: iPadOS 16',
                'price': '749.00',
                'discount_price': '699.00',
                'stock': 35,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1561154464-82e9adf32764?w=600&auto=format&fit=crop',
            },
            # Laptops
            {
                'name': 'Apple MacBook Pro 14" M3 Pro',
                'slug': 'macbook-pro-14-m3-pro',
                'category': categories['laptops'],
                'brand': brands['apple'],
                'description': 'MacBook Pro 14-inch with M3 Pro chip. Supercharged for pros with incredible performance and battery life.',
                'specs': '• Chip: M3 Pro (11-core CPU, 14-core GPU)\n• Display: 14.2" Liquid Retina XDR ProMotion\n• RAM: 18GB\n• Storage: 512GB SSD\n• Battery: Up to 18 hours\n• Ports: 3x Thunderbolt 4, HDMI, SDXC, MagSafe',
                'price': '2099.00',
                'discount_price': '1999.00',
                'stock': 15,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Dell XPS 15 (2024)',
                'slug': 'dell-xps-15-2024',
                'category': categories['laptops'],
                'brand': brands['dell'],
                'description': 'Dell XPS 15 — the ultimate 15-inch laptop with a stunning OLED display, Intel Core i7 processor, and NVIDIA GeForce RTX 4060 for professionals and creators.',
                'specs': '• Processor: Intel Core i7-13700H\n• Display: 15.6" OLED 3.5K, 120Hz\n• RAM: 16GB DDR5\n• Storage: 512GB NVMe SSD\n• GPU: NVIDIA GeForce RTX 4060 8GB\n• Battery: Up to 13 hours\n• OS: Windows 11 Home',
                'price': '1799.00',
                'discount_price': '1649.00',
                'stock': 12,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=600&auto=format&fit=crop',
            },
            {
                'name': 'Microsoft Surface Laptop 5',
                'slug': 'microsoft-surface-laptop-5',
                'category': categories['laptops'],
                'brand': brands['microsoft'],
                'description': 'Surface Laptop 5 — beautifully designed with a vibrant 13.5" PixelSense touchscreen, all-day battery, and lightning-fast Intel Core i5/i7 processors.',
                'specs': '• Processor: Intel Core i5-1235U\n• Display: 13.5" PixelSense Touch, 2256×1504\n• RAM: 8GB / 16GB\n• Storage: 256GB / 512GB SSD\n• Battery: Up to 17 hours\n• Weight: 1.27 kg\n• OS: Windows 11 Home',
                'price': '1199.00',
                'discount_price': None,
                'stock': 20,
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1593642533144-3d62aa4783ec?w=600&auto=format&fit=crop',
            },
            {
                'name': 'ASUS ROG Zephyrus G14',
                'slug': 'asus-rog-zephyrus-g14',
                'category': categories['laptops'],
                'brand': brands['asus'],
                'description': 'ASUS ROG Zephyrus G14 — the ultimate compact gaming laptop powered by AMD Ryzen 9 and NVIDIA GeForce RTX 4070, with an AniMe Matrix LED lid.',
                'specs': '• Processor: AMD Ryzen 9 7940HS\n• Display: 14" QHD+ ROG Nebula Display, 165Hz\n• RAM: 16GB DDR5\n• Storage: 1TB NVMe SSD\n• GPU: NVIDIA GeForce RTX 4070 8GB\n• Battery: 76Wh, 180W charging\n• OS: Windows 11 Home',
                'price': '1699.00',
                'discount_price': '1549.00',
                'stock': 10,
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop',
            },
        ]

        for p in products_data:
            product, created = Product.objects.update_or_create(
                slug=p['slug'],
                defaults={
                    'name': p['name'],
                    'category': p['category'],
                    'brand': p.get('brand'),
                    'description': p['description'],
                    'specs': p.get('specs', ''),
                    'price': p['price'],
                    'discount_price': p.get('discount_price'),
                    'stock': p['stock'],
                    'featured': p.get('featured', False),
                    'image_url': p.get('image_url', ''),
                    'available': True,
                }
            )
            action = 'Created' if created else 'Updated'
            self.stdout.write(f'  {action}: {product.name}')

        self.stdout.write('Creating coupons...')
        now = timezone.now()
        Coupon.objects.get_or_create(
            code='TECHMART10',
            defaults={
                'discount_percent': 10,
                'max_uses': 500,
                'active': True,
                'valid_from': now,
                'valid_to': now + timedelta(days=365),
            }
        )
        Coupon.objects.get_or_create(
            code='WELCOME20',
            defaults={
                'discount_percent': 20,
                'max_uses': 100,
                'active': True,
                'valid_from': now,
                'valid_to': now + timedelta(days=30),
            }
        )
        Coupon.objects.get_or_create(
            code='SAVE15',
            defaults={
                'discount_percent': 15,
                'max_uses': 200,
                'active': True,
                'valid_from': now,
                'valid_to': now + timedelta(days=60),
            }
        )

        self.stdout.write('Creating admin user...')
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@techmart.com', 'admin123')
            self.stdout.write('  Admin user created: admin / admin123')

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully!'))
        self.stdout.write(self.style.SUCCESS('Active coupons: TECHMART10, WELCOME20, SAVE15'))
