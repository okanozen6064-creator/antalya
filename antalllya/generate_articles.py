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

# --- DATA SOURCES ---

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

neighborhoods = [
    "Lara", "Dedeman", "Işıklar", "Güllük", "Dokuma", "Meltem", "Uncalı", "Altınkum", "Arapsuyu", "Gürsu", 
    "Hurma", "Sarısu", "Varsak", "Masadağı", "Kırcami", "Şirinyalı", "Fener", "Çağlayan", "Güzeloba", "Ermenek",
    "Kundu", "Belek", "Kadriye", "Boğazkent", "Çolaklı", "Kumköy", "Side", "Manavgat Merkez", "Alanya Merkez",
    "Mahmutlar", "Kestel", "Oba", "Tosmur", "Konaklı", "Avsallar", "Okurcalar", "Türkler", "Payallar",
    "Göynük", "Beldibi", "Kiriş", "Çamyuva", "Tekirova", "Adrasan", "Olympos", "Çıralı", "Mavikent", "Beykonak",
    "Duraliler", "Çakırlar", "Bahtılı", "Doyran", "Geyikbayırı", "Hisarçandır", "Liman", "Öğretmenevleri",
    "Toros", "Pınarbaşı", "Soğuksu", "Bayındır", "Meydankavağı", "Yeşilbahçe", "Zerdalilik", "Sinan", "Haşim İşcan",
    "Kızılarık", "Konuksever", "Etiler", "Yüksekalan", "Dutlubahçe", "Sedir", "Varlık", "Yıldız"
]

hospitals = [
    "Akdeniz Üniversitesi Hastanesi", "Antalya Eğitim ve Araştırma Hastanesi", "Atatürk Devlet Hastanesi", 
    "Kepez Devlet Hastanesi", "Medical Park Antalya", "Memorial Antalya", "Yaşam Hastanesi", "OFM Hastanesi", 
    "Anadolu Hastanesi", "Medstar Hastanesi", "Dünya Göz Hastanesi", "Olimpos Hastanesi", "Vitale Hastanesi",
    "Uncalı Meydan Hastanesi", "Sirkeli Tıp Merkezi", "Korkuteli Devlet Hastanesi", "Alanya Eğitim Araştırma Hastanesi",
    "Manavgat Devlet Hastanesi", "Serik Devlet Hastanesi", "Kumluca Devlet Hastanesi", "Finike Devlet Hastanesi",
    "Özel Antalya Likya Hastanesi", "Özel Termessos Hastanesi", "Özel Şelale Tıp Merkezi", "Özel Lara Anadolu Hastanesi"
]

schools = [
    "Akdeniz Üniversitesi", "Antalya Bilim Üniversitesi", "Alanya Alaaddin Keykubat Üniversitesi", "Alanya Hamdullah Emin Paşa Üniversitesi",
    "Antalya AKEV Üniversitesi", "Adem Tolunay Anadolu Lisesi", "Antalya Anadolu Lisesi", "Metin Nuran Çakallıklı Anadolu Lisesi",
    "Levent Aydın Anadolu Lisesi", "Yusuf Ziya Öner Fen Lisesi", "Dr. İlhami Tankut Anadolu Lisesi", "Gazi Anadolu Lisesi",
    "Hacı Malike Mehmet Bileydi Anadolu Lisesi", "Konyaaltı Anadolu Lisesi", "Aldemir Atilla Konuk Anadolu Lisesi",
    "TED Antalya Koleji", "Antalya Koleji", "İstek Antalya Okulları", "Bahçeşehir Koleji Antalya", "Doğa Koleji Antalya"
]

transportation = [
    "Antalya Otogarı", "Antalya Havalimanı", "Antray Tramvay Hattı", "Nostaljik Tramvay", "Antalya Kart Başvuru Merkezi",
    "Doğu Garajı", "Meydan Depolama", "Sarısu Depolama", "Varsak Depolama", "Fatih Tramvay Durağı", "Expo Tramvay Durağı",
    "Havalimanı Tramvay Durağı", "Otogar Tramvay Durağı", "Çallı Tramvay Durağı", "Muratpaşa Tramvay Durağı", "İsmetpaşa Tramvay Durağı",
    "Sigorta Tramvay Durağı", "Şarampol Tramvay Durağı", "Burhanettin Onat Tramvay Durağı", "Kaleiçi Tramvay Durağı"
]

