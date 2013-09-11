from flask import render_template, request
from charlotte import app
from charlotte.database import add_feed, get_feeds, get_entries
from charlotte.feed import update_feed, update_feeds
import feedparser

@app.route('/')
def index():
	feeds = []
	for feed in get_feeds():
		if not feed['title']:
			feed['title'] = feed['url'] + ' [needs update]'
		feed['entries'] = get_entries(feed['id'])
		feeds.append(feed)
	
	return render_template('listing.html', feeds=feeds)

@app.route('/update', methods=['GET', 'POST'])
def do_update_feeds():
	if request.method == 'GET':
		return render_template('update.html')
	elif request.method == 'POST':
		update_feeds()
		return 'ok'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def do_update_feed(id):
	if request.method == 'GET':
		return render_template('update.html')
	elif request.method == 'POST':
		update_feed(id)
		return 'ok'

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'GET':
		return render_template('add.html')
	elif request.method == 'POST':
		add_feed(request.form['url'])
		return 'ok'
