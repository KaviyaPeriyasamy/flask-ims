from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('base.html')
@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')
@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')
@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/product', methods=['GET','POST'])
def product():
    return render_template('product.html')
@app.route('/product_movement', methods=['GET','POST'])
def product_movement():
    return render_template('product_movement.html')
@app.route('/location', methods=['GET','POST'])
def location():
    return render_template('location.html')
@app.route('/report', methods=['GET','POST'])
def report():
    return render_template('report.html')
@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))
if __name__ == '__main__':
    app.debug = True
    app.run()