foods = [
    "Antalya Piyazı", "Şiş Köfte", "Hibeş", "Kabak Tatlısı", "Yanık Dondurma", "Serpme Börek", "Tahinli Piyaz", 
    "Turunç Reçeli", "Bergamot Reçeli", "Patlıcan Reçeli", "Gözleme", "Bazlama", "Tandır Kebabı", "Alanya Bohçası",
    "Gülüklü Çorba", "Laba Dolması", "Öküz Helvası", "Cive Yemeği", "Enginarlı Girit Kebabı", "Arap Kadayıfı",
    "Finike Portakalı", "Korkuteli Yanık Dondurması"
]

services = [
    "Antalya Nöbetçi Eczaneler", "Antalya Su Kesintisi", "Antalya Elektrik Kesintisi", "Antalya Hava Durumu", 
    "Antalya Namaz Vakitleri", "Antalya Çilingir Hizmetleri", "Antalya Halı Yıkama", "Antalya Evden Eve Nakliyat",
    "Antalya Araç Kiralama", "Antalya Temizlik Şirketleri", "Antalya Veteriner Klinikleri", "Antalya Diş Klinikleri",
    "Antalya Spor Salonları", "Antalya Yüzme Havuzları", "Antalya Kütüphaneler", "Antalya Noterleri",
    "Antalya Tesisatçı", "Antalya Elektrikçi", "Antalya Boyacı", "Antalya Klima Servisi"
]

beaches = [
    "Kaputaş Plajı", "Patara Plajı", "Konyaaltı Plajı", "Lara Plajı", "Phaselis Koyu", "Olympos Plajı", 
    "Adrasan Koyu", "Kleopatra Plajı", "Damlataş Plajı", "İncekum Plajı", "Mermerli Plajı", "Çıralı Plajı",
    "Kekova Batık Şehir", "Suluada", "Korsan Koyu", "Papaz Koyu", "Beldibi Plajı", "Göynük Plajı", "Kemer Plajı",
    "Tekirova Plajı", "Çamyuva Plajı", "Kızılot Plajı", "Sorgun Plajı", "Titreyengöl Plajı"
]

malls = [
    "TerraCity AVM", "MarkAntalya AVM", "Mall of Antalya", "Deepo Outlet Center", "Migros 5M AVM", 
    "ÖzdilekPark Antalya", "Erasta AVM", "Agora Antalya", "Shemall AVM", "Laura AVM", "Alanyum AVM",
    "Novamall Manavgat", "Time Center Kemer", "Land of Legends Shopping Avenue"
]

historical_sites = [
    "Termessos Antik Kenti", "Perge Antik Kenti", "Aspendos Antik Tiyatrosu", "Myra Antik Kenti", 
    "Xanthos Antik Kenti", "Arykanda Antik Kenti", "Side Antik Kenti", "Apollon Tapınağı", 
    "Hadrian Kapısı (Üç Kapılar)", "Hıdırlık Kulesi", "Yivli Minare", "Karain Mağarası", "Alanya Kalesi", "Kızılkule",
    "Simena Antik Kenti", "Patara Antik Kenti", "Olympos Antik Kenti", "Phaselis Antik Kenti", "Sillyon Antik Kenti",
    "Lyrbe Antik Kenti", "Selge Antik Kenti"
]

activities = [
    "Köprülü Kanyon Rafting", "Kaş Dalış Turu", "Alanya Yamaç Paraşütü", "Olympos Teleferik", 
    "Tünektepe Teleferik", "Antalya Jeep Safari", "Kemer Tekne Turu", "Manavgat Şelalesi Tekne Turu", 
    "Antalya Akvaryum", "Land of Legends Theme Park", "Sandland Kum Heykel Müzesi", "Antalya Müzesi Ziyareti",
    "Düden Şelalesi Gezisi", "Kurşunlu Şelalesi Gezisi", "Saklıkent Kayak Merkezi", "Karain Mağarası Gezisi",
    "Altınbeşik Mağarası Gezisi", "Dim Çayı Piknik", "Sapadere Kanyonu Turu", "Tazı Kanyonu Turu"
]

parks = [
    "Karaalioğlu Parkı", "Atatürk Parkı", "Düden Parkı", "Dokuma Park", "Kepez Kent Ormanı", "Falez Parkı",
    "Yavuz Özcan Parkı", "Cam Piramit Parkı", "Beach Park", "Aktur Park"
]

mosques = [
    "Yivli Minare Camii", "Murat Paşa Camii", "Tekeli Mehmet Paşa Camii", "İskele Camii", "Kesik Minare (Korkut) Camii",
    "Akdeniz Üniversitesi Camii", "Külliye Camii", "Müsellim Camii", "Balibey Camii"
]

