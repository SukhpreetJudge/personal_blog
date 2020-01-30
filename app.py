from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{
		'author' : 'Sonny',
		'post_title' : 'How to master coding',
		'post_body' : 'Today I will teach you',
		'date_posted' : 'Jan 30th 2020'
	},
	{
		'author' : 'Pajeet',
		'post_title' : 'Where are the best jobs',
		'post_body' : 'West coast',
		'date_posted' : 'Jan 31st 2020'
	}
]


@app.route("/")
@app.route("/home")
def homepage():
	return render_template('home.html', posts = posts, title = 'Sonny\'s')


@app.route("/about")
def aboutPage():
	return render_template('about.html', title = 'H')


if __name__ == '__main__':
	app.run(debug = True)
