from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('mainpage.html')
    
@app.route("/kurumsal")
def page_kurumsal():
    return render_template('kurumsal.html')

@app.route("/products")
def page_products():
    return render_template('products.html')

@app.route("/hizmetler")
def page_hizmetler():
    return render_template('hizmetler.html')

@app.route("/referanslar")
def page_referanslar():
    return render_template('referanslar.html')

@app.route("/iletisim")
def page_iletisim():
    return render_template('iletisim.html')

@app.route("/haberler")
def page_haberler():
    return render_template('haberler.html')



if __name__ == "__main__":
    app.run()