from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'random string'

translations = [
    ["tur","anasayfa","kurumsal",
    "DTM Elektroteknik A.Ş. 2000 yılından bu yana tecrübeli kadrosu ile 25A'den 6300A'e kadar busbar üretimi ile hizmet vermektedir. Misyonumuz sahip olduğumuz belge ve sertifika standartlarında müşteri memnuniyetini sağlamak, yurt içi ve dışında busbar sistemlerini en iyi şekilde üretmek ve busbar sistemlerinde güvenilir ve kaliteli hizmet sunmaktır."
    ,"ürünler","25A - 6300A arası, yüksek kaliteli ve standartlara uygun üretilen Busbar Kanal Sistemleri hakkında bilgi almak için bu bölümü ziyaret ediniz."
    ,"AYDINLATMA","ALÇAK","ORTA","YÜKSEK","hizmetler","Satış öncesi ve satış sonrası hizmetleri mükemmel bir düzeyde vermek, DTM Elektroteknik A.Ş. için çok önemlidir. Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat soluta impedit, optio similique esse nemo provident temporibus officia sed illum tenetur labore, nobis quasi explicabo, cupiditate velit veniam sint veritatis!"
    ,"Alüminyum Kasa","",""
    ],
    ["eng","homepage","corporate",
    "DTM Electrotechnical Inc. has been providing service with busbar production from 25A to 6300A with its experienced staff since 2000. Our mission is to ensure customer satisfaction in the document and certificate standards we have, to produce busbar systems in the best way in Turkey and abroad, and to to provide reliable and quality service in their systems."
    ,"products"," Please visit this section for information about Busbar Systems between 25A - 6300A, produced in accordance with standards and high quality"
    ,"lIGHTNING","LOW","MEDIUM","HIGH","SERVICES","Satış öncesi ve satış sonrası hizmetleri mükemmel bir düzeyde vermek, DTM Elektroteknik A.Ş. için çok önemlidir. Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat soluta impedit, optio similique esse nemo provident temporibus officia sed illum tenetur labore, nobis quasi explicabo, cupiditate velit veniam sint veritatis!"
    ,"Aluminum Case","",""
    ]
]

# 0: Tur, 1: Eng
@app.route('/set_lang', methods = ['POST'])
def set_lang():
    if request.method == 'POST':
        session["language"] = int(request.form['langval']) # make eng -> eng returns a '1'
    return redirect(url_for('root'))

def get_lang():
    try:
        if 'language' not in session:  # if session does not contain a language variable, if it exists no need to manually re-add it on else.
            session["language"] = 1
        
        # hideous code - refactor
        if session['language'] == 0:
            return 0
        elif session['language'] == 1:
            return 1
        else:
            return 1 # failsafe for other languages, if need be.
    except Exception as e:
        print(e)

@app.route('/send_mail', methods = ['POST'])
def send_mail():
    try:
        if request.method == 'POST':
            your_message = request.form['yourmsg']
            # try açıp mail at burada
        return redirect(url_for('page_iletisim', stt = "Success!", bg = "#00FF00")) # BUNLAR KALMAYACAK - MAILER POST YAP
    except Exception as e:
        return redirect(url_for('page_iletisim', stt = e, bg = "#FF3300")) # BUNLAR KALMAYACAK - MAILER POST YAP

@app.route("/")
def root():
    lang_id = get_lang()
    return render_template('mainpage.html', translation = translations[lang_id])
    
@app.route("/kurumsal")
def page_kurumsal():
    lang_id = get_lang()
    return render_template('kurumsal.html', translation = translations[lang_id])

@app.route("/products")
def page_products():
    lang_id = get_lang()
    return render_template('products.html', translation = translations[lang_id])

@app.route("/hizmetler")
def page_hizmetler():
    lang_id = get_lang()
    return render_template('hizmetler.html', translation = translations[lang_id])

@app.route("/referanslar")
def page_referanslar():
    lang_id = get_lang()
    return render_template('referanslar.html', translation = translations[lang_id])

@app.route("/iletisim")
def page_iletisim():
    lang_id = get_lang()
    return render_template('iletisim.html', translation = translations[lang_id])

@app.route("/sertifikalar")
def page_sertifikalar():
    lang_id = get_lang()
    return render_template('sertifikalar.html', translation = translations[lang_id])

@app.route("/haberler")
def page_haberler():
    lang_id = get_lang()
    return render_template('haberler.html', translation = translations[lang_id])


  
if __name__ == "__main__":
    app.run()