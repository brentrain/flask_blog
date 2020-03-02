from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return url_for('about')

@app.route('/blog')
def blog():
	return render_template('blog.html')

@app.route('/work')
def work():
	return render_template('work.html')


if __name__ == "__main__":
	app.run(debug=True)