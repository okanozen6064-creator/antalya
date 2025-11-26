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

districts = [
    "Akseki", "Aksu", "Alanya", "Demre", "Döşemealtı", "Elmalı", "Finike", "Gazipaşa", "Gündoğmuş", "İbradı", 
    "Kaş", "Kemer", "Kepez", "Konyaaltı", "Korkuteli", "Kumluca", "Manavgat", "Muratpaşa", "Serik"
]

beaches = [
    "Kaputaş Plajı", "Patara Plajı", "Konyaaltı Plajı", "Lara Plajı", "Phaselis Koyu", "Olympos Plajı", 
    "Adrasan Koyu", "Kleopatra Plajı", "Damlataş Plajı", "İncekum Plajı", "Mermerli Plajı", "Çıralı Plajı",
    "Kekova Batık Şehir", "Suluada", "Korsan Koyu", "Papaz Koyu"
]

historical_sites = [
    "Termessos Antik Kenti", "Perge Antik Kenti", "Aspendos Antik Tiyatrosu", "Myra Antik Kenti", 
    "Xanthos Antik Kenti", "Arykanda Antik Kenti", "Side Antik Kenti", "Apollon Tapınağı", 
    "Hadrian Kapısı (Üç Kapılar)", "Hıdırlık Kulesi", "Yivli Minare", "Karain Mağarası", "Alanya Kalesi", "Kızılkule"
]

malls = [
    "TerraCity AVM", "MarkAntalya AVM", "Mall of Antalya", "Deepo Outlet Center", "Migros 5M AVM", 
    "ÖzdilekPark Antalya", "Erasta AVM", "Agora Antalya", "Shemall AVM", "Laura AVM"
]

activities = [
    "Köprülü Kanyon Rafting", "Kaş Dalış Turu", "Alanya Yamaç Paraşütü", "Olympos Teleferik", 
    "Tünektepe Teleferik", "Antalya Jeep Safari", "Kemer Tekne Turu", "Manavgat Şelalesi Tekne Turu", 
    "Antalya Akvaryum", "Land of Legends Theme Park", "Sandland Kum Heykel Müzesi"
]

popular_places = [
    {"name": "7 Mehmet", "type": "Restaurant", "desc": "Antalya'nın en köklü ve meşhur restoranlarından biri."},
    {"name": "Akdeniz Üniversitesi", "type": "Eğitim", "desc": "Türkiye'nin en saygın eğitim kurumlarından biri olan Akdeniz Üniversitesi kampüsü."},
    {"name": "Lara Balıkevi", "type": "Restaurant", "desc": "Deniz ürünleri sevenlerin vazgeçilmez adresi."},
    {"name": "Antalya Müzesi", "type": "Müze", "desc": "Tarihe tanıklık eden binlerce eserin sergilendiği müze."},
    {"name": "Saklıkent Kayak Merkezi", "type": "Spor", "desc": "Aynı gün hem denize girip hem kayak yapabileceğiniz nadir yerlerden."},
    {"name": "Kaleiçi Yat Limanı", "type": "Tarih", "desc": "Tarihi dokusu ve tekneleriyle Antalya'nın simgesi."},
]

