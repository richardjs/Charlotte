from flask import render_template, request
from charlotte import app
from charlotte import database
from charlotte.feed import update_feed, update_feeds, get_feeds
import feedparser

@app.route('/')
@app.route('/list')
def list():
	feeds = []
	for feed in database.get_feeds():
		if not feed['title']:
			feed['title'] = feed['url'] + ' [needs update]'
		feed['entries'] = database.get_entries(feed['id'])
		feeds.append(feed)
	
	return render_template('list.html', feeds=feeds)

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
		database.add_feed(request.form['url'])
		return 'ok'

@app.route('/rename', methods=['GET', 'POST'])
def rename():
	if request.method == 'GET':
		feeds = get_feeds()
		return render_template('rename.html', feeds=feeds)
	elif request.method == 'POST':
		database.rename_feed(
			request.form['id'], request.form['name']
		)
		return 'ok'