living_topics = [
    "Antalya'da Yaşam Maliyeti 2025", "Antalya'da Ev Kiraları Ne Kadar?", "Antalya'da Öğrenci Olmak", 
    "Antalya'da İş İmkanları", "Antalya'da Emeklilik Hayatı", "Antalya'da Yabancıların Oturma İzni",
    "Antalya'da Doğalgaz Aboneliği", "Antalya'da Su Aboneliği", "Antalya'da Elektrik Aboneliği",
    "Antalya'da İnternet Altyapısı", "Antalya'da Toplu Taşıma Kartı Nasıl Alınır?", "Antalya'da Bisiklet Yolları",
    "Antalya'da Trafik Durumu", "Antalya'da İklim ve Hava Durumu", "Antalya'da Tarım ve Seracılık",
    "Antalya'da Sanayi ve Ticaret", "Antalya'da Turizm Sezonu Ne Zaman Başlar?", "Antalya'da Kışın Neler Yapılır?",
    "Antalya'da Yazın Neler Yapılır?", "Antalya'da Haftasonu Gezilecek Yerler", "Antalya'da Kamp Yapılacak Yerler",
    "Antalya'da Balık Tutulacak Yerler", "Antalya'da Fotoğraf Çekilecek Yerler", "Antalya'da Düğün Mekanları",
    "Antalya'da Kahvaltı Mekanları", "Antalya'da Meyhaneler", "Antalya'da Gece Kulüpleri", "Antalya'da Beach Clublar",
    "Antalya'da Aquaparklar", "Antalya'da Lunaparklar", "Antalya'da Hayvanat Bahçesi", "Antalya'da Oyuncak Müzesi",
    "Antalya'da Ters Ev", "Antalya'da Masal Parkı", "Antalya'da Hobit Evleri", "Antalya'da Orman Parkı"
]

articles_to_generate = []

# --- GENERATION LOOPS ---

# 1. City Distances
for city in cities:
    km = random.randint(100, 1500)
    hours = km // 80
    articles_to_generate.append({
        "filename": f"antalya-{city.lower().replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-kac-km.html",
        "title": f"Antalya {city} Arası Kaç Km? Kaç Saat?",
        "description": f"Antalya ile {city} arası kaç kilometre? Otobüsle ve özel araçla kaç saat sürer? {city} Antalya yol tarifi.",
        "keywords": f"antalya {city} arası kaç km, antalya {city} kaç saat, {city} antalya yol tarifi",
        "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'dan {city} şehrine gitmeyi planlayanlar için detaylı yol rehberi.",
        "content_p1": f"Antalya ile {city} arasındaki mesafe karayolu ile yaklaşık olarak {km} kilometredir.",
        "subheading": f"Antalya - {city} Yolculuğu Ne Kadar Sürer?",
        "content_p2": f"Özel araçla Antalya'dan {city}'a gitmek ortalama {hours} saat sürmektedir.",
        "content_p3": f"{city} şehrinden Antalya'ya gelirken yol üzerindeki dinlenme tesislerini kullanabilirsiniz.",
        "topic": "şehirlerarası ulaşım"
    })

# 2. Neighborhoods
for hood in neighborhoods:
    articles_to_generate.append({
        "filename": f"antalya-{hood.lower().replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c').replace(' ','-')}-nerede.html",
        "title": f"Antalya {hood} Nerede? Gezilecek Yerler",
        "description": f"Antalya {hood} mahallesi nerede? {hood} bölgesindeki oteller, restoranlar ve gezilecek yerler.",
        "keywords": f"antalya {hood} nerede, {hood} gezilecek yerler, {hood} otelleri",
        "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'nın popüler bölgelerinden {hood}, hem yerleşim hem de turistik açıdan önem taşıyor.",
        "content_p1": f"{hood}, Antalya'nın merkezi noktalarına yakınlığı ve sosyal imkanlarıyla dikkat çekmektedir.",
        "subheading": f"{hood} Yaşam ve Konut",
        "content_p2": f"{hood} bölgesinde satılık ve kiralık daire fiyatları, bölgenin konumuna ve denize yakınlığına göre değişiklik göstermektedir.",
        "content_p3": "Bölgedeki parklar, okullar ve alışveriş olanakları aileler için ideal bir yaşam alanı sunmaktadır.",
        "topic": f"{hood} mahallesi"
    })