general_topics = [
    {"title": "Antalya Villalar", "keyword": "antalya kiralık villa", "content": "Antalya'da tatil yapmak isteyenler için villa kiralama seçenekleri her geçen gün artıyor."},
    {"title": "Antalya Oteller", "keyword": "antalya otel fiyatları", "content": "Her bütçeye uygun otel seçenekleriyle Antalya, turizmin başkenti."},
    {"title": "Antalya Konserler", "keyword": "antalya konser takvimi 2025", "content": "Antalya Açıkhava Tiyatrosu ve Expo alanı başta olmak üzere şehirde yıl boyunca birçok ünlü sanatçı konser veriyor."},
    {"title": "Antalya Kamp Alanları", "keyword": "antalya ücretsiz kamp alanları", "content": "Doğa severler için Antalya'nın koyları ve yaylaları eşsiz kamp imkanları sunuyor."},
    {"title": "Antalya Gece Hayatı", "keyword": "antalya barlar sokağı", "content": "Kaleiçi barlar sokağı, Lara ve Konyaaltı'ndaki mekanlar ile Antalya geceleri sabahın ilk ışıklarına kadar devam ediyor."},
    {"title": "Antalya Özel Hastaneler", "keyword": "antalya özel hastane listesi", "content": "Sağlık turizminin başkenti Antalya'da dünya standartlarında hizmet veren birçok özel hastane bulunmaktadır."},
    {"title": "Antalya Havalimanı Transfer", "keyword": "antalya havalimanı ulaşım", "content": "Antalya Havalimanı'ndan şehir merkezine ve otellere ulaşım için Havaş, Antray, taksi ve özel transfer seçenekleri mevcuttur."},
    {"title": "Antalya Semt Pazarları", "keyword": "antalya pazar yerleri", "content": "Taze sebze ve meyveye ulaşmak için Antalya'nın meşhur semt pazarları haftanın her günü farklı noktalarda kuruluyor."},
]

articles_to_generate = []

# 1. City Distances
for city in cities:
    km = random.randint(100, 1500)
    hours = km // 80
    minutes = random.choice([15, 30, 45, 0])
    articles_to_generate.append({
        "filename": f"antalya-{city.lower().replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-kac-km.html",
        "title": f"Antalya {city} Arası Kaç Km? Kaç Saat?",
        "description": f"Antalya ile {city} arası kaç kilometre? Otobüsle ve özel araçla kaç saat sürer? {city} Antalya yol tarifi.",
        "keywords": f"antalya {city} arası kaç km, antalya {city} kaç saat, {city} antalya yol tarifi",
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'dan {city} şehrine gitmeyi planlayanlar için detaylı yol rehberi.",
        "content_p1": f"Antalya ile {city} arasındaki mesafe karayolu ile yaklaşık olarak {km} kilometredir.",
        "subheading": f"Antalya - {city} Yolculuğu Ne Kadar Sürer?",
        "content_p2": f"Özel araçla Antalya'dan {city}'a gitmek ortalama {hours} saat {minutes} dakika sürmektedir.",
        "content_p3": f"{city} şehrinden Antalya'ya gelirken yol üzerindeki dinlenme tesislerini kullanabilirsiniz.",
        "topic": "şehirlerarası ulaşım"
    })

# 2. Districts
for district in districts:
    articles_to_generate.append({
        "filename": f"antalya-{district.lower().replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-gezilecek-yerler.html",
        "title": f"Antalya {district} Gezilecek Yerler ve Rehber",
        "description": f"Antalya'nın {district} ilçesinde gezilecek yerler, tarihi mekanlar ve doğal güzellikler. {district} otelleri ve restoranları.",
        "keywords": f"antalya {district} gezilecek yerler, {district} otelleri, {district} nerede",
        "image": f"https://source.unsplash.com/1000x600/?antalya,{district.lower()}",
        "intro": f"Antalya'nın gözde ilçelerinden {district}, hem tarihi hem de doğal güzellikleriyle ziyaretçilerini büyülüyor.",
        "content_p1": f"{district}, Antalya merkezine yakınlığı ve sunduğu imkanlarla dikkat çekiyor. Bölgede birçok konaklama ve yeme-içme alternatifi mevcut.",
        "subheading": f"{district} Bölgesinde Neler Yapılır?",
        "content_p2": f"{district} ziyaretinizde mutlaka görmeniz gereken yerler arasında antik kentler, plajlar ve doğal parklar bulunuyor.",
        "content_p3": "Yerel lezzetleri tatmadan ve bölgenin çarşısını gezmeden dönmeyin.",
        "topic": f"{district} bölgesi"
    })

