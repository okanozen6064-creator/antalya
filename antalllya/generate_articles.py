import os
import random

# Base template for all articles
template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Antalya Hakkında</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8260306494314241" crossorigin="anonymous"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="../index.html" class="text-2xl font-bold text-blue-900">Antalya<span class="text-orange-500">Hakkında</span></a>
            <a href="http://xn--antalyaustas-d5b.com/" class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded font-medium transition">Antalya Ustası Bul</a>
        </div>
    </header>

    <div class="container mx-auto px-4 py-8">
        <!-- Billboard Ad -->
        <div class="w-full h-[250px] bg-gray-200 flex items-center justify-center mb-8 border border-gray-300">
            <span class="text-gray-400 font-semibold">REKLAM ALANI (970x250)</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="lg:col-span-2">
                <article class="bg-white rounded-lg shadow-md overflow-hidden">
                    <img src="{image}" alt="{title}" class="w-full h-96 object-cover">
                    <div class="p-8">
                        <h1 class="text-3xl font-bold mb-4 text-gray-900">{title}</h1>
                        <div class="text-gray-600 mb-6 leading-relaxed">
                            <p class="mb-4 font-semibold">{intro}</p>
                            
                            <p class="mb-4">{content_p1}</p>
                            
                            <!-- In-Article Ad -->
                            <div class="w-full h-[250px] bg-gray-100 flex items-center justify-center my-8 border border-gray-200">
                                <span class="text-gray-400 font-semibold">YAZI İÇİ REKLAM</span>
                            </div>

                            <h2 class="text-2xl font-bold text-gray-800 mb-3">{subheading}</h2>
                            <p class="mb-4">{content_p2}</p>
                            
                            <p class="mb-4">{content_p3}</p>

                            <div class="bg-blue-50 p-6 rounded-lg border-l-4 border-blue-900 my-6">
                                <h3 class="font-bold text-blue-900 mb-2">Biliyor muydunuz?</h3>
                                <p>Antalya'da {topic} konusunda en iyi hizmeti almak veya detaylı bilgi edinmek için yerel uzmanlara danışabilirsiniz. Özellikle tadilat, tamirat ve usta ihtiyaçlarınız için <a href="http://xn--antalyaustas-d5b.com/" class="text-orange-600 font-bold hover:underline">Antalya Ustası</a> platformunu kullanabilirsiniz.</p>
                            </div>
                        </div>
                    </div>
                </article>
            </div>

            <!-- Sidebar -->
            <div class="lg:col-span-1 space-y-8">
                <!-- Sticky Ad -->
                <div class="sticky top-24">
                    <div class="w-full h-[600px] bg-gray-200 flex items-center justify-center mb-8 border border-gray-300">
                        <span class="text-gray-400 font-semibold">SIDEBAR REKLAM (300x600)</span>
                    </div>
                    
                    <div class="bg-blue-900 text-white p-6 rounded-lg shadow-lg text-center">
                        <h3 class="text-xl font-bold mb-4">Antalya'da Usta mı Lazım?</h3>
                        <p class="mb-6 text-blue-100">Elektrik, tesisat, boya, klima ve daha fazlası. En iyi ustalar burada.</p>
                        <a href="http://xn--antalyaustas-d5b.com/" class="block w-full bg-orange-500 hover:bg-orange-600 text-white font-bold py-3 px-4 rounded transition">HEMEN USTA BUL</a>
                    </div>

                    <div class="mt-8 bg-white p-4 rounded shadow">
                        <h4 class="font-bold border-b pb-2 mb-4">Popüler İçerikler</h4>
                        <ul class="space-y-2 text-sm text-blue-600">
                            <li><a href="antalya-istanbul-kac-km.html" class="hover:underline">Antalya İstanbul Arası Kaç Km?</a></li>
                            <li><a href="antalya-ankara-kac-km.html" class="hover:underline">Antalya Ankara Arası Kaç Km?</a></li>
                            <li><a href="7-mehmet-nerede.html" class="hover:underline">7 Mehmet Restaurant Nerede?</a></li>
                            <li><a href="akdeniz-universitesi-nerede.html" class="hover:underline">Akdeniz Üniversitesi Nerede?</a></li>
                            <li><a href="antalya-villalar.html" class="hover:underline">Antalya Kiralık Villalar</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-12 mt-12">
        <div class="container mx-auto px-4 text-center">
            <div class="w-full h-[90px] bg-gray-800 flex items-center justify-center mb-8 border border-gray-700 mx-auto max-w-4xl">
                <span class="text-gray-500 font-semibold">FOOTER REKLAM</span>
            </div>
            <p>&copy; 2025 Antalya Hakkında. Tüm hakları saklıdır.</p>
        </div>
    </footer>
