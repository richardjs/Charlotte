from flask import g
from charlotte import app
import sqlite3

DATABASE = '/tmp/dataT.db'

def get_db():
	db = getattr(g, 'database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, 'database', None)
	if db is not None:
		db.close()

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

def add_feed(feed):
	db = get_db()
	db.cursor().execute(
		'insert into feeds(url) values(?)', (feed,)
	)
	db.commit()

def get_feeds():
	db = get_db()
	cursor = db.cursor()
	cursor.execute('select url from feeds')
	for row in cursor:
		yield {
			'url': row[0]
		}
