from flask import Flask
<<<<<<< HEAD
from flask import render_template
=======
from flask import send_file
>>>>>>> 2fb96b3b302332add0878ec24fef9248548c23fc
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)

@app.route('/')
<<<<<<< HEAD
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


=======
def show_root():
	#show the root
	return 'Welcome To the Root!'

@app.route('/test/')
def show_test_page():
	#show the test page
	return '<a href="http://www.aftonbladet.se" target="_blank">aftonbladet</a>'

@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
       filename = 'ok.jpg'
    else:
       filename = 'error.jpg'
    return send_file(filename, mimetype='image/gif')
>>>>>>> 2fb96b3b302332add0878ec24fef9248548c23fc

if __name__ == '__main__':
	app.run()