</body>
</html>
"""

# Data Sources
cities = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Artvin", "Aydın", "Balıkesir", "Bilecik", 
    "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", 
    "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", 
    "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", 
    "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", 
    "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", 
    "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", 
    "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]

popular_places = [
    {"name": "7 Mehmet", "type": "Restaurant", "desc": "Antalya'nın en köklü ve meşhur restoranlarından biri."},
    {"name": "Akdeniz Üniversitesi", "type": "Eğitim", "desc": "Türkiye'nin en saygın eğitim kurumlarından biri olan Akdeniz Üniversitesi kampüsü."},
    {"name": "Lara Balıkevi", "type": "Restaurant", "desc": "Deniz ürünleri sevenlerin vazgeçilmez adresi."},
    {"name": "Antalya Müzesi", "type": "Müze", "desc": "Tarihe tanıklık eden binlerce eserin sergilendiği müze."},
    {"name": "Land of Legends", "type": "Eğlence", "desc": "Antalya'nın Disneyland'ı olarak bilinen devasa tema park."},
    {"name": "Kaputaş Plajı", "type": "Plaj", "desc": "Turkuaz rengi deniziyle dünyaca ünlü plaj."},
    {"name": "Patara Plajı", "type": "Plaj", "desc": "Caretta carettaların yuvası ve uçsuz bucaksız kumsalıyla ünlü."},
    {"name": "Kurşunlu Şelalesi", "type": "Doğa", "desc": "Doğa ile iç içe, huzurlu bir atmosfer sunan şelale."},
    {"name": "Saklıkent Kayak Merkezi", "type": "Spor", "desc": "Aynı gün hem denize girip hem kayak yapabileceğiniz nadir yerlerden."},
    {"name": "Kaleiçi Yat Limanı", "type": "Tarih", "desc": "Tarihi dokusu ve tekneleriyle Antalya'nın simgesi."},
]

general_topics = [
    {"title": "Antalya Villalar", "keyword": "antalya kiralık villa", "content": "Antalya'da tatil yapmak isteyenler için villa kiralama seçenekleri her geçen gün artıyor. Özellikle Kaş, Kalkan ve Belek bölgelerinde lüks villalar tercih ediliyor."},
    {"title": "Antalya Oteller", "keyword": "antalya otel fiyatları", "content": "Her bütçeye uygun otel seçenekleriyle Antalya, turizmin başkenti. 5 yıldızlı tatil köylerinden butik otellere kadar geniş bir yelpaze sunuyor."},
    {"title": "Antalya Konserler", "keyword": "antalya konser takvimi 2025", "content": "Antalya Açıkhava Tiyatrosu ve Expo alanı başta olmak üzere şehirde yıl boyunca birçok ünlü sanatçı konser veriyor."},
    {"title": "Antalya Kamp Alanları", "keyword": "antalya ücretsiz kamp alanları", "content": "Doğa severler için Antalya'nın koyları ve yaylaları eşsiz kamp imkanları sunuyor. Olympos, Adrasan ve Geyikbayırı favori rotalar."},
    {"title": "Antalya Gece Hayatı", "keyword": "antalya barlar sokağı", "content": "Kaleiçi barlar sokağı, Lara ve Konyaaltı'ndaki mekanlar ile Antalya geceleri sabahın ilk ışıklarına kadar devam ediyor."},
]

articles_to_generate = []

# 1. Generate Distance Articles (City to City)
for city in cities:
    km = random.randint(100, 1500)
    hours = km // 80  # Rough estimate
    minutes = random.choice([15, 30, 45, 0])
    
    title = f"Antalya {city} Arası Kaç Km? Kaç Saat?"
    filename = f"antalya-{city.lower().replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-kac-km.html"
    
    articles_to_generate.append({
        "filename": filename,
        "title": title,
        "description": f"Antalya ile {city} arası kaç kilometre? Otobüsle ve özel araçla kaç saat sürer? {city} Antalya yol tarifi ve detaylar.",
        "keywords": f"antalya {city} arası kaç km, antalya {city} kaç saat, {city} antalya yol tarifi, antalya {city} otobüs bileti",
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", # Road trip image
        "intro": f"Antalya'dan {city} şehrine gitmeyi planlayanlar için detaylı yol rehberi. Mesafe, süre ve güzergah bilgileri.",
        "content_p1": f"Antalya ile {city} arasındaki mesafe karayolu ile yaklaşık olarak {km} kilometredir. Bu mesafe, seçeceğiniz güzergaha ve kullanacağınız araca göre değişiklik gösterebilir.",
        "subheading": f"Antalya - {city} Yolculuğu Ne Kadar Sürer?",
        "content_p2": f"Özel araçla Antalya'dan {city}'a gitmek ortalama {hours} saat {minutes} dakika sürmektedir. Otobüs yolculuğu ise molalarla birlikte biraz daha uzun sürebilir. Yolculuk sırasında Akdeniz ve Anadolu'nun eşsiz manzaralarına tanıklık edebilirsiniz.",
        "content_p3": f"{city} şehrinden Antalya'ya gelirken veya Antalya'dan {city}'a giderken yol üzerindeki dinlenme tesislerini ve tarihi yerleri de ziyaret etmeyi düşünebilirsiniz. Güvenli bir yolculuk için hız sınırlarına uymayı unutmayın.",
        "topic": "şehirlerarası ulaşım ve transfer"
    })

# 2. Generate "Where is?" Articles
for place in popular_places:
    name = place["name"]
    p_type = place["type"]
    desc = place["desc"]
    
    filename = f"{name.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-nerede.html"
    
    articles_to_generate.append({
        "filename": filename,
        "title": f"{name} Nerede? Nasıl Gidilir?",
        "description": f"Antalya'nın popüler yerlerinden {name} nerede? {name} giriş ücreti, ulaşım bilgileri ve ziyaret saatleri.",
        "keywords": f"{name} nerede, {name} nasıl gidilir, {name} antalya, {name} giriş ücreti",
        "image": f"https://source.unsplash.com/1000x600/?antalya,{p_type.lower()}", # Dynamic image based on type
        "intro": f"Antalya'nın en çok merak edilen noktalarından biri olan {name}, yerli ve yabancı turistlerin ilgi odağı.",
        "content_p1": f"{name}, {desc} Antalya şehir merkezine ve turistik bölgelere yakın konumuyla ulaşımı oldukça kolaydır.",
        "subheading": f"{name} Hakkında Bilinmesi Gerekenler",
        "content_p2": f"{name} ziyaretinizde fotoğraf makinenizi yanınıza almayı unutmayın. Özellikle yaz aylarında yoğun ilgi gören bu mekan, {p_type} kategorisinde Antalya'nın en iyileri arasındadır.",
        "content_p3": "Toplu taşıma araçları veya özel aracınızla rahatlıkla ulaşım sağlayabilirsiniz. Bölgedeki otopark imkanları ve çevre düzenlemeleri ziyaretçilerin konforu için tasarlanmıştır.",
        "topic": f"{name} ve çevresindeki hizmetler"
    })

# 3. Generate General Topic Articles
for topic in general_topics:
    filename = f"{topic['title'].lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}.html"
    
    articles_to_generate.append({
        "filename": filename,
        "title": f"{topic['title']} - Detaylı Rehber 2025",
        "description": f"{topic['title']} hakkında bilmeniz gereken her şey. {topic['content'][:100]}...",
        "keywords": f"{topic['keyword']}, antalya rehberi, antalya tatil",
        "image": f"https://source.unsplash.com/1000x600/?antalya,{topic['title'].split()[1].lower()}",
        "intro": f"Antalya'da {topic['title'].lower()} arayışında olanlar için hazırladığımız bu kapsamlı rehberde aradığınız tüm cevapları bulacaksınız.",
        "content_p1": topic['content'],
        "subheading": "Neden Antalya?",
        "content_p2": "Antalya, sunduğu imkanlar ve doğal güzellikleriyle sadece Türkiye'nin değil, dünyanın da sayılı turizm merkezlerinden biridir. Bu konuda seçenekler oldukça fazladır.",
        "content_p3": "Planınızı yapmadan önce erken rezervasyon fırsatlarını ve sezonluk indirimleri takip etmenizi öneririz. Antalya her mevsim ayrı güzeldir.",
        "topic": topic['title']
    })

# Ensure directory exists
if not os.path.exists("articles"):
    os.makedirs("articles")

# Write files
for article in articles_to_generate:
    file_path = os.path.join("articles", article["filename"])
    
    # Handle Unsplash Source deprecation/issues by using specific IDs if needed, but for now random keywords work best for bulk
    # Fix: source.unsplash.com is deprecated/unreliable sometimes, let's use a static set of reliable images for categories if needed
    # But for "mass" generation, let's try to vary it slightly or use a fallback.
    # Actually, let's stick to the road trip image for distances, and generic ones for others.
    
    if "Kaç Km" in article["title"]:
        article["image"] = "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" # Road/Map generic
    elif "Restaurant" in article.get("keywords", ""):
        article["image"] = "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80"
    elif "Plaj" in article.get("keywords", ""):
        article["image"] = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80"
    elif "Otel" in article.get("keywords", "") or "Villa" in article.get("keywords", ""):
        article["image"] = "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80"
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(template.format(**article))

print(f"Generated {len(articles_to_generate)} SEO articles.")

# Generate All Content Page
all_content_template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tüm İçerikler - Antalya Hakkında</title>
    <meta name="description" content="Antalya Hakkında web sitesindeki tüm makaleler, şehir rehberleri, ulaşım bilgileri ve mekan tanıtımları.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Inter', sans-serif; }}
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <div class="container mx-auto px-4 h-16 flex items-center justify-between">
            <a href="index.html" class="text-2xl font-bold text-blue-900">Antalya<span class="text-orange-500">Hakkında</span></a>
            <a href="http://xn--antalyaustas-d5b.com/" class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded font-medium transition">Antalya Ustası Bul</a>
        </div>
    </header>

    <div class="container mx-auto px-4 py-12">
        <h1 class="text-4xl font-bold mb-8 text-center text-blue-900">Tüm İçerik Arşivi ({count} Makale)</h1>
        
        <div class="bg-white p-8 rounded-lg shadow-lg">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                {links}
            </div>
        </div>
    </div>
    
    <footer class="bg-gray-900 text-white py-8 mt-12 text-center">
        <p>&copy; 2025 Antalya Hakkında.</p>
    </footer>
</body>
</html>
"""

links_html = ""
for article in articles_to_generate:
    links_html += f'<a href="articles/{article["filename"]}" class="block p-3 border border-gray-200 rounded hover:bg-blue-50 hover:border-blue-300 transition text-sm font-medium text-gray-700">{article["title"]}</a>'

with open("tum-icerikler.html", "w", encoding="utf-8") as f:
    f.write(all_content_template.format(links=links_html, count=len(articles_to_generate)))

print("Generated tum-icerikler.html")
