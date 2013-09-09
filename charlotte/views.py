from flask import render_template, request
from charlotte import app
from charlotte.database import add_feed, get_feeds
import feedparser

@app.route('/')
def index():
	r = ''

	for feed in get_feeds():
		d = feedparser.parse(feed['url'])
		r += '<p>%s</p>' % d.feed.title
		for entry in d.entries:
			r += '<li><a href="%s">%s</a></li>' % (entry.link, entry.title)
		r += '</ul>'

	return r
	return render_template('listing.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'GET':
		return render_template('add.html')
	elif request.method == 'POST':
		add_feed(request.form['url'])
		return 'Added'
			
