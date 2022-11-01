from flask import Flask, render_template, session, request, redirect, url_for
from flask_mail import Mail, Message
app = Flask(__name__)

app.secret_key = 'random string'

app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = 465 #default 25, 465 is SSL friendly
app.config['MAIL_USE_SSL']= True
app.config['MAIL_USERNAME']= 'batuhan.sahin@dtmbusbar.com' #mail adress 
app.config['MAIL_PASSWORD']= 'DTM1907.,' #mail password 

mail = Mail(app)

def sendContactForm(hermes):
    msg = Message("Contact Form from Testing",sender="batuhan.sahin@dtmbusbar.com",recipients=["batuhannsahinn@hotmail.com"])

    msg.body = """ 
    Merhaba,
    You just received a contact form.

    Name:{}
    Email:{}
    Message:{}

    Saygılar,
    Websitesi

    
    """.format(hermes['name'],hermes['email'],hermes['message'])

    mail.send(msg)

@app.route("/iletisim",methods=["GET","POST"])
def contact():

    if request.method == 'POST':
        hermes = {}

        hermes ['name'] = request.form['name']
        hermes ['email'] = request.form['email'].replace(' ', '').lower()
        hermes ['message'] = request.form['message']

        sendContactForm(hermes)

        return render_template('iletisim.html')


    return render_template('iletisim.html')







translations = [
    ["tr","Ana Sayfa","Kurumsal","Hakkımızda","Ürünler","Ürünlerimiz","AYDINLATMA","ALÇAK GÜÇ","ORTA GÜÇ","YÜKSEK GÜÇ"
    ,"İletişim","Kullanım Alanları","Hizmetler","Referanslar","Sertifikalar","Haberler","Hızlı Navigasyon","DTM Elektroteknik A.Ş.","Adınız","Mesajınız"
    ,"BÖLGE BAYİ","Adres","Devamını gör..","Adınızı Giriniz","Mesajınızı buraya yazabilirsiniz...","Gönder","Proje Referanslarımızdan Örnekler","","",""],
    ["eng","Homepage","Corporate","About Us","Products","Our Products","LIGHTNING","LOW POWER","MEDIUM POWER","HIGH POWER"
    ,"Contact Us","Application Areas","Services","References","Certificates","News","Fast Navigation","DTM Electrotechnical Inc.","Name","Message"
    ,"REGIONAL DEALER","Adress","Read more..","John Doe","You can write your message here...","Send","Some of our project references","","",""]
]
# 0: Tr, 1: Eng
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