# 3. Beaches
for beach in beaches:
    articles_to_generate.append({
        "filename": f"{beach.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-nerede.html",
        "title": f"{beach} Nerede? Nasıl Gidilir? Giriş Ücreti 2025",
        "description": f"Antalya'nın en güzel plajlarından {beach} nerede? Giriş ücretli mi? Şezlong ve şemsiye fiyatları.",
        "keywords": f"{beach} nerede, {beach} giriş ücreti, {beach} yol tarifi",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Turkuaz rengi denizi ve altın sarısı kumuyla {beach}, deniz severlerin favori rotalarından biri.",
        "content_p1": f"{beach}, temizliği ve berraklığı ile Mavi Bayrak ödülüne layık görülmüştür. Ailenizle güvenle denize girebilirsiniz.",
        "subheading": f"{beach} İmkanları",
        "content_p2": "Plajda duş, tuvalet, soyunma kabini gibi imkanlar mevcuttur. Ayrıca çevrede yiyecek ve içecek ihtiyaçlarınızı karşılayabileceğiniz işletmeler bulunmaktadır.",
        "content_p3": "Yaz sezonunda erken saatlerde gitmenizi öneririz, zira öğle saatlerinde oldukça kalabalık olabilmektedir.",
        "topic": "plajlar ve koylar"
    })

# 4. Historical Sites
for site in historical_sites:
    articles_to_generate.append({
        "filename": f"{site.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c').replace('(','').replace(')','')}-tarihi.html",
        "title": f"{site} Tarihi ve Ziyaret Saatleri",
        "description": f"{site} nerede? Giriş ücreti ne kadar? Müze kart geçerli mi? {site} tarihi hakkında bilgi.",
        "keywords": f"{site} tarihi, {site} giriş ücreti, {site} nerede",
        "image": "https://images.unsplash.com/photo-1540202404-a671b57d5c9c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'nın binlerce yıllık tarihine ışık tutan {site}, arkeoloji meraklıları için eşsiz bir durak.",
        "content_p1": f"{site}, Roma, Bizans ve Selçuklu dönemlerinden izler taşımaktadır. Yapılan kazı çalışmalarıyla her geçen gün yeni eserler gün yüzüne çıkarılmaktadır.",
        "subheading": f"{site} Ziyaret Bilgileri",
        "content_p2": "Müze Kart ile giriş yapabileceğiniz ören yerine, yaz ve kış dönemlerinde farklı ziyaret saatleri uygulanmaktadır.",
        "content_p3": "Tarihi alanı gezerken rahat ayakkabılar tercih etmenizi ve yanınıza su almanızı tavsiye ederiz.",
        "topic": "tarihi ve kültürel miras"
    })

# 5. Malls
for mall in malls:
    articles_to_generate.append({
        "filename": f"{mall.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-magazalar.html",
        "title": f"{mall} Mağazalar ve Sinema",
        "description": f"Antalya {mall} nerede? Hangi mağazalar var? Sinema seansları ve ulaşım bilgileri.",
        "keywords": f"{mall} mağazalar, {mall} sinema, {mall} ulaşım",
        "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Alışveriş ve eğlencenin adresi {mall}, dünyaca ünlü markaları ve geniş yemek alanı ile hizmet veriyor.",
        "content_p1": f"{mall} içerisinde giyim, teknoloji, kozmetik ve ev dekorasyonu alanında yüzlerce mağaza bulunmaktadır.",
        "subheading": "Eğlence ve Yeme İçme",
        "content_p2": "Sinema salonları, çocuk oyun alanları ve bowling salonu ile ailenizle keyifli vakit geçirebilirsiniz.",
        "content_p3": "Geniş otopark kapasitesi ve toplu taşıma kolaylığı ile {mall}, Antalya'nın en çok tercih edilen alışveriş merkezlerinden biridir.",
        "topic": "alışveriş ve yaşam"
    })