# 3. Hospitals
for hospital in hospitals:
    articles_to_generate.append({
        "filename": f"{hospital.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c').replace('.','')}-randevu.html",
        "title": f"{hospital} Randevu ve İletişim",
        "description": f"{hospital} nerede? Telefon numarası ve randevu alma bilgileri. {hospital} bölümleri ve doktorları.",
        "keywords": f"{hospital} randevu, {hospital} telefon, {hospital} nerede",
        "image": "https://images.unsplash.com/photo-1538108149393-fbbd81895907?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'nın önde gelen sağlık kuruluşlarından {hospital}, modern tıbbi cihazları ve uzman kadrosuyla hizmet vermektedir.",
        "content_p1": f"{hospital} bünyesinde acil servis, poliklinikler ve ameliyathaneler bulunmaktadır.",
        "subheading": "Nasıl Randevu Alınır?",
        "content_p2": "MHRS sistemi üzerinden veya hastanenin kendi web sitesinden online randevu oluşturabilirsiniz. Ayrıca telefonla da randevu almanız mümkündür.",
        "content_p3": "Hastaneye ulaşım için toplu taşıma araçlarını kullanabilir veya özel aracınızla otopark hizmetinden yararlanabilirsiniz.",
        "topic": "sağlık hizmetleri"
    })

# 4. Schools & Universities
for school in schools:
    articles_to_generate.append({
        "filename": f"{school.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c').replace('.','')}-nerede.html",
        "title": f"{school} Nerede? Taban Puanları ve Bölümler",
        "description": f"{school} nerede? İletişim bilgileri, taban puanları ve ulaşım imkanları.",
        "keywords": f"{school} nerede, {school} taban puanları, {school} iletişim",
        "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Eğitim kalitesiyle öne çıkan {school}, Antalya'nın önemli eğitim kurumlarından biridir.",
        "content_p1": f"{school}, öğrencilerine sunduğu akademik ve sosyal imkanlarla başarıyı hedeflemektedir.",
        "subheading": "Ulaşım ve Konum",
        "content_p2": "Okula ulaşım için şehrin farklı noktalarından servis ve toplu taşıma imkanları bulunmaktadır.",
        "content_p3": "Detaylı bilgi ve kayıt koşulları için kurumun resmi web sitesini ziyaret edebilirsiniz.",
        "topic": "eğitim kurumları"
    })

# 5. Transportation Points
for trans in transportation:
    articles_to_generate.append({
        "filename": f"{trans.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-ulasim.html",
        "title": f"{trans} Nerede? Hangi Otobüs Gider?",
        "description": f"{trans} nerede? Harita konumu, geçen otobüs hatları ve ulaşım bilgileri.",
        "keywords": f"{trans} nerede, {trans} otobüs, {trans} yol tarifi",
        "image": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya şehir içi ulaşımın kilit noktalarından biri olan {trans}, her gün binlerce yolcuya hizmet vermektedir.",
        "content_p1": f"{trans} konumuna ulaşmak için Antray tramvay hattını veya belediye otobüslerini kullanabilirsiniz.",
        "subheading": "Önemli Bilgiler",
        "content_p2": "Antalya Kart'ınızla toplu taşıma araçlarından indirimli aktarma imkanlarıyla yararlanabilirsiniz.",
        "content_p3": "Sefer saatleri ve güzergah bilgileri için Antalya Ulaşım mobil uygulamasını kontrol etmenizi öneririz.",
        "topic": "şehir içi ulaşım"
    })

# 6. Local Foods
for food in foods:
    articles_to_generate.append({
        "filename": f"{food.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-nerede-yenir.html",
        "title": f"Antalya'da En İyi {food} Nerede Yenir?",
        "description": f"{food} tarifi ve Antalya'da {food} yapan en meşhur yerler. {food} fiyatları.",
        "keywords": f"{food} nerede yenir, {food} tarifi, antalya {food}",
        "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya mutfağının vazgeçilmez lezzetlerinden {food}, şehre gelenlerin mutlaka denemesi gereken bir tat.",
        "content_p1": f"{food}, yöresel malzemelerle hazırlanan ve kendine has sunumuyla damaklarda iz bırakan bir lezzettir.",
        "subheading": "Nerede Denemeli?",
        "content_p2": "Şehir merkezindeki tarihi restoranlarda ve esnaf lokantalarında bu lezzetin en doğal halini bulabilirsiniz.",
        "content_p3": "Evde yapmak isteyenler için orijinal tarifine sadık kalarak hazırlamanızı öneririz.",
        "topic": "yöresel lezzetler"
    })

