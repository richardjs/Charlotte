from flask import render_template, request
from charlotte import app
from charlotte.database import add_feed, get_feeds
import feedparser

@app.route('/')
def index():
	r = ''

	feeds = []
	for feed in get_feeds():
		d = feedparser.parse(feed['url'])
		feed['title'] = d.feed['title']
		feed['entries'] = d.entries
		feeds.append(feed)

	return render_template('listing.html', feeds=feeds)

@app.route('/update', methods=['GET', 'POST'])
def update():
	if request.method == 'GET':
		return render_template('update.html')
	elif request.method == 'POST':
		return 'will update...'

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'GET':
		return render_template('add.html')
	elif request.method == 'POST':
		add_feed(request.form['url'])
		return 'Added'
			
