# İçe aktar
from flask import Flask, render_template,request, redirect
# Veri tabanı kitaplığını bağlama
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET','POST']) 
def anasayfa():
	if request.method == 'POST':
			cards = request.form['cards']
			return render_template('index.html', cards=cards)
	else: 
		return render_template('index.html')
	
app.run(debug=True)