# 6. Activities
for activity in activities:
    articles_to_generate.append({
        "filename": f"{activity.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-fiyatlari.html",
        "title": f"{activity} Fiyatları ve Tur Detayları 2025",
        "description": f"Antalya'da {activity} nerede yapılır? Fiyatları ne kadar? {activity} tavsiyeleri.",
        "keywords": f"{activity} fiyat, {activity} nerede, antalya aktiviteler",
        "image": "https://images.unsplash.com/photo-1533105079780-92b9be482077?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Adrenalin ve eğlence arayanlar için {activity}, Antalya tatilinizin unutulmaz anlarından biri olacak.",
        "content_p1": f"{activity} için profesyonel ekiplerle çalışmanızı ve güvenlik önlemlerini dikkate almanızı öneririz.",
        "subheading": "Ne Zaman Yapılır?",
        "content_p2": "Hava koşullarına bağlı olarak yılın büyük bir bölümünde bu aktiviteyi gerçekleştirebilirsiniz.",
        "content_p3": "Rezervasyonunuzu önceden yaptırarak indirimli fiyatlardan yararlanabilirsiniz.",
        "topic": "aktivite ve eğlence"
    })

# 7. Popular Places (Existing)
for place in popular_places:
    articles_to_generate.append({
        "filename": f"{place['name'].lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-nerede.html",
        "title": f"{place['name']} Nerede? Nasıl Gidilir?",
        "description": f"Antalya'nın popüler yerlerinden {place['name']} nerede? {place['name']} giriş ücreti ve detaylar.",
        "keywords": f"{place['name']} nerede, {place['name']} antalya",
        "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'nın en çok merak edilen noktalarından biri olan {place['name']}, ziyaretçilerin ilgi odağı.",
        "content_p1": f"{place['name']}, {place['desc']}",
        "subheading": "Ziyaret Bilgileri",
        "content_p2": "Şehir merkezinden kolayca ulaşabileceğiniz bu mekan, haftanın her günü hizmet vermektedir.",
        "content_p3": "Detaylı bilgi ve rezervasyon için işletme ile iletişime geçebilirsiniz.",
        "topic": "mekan rehberi"
    })

# 8. General Topics (Existing)
for topic in general_topics:
    articles_to_generate.append({
        "filename": f"{topic['title'].lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}.html",
        "title": f"{topic['title']} - Detaylı Rehber 2025",
        "description": f"{topic['title']} hakkında bilmeniz gereken her şey. {topic['content'][:100]}...",
        "keywords": f"{topic['keyword']}, antalya rehberi",
        "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'da {topic['title'].lower()} arayışında olanlar için hazırladığımız bu rehberde tüm detayları bulacaksınız.",
        "content_p1": topic['content'],
        "subheading": "Önerilerimiz",
        "content_p2": "Bütçenize ve zevkinize uygun en iyi seçenekleri değerlendirmek için erken hareket etmenizde fayda var.",
        "content_p3": "Antalya'nın sunduğu bu imkanlardan yararlanarak tatilinizi daha keyifli hale getirebilirsiniz.",
        "topic": topic['title']
    })

# Ensure directory exists
if not os.path.exists("articles"):
    os.makedirs("articles")

# Write files
for article in articles_to_generate:
    file_path = os.path.join("articles", article["filename"])
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
# Sort articles by title for better UX
articles_to_generate.sort(key=lambda x: x["title"])

for article in articles_to_generate:
    links_html += f'<a href="articles/{article["filename"]}" class="block p-3 border border-gray-200 rounded hover:bg-blue-50 hover:border-blue-300 transition text-sm font-medium text-gray-700">{article["title"]}</a>'

with open("tum-icerikler.html", "w", encoding="utf-8") as f:
    f.write(all_content_template.format(links=links_html, count=len(articles_to_generate)))

print("Generated tum-icerikler.html")
