from flask import render_template
from flask import Flask
 
app = Flask(__name__)

@app.route('/')
def site_index():
	return render_template('home_index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__  == ('__main__'):
	app.run()
