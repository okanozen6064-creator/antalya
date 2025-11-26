import os

articles = [
    {
        "title": "Antalya Kaleiçi: Tarihin Kalbi",
        "filename": "kaleici-tarihin-kalbi.html",
        "content": "Antalya'nın kalbi Kaleiçi, dar sokakları, tarihi evleri ve antik limanı ile ziyaretçilerini büyülüyor. Hadrian Kapısı'ndan girip tarihe yolculuk yapın.",
        "image": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Düden Şelalesi: Doğanın Mucizesi",
        "filename": "duden-selalesi.html",
        "content": "Antalya'nın serinletici güzelliği Düden Şelalesi, hem yukarı hem de aşağı şelale olarak iki kısımdan oluşur. Denize dökülen suların manzarası görülmeye değer.",
        "image": "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Konyaaltı Plajı: Mavi Bayraklı Güzellik",
        "filename": "konyaalti-plaji.html",
        "content": "Dünyaca ünlü Konyaaltı Plajı, tertemiz denizi ve dağ manzarası ile deniz severlerin vazgeçilmezi. Sabah yürüyüşleri için de ideal bir kordon boyuna sahip.",
        "image": "https://images.unsplash.com/photo-1566438480900-0609be27a4be?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Lara Plajı ve Kum Heykeller",
        "filename": "lara-plaji.html",
        "content": "Altın sarısı kumlarıyla ünlü Lara Plajı, aynı zamanda her yıl düzenlenen Uluslararası Kum Heykel Festivali'ne ev sahipliği yapıyor.",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Antalya Müzesi: Tarihe Işık Tutan Eserler",
        "filename": "antalya-muzesi.html",
        "content": "Türkiye'nin en büyük müzelerinden biri olan Antalya Müzesi, bölgedeki antik kentlerden çıkarılan eşsiz heykellere ve lahitlere ev sahipliği yapıyor.",
        "image": "https://images.unsplash.com/photo-1599576838663-8334b7f5f6f6?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Aspendos Antik Tiyatrosu",
        "filename": "aspendos.html",
        "content": "Akustiği ile ünlü Aspendos Antik Tiyatrosu, günümüzde hala konserlere ve etkinliklere ev sahipliği yapmaktadır. Roma döneminin en iyi korunmuş tiyatrosudur.",
        "image": "https://images.unsplash.com/photo-1528659588554-325f161b9627?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Termessos: Dağların Zirvesindeki Kent",
        "filename": "termessos.html",
        "content": "Güllük Dağı'nın tepesinde yer alan Termessos, Büyük İskender'in bile alamadığı şehir olarak bilinir. Vahşi doğa ile tarihin iç içe geçtiği bir yer.",
        "image": "https://images.unsplash.com/photo-1623164344502-31593305f38e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Antalya Usulü Piyaz: Tadına Doyum Olmaz",
        "filename": "antalya-piyazi.html",
        "content": "Tahinli sosuyla diğer piyazlardan ayrılan Antalya Piyazı, köftenin en iyi eşlikçisidir. Bu lezzeti denemeden Antalya'dan dönmeyin.",
        "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Antalya'da Ne Yenir? Yöresel Lezzetler",
        "filename": "antalya-yemekleri.html",
        "content": "Şiş köfte, hibeş, kabak tatlısı ve yanık dondurma... Antalya mutfağı, Akdeniz lezzetlerini kendine has yorumuyla sunuyor.",
        "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Olympos ve Çıralı: Doğal Cennet",
        "filename": "olympos-cirali.html",
        "content": "Caretta Caretta'ların yumurtlama alanı olan Çıralı ve sönmeyen ateşiyle Yanartaş, doğa severler için eşsiz bir kaçış noktası.",
        "image": "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Antalya'da Ulaşım Rehberi",
        "filename": "antalya-ulasim.html",
        "content": "Antray, otobüsler ve deniz otobüsü... Antalya'da şehir içi ulaşım hakkında bilmeniz gereken her şey bu rehberde.",
        "image": "https://images.unsplash.com/photo-1562620409-77e8c1c4e361?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Antalya Hava Durumu: Ne Zaman Gidilir?",
        "filename": "antalya-hava-durumu.html",
        "content": "Yılın 300 günü güneşli olan Antalya'da tatil sezonu hiç bitmez. Ancak en ideal zamanlar ilkbahar ve sonbahar aylarıdır.",
        "image": "https://images.unsplash.com/photo-1561571994-3c61c5541711?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Antalya Gece Hayatı",
        "filename": "antalya-gece-hayati.html",
        "content": "Kaleiçi barlar sokağından lüks otellerin diskolarına kadar Antalya'da gece hayatı oldukça renklidir. Eğlencenin kalbi burada atar.",
        "image": "https://images.unsplash.com/photo-1566737236500-c8ac43014a67?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Antalya'da Alışveriş: Nereden Ne Alınır?",
        "filename": "antalya-alisveris.html",
        "content": "Tarihi çarşılardan modern AVM'lere, Antalya alışveriş tutkunları için pek çok seçenek sunuyor. Yöresel reçeller ve hediyelik eşyalar favori.",
        "image": "https://images.unsplash.com/photo-1483985988355-763728e1935b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Perge Antik Kenti",
        "filename": "perge.html",
        "content": "Helenistik dönemin en zengin ve güzel şehirlerinden biri olan Perge, stadyumu ve sütunlu caddesi ile ziyaretçilerini büyülüyor.",
        "image": "https://images.unsplash.com/photo-1540202404-a671b57d5c9c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
    }
]

template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Antalya Hakkında</title>
    <meta name="description" content="{content}">
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
                            <p class="mb-4">{content}</p>
                            <p class="mb-4">Antalya'nın bu eşsiz güzelliği, her yıl milyonlarca turisti ağırlamaktadır. {title}, hem yerli hem de yabancı turistlerin ilgisini çeken önemli bir destinasyondur.</p>
                            <p class="mb-4">Ziyaretiniz sırasında çevredeki diğer tarihi ve doğal güzellikleri de keşfetmeyi unutmayın. Antalya, her köşesinde ayrı bir sürpriz barındıran büyülü bir şehirdir.</p>
                            
                            <!-- In-Article Ad -->
                            <div class="w-full h-[250px] bg-gray-100 flex items-center justify-center my-8 border border-gray-200">
                                <span class="text-gray-400 font-semibold">YAZI İÇİ REKLAM</span>
                            </div>

                            <p>Daha fazla bilgi ve detaylı rehberlik hizmetleri için yerel uzmanlara danışabilirsiniz.</p>
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
                        <h3 class="text-xl font-bold mb-4">Antalya'da Usta mı Arıyorsunuz?</h3>
                        <p class="mb-6 text-blue-100">Elektrik, tesisat, boya ve daha fazlası için en iyi ustalar bir tık uzağınızda.</p>
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

for article in articles:
    file_path = os.path.join("articles", article["filename"])
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(template.format(**article))

print(f"Generated {len(articles)} articles.")
