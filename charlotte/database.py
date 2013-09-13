from flask import g
from charlotte import app
from os.path import join
import sqlite3

DATABASE = join(app.instance_path, 'dataT.db')

def dict_factory(cursor, row):
	return dict(
		(cursor.description[idx][0], value)
		for idx, value in enumerate(row)
	)

def get_db():
	db = getattr(g, 'database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	db.row_factory = dict_factory
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

def get_feeds():
	db = get_db()
	cursor = db.cursor()
	cursor.execute('select * from feeds')
	return cursor.fetchall()

def get_feed(id):
	db = get_db()
	cursor = db.cursor()
	cursor.execute('select * from feeds where id=?', (id,))
	return cursor.fetchone()

def add_feed(url):
	db = get_db()
	db.cursor().execute(
		'insert into feeds(url) values(?)', (url,)
	)
	db.commit()

def add_feed_title(id, title):
	db = get_db()
	db.cursor().execute(
		'update feeds set title=? where id=?', (title, id)
	)
	db.commit()

def rename_feed(id, title):
	db = get_db()
	db.cursor().execute(
		'update feeds set displayname=? where id=?',
		(title, id)
	)
	db.commit()

def get_entries(feedid):
	db = get_db()
	cursor = db.cursor()
	cursor.execute(
		'select * from entries where feedid=?', (feedid,)
	)
	return cursor.fetchall()

def have_entry(url, title):
	db = get_db()
	cursor = db.cursor()
	cursor.execute(
		'select * from entries where url=? and title=?',
		(url, title)
	)
	if cursor.fetchone() is None:
		return False
	return True

def add_entry(feedid, url, title):
	db = get_db()
	db.cursor().execute(
		'insert into entries(feedid, url, title) values(?, ?, ?)',
		(feedid, url, title)
	)
	db.commit()