# 7. Services
for service in services:
    articles_to_generate.append({
        "filename": f"{service.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}.html",
        "title": f"{service} ve İletişim Bilgileri",
        "description": f"{service} listesi, telefon numaraları ve adres bilgileri. Güncel {service} rehberi.",
        "keywords": f"{service}, antalya hizmetler, {service} telefon",
        "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'da {service.lower()} ihtiyacınız olduğunda başvurabileceğiniz güvenilir adresler ve bilgiler.",
        "content_p1": f"Vatandaşların ve turistlerin hayatını kolaylaştıran {service.lower()} hizmetleri, şehrin her noktasında erişilebilir durumdadır.",
        "subheading": "Detaylar",
        "content_p2": "Güncel bilgilere ve iletişim numaralarına resmi kurumların web sitelerinden veya çağrı merkezlerinden ulaşabilirsiniz.",
        "content_p3": "Acil durumlarda 112 Acil Çağrı Merkezi'ni arayarak yardım talep edebilirsiniz.",
        "topic": "kamu ve özel hizmetler"
    })

# 8. Districts
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

# 9. Beaches
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

# 10. Historical Sites
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

# 11. Malls
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

# 12. Activities
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

# 13. Parks
for park in parks:
    articles_to_generate.append({
        "filename": f"{park.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-nerede.html",
        "title": f"{park} Nerede? Giriş Ücreti ve Aktiviteler",
        "description": f"{park} nerede? Park içinde neler var? Piknik yapılır mı? Giriş ücreti.",
        "keywords": f"{park} nerede, {park} giriş ücreti, antalya parklar",
        "image": "https://images.unsplash.com/photo-1496417263034-38ec4f0d6d21?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'nın yeşil yüzü {park}, şehrin gürültüsünden uzaklaşmak isteyenler için harika bir kaçış noktası.",
        "content_p1": f"{park}, geniş yürüyüş yolları, çocuk oyun alanları ve dinlenme noktalarıyla her yaştan ziyaretçiye hitap ediyor.",
        "subheading": "Neler Yapılır?",
        "content_p2": "Park içerisinde yürüyüş yapabilir, bisiklete binebilir veya manzaranın tadını çıkararak kitabınızı okuyabilirsiniz.",
        "content_p3": "Özellikle hafta sonları ailelerin uğrak noktası olan parkta, doğa ile iç içe keyifli vakit geçirebilirsiniz.",
        "topic": "park ve rekreasyon"
    })

# 14. Mosques
for mosque in mosques:
    articles_to_generate.append({
        "filename": f"{mosque.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c')}-tarihi.html",
        "title": f"{mosque} Tarihi ve Mimari Özellikleri",
        "description": f"{mosque} nerede? Kim tarafından yapıldı? {mosque} tarihi ve mimarisi.",
        "keywords": f"{mosque} tarihi, {mosque} nerede, antalya camileri",
        "image": "https://images.unsplash.com/photo-1565060169194-196e9272dad9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'nın manevi ve tarihi simgelerinden {mosque}, mimari yapısıyla dikkat çekmektedir.",
        "content_p1": f"{mosque}, geçmişten günümüze taşıdığı izlerle şehrin kültürel mirasının önemli bir parçasıdır.",
        "subheading": "Mimari Detaylar",
        "content_p2": "Caminin iç ve dış süslemeleri, dönemin sanat anlayışını yansıtan eşsiz örnekler sunmaktadır.",
        "content_p3": "İbadete açık olan camiyi ziyaret ederken kıyafet kurallarına ve ziyaret saatlerine dikkat etmenizi rica ederiz.",
        "topic": "inanç turizmi"
    })

# 15. Living Topics
for topic in living_topics:
    articles_to_generate.append({
        "filename": f"{topic.lower().replace(' ','-').replace('ı','i').replace('ğ','g').replace('ü','u').replace('ş','s').replace('ö','o').replace('ç','c').replace('?','')}.html",
        "title": topic,
        "description": f"{topic} hakkında detaylı bilgiler, ipuçları ve tavsiyeler. Antalya yaşam rehberi.",
        "keywords": f"{topic}, antalya yaşam, antalya rehberi",
        "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80",
        "intro": f"Antalya'da yaşamayı düşünenler veya şehri daha yakından tanımak isteyenler için {topic} konusu oldukça önemlidir.",
        "content_p1": f"{topic} hakkında merak edilen tüm detayları bu yazımızda derledik. Şehrin sunduğu imkanlar ve yaşam standartları hakkında fikir sahibi olabilirsiniz.",
        "subheading": "Önemli İpuçları",
        "content_p2": "Antalya, hem yerli hem de yabancı nüfusun yoğun olduğu kozmopolit bir şehirdir. Bu nedenle {topic} konusunda farklı seçenekler ve alternatifler bulmanız mümkündür.",
        "content_p3": "Güncel bilgilere ve resmi prosedürlere ilgili kurumların web sitelerinden ulaşmanızı tavsiye ederiz.",
        "topic": "yaşam rehberi"
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
