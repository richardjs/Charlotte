from charlotte import database
import feedparser

def update_feed(id=None, feed=None):
	assert id is not None or feed is not None
	if id is not None:
		feed = database.get_feed(id)
	else:
		id = feed['id']

	d = feedparser.parse(feed['url'])

	if not feed['title']:
		database.add_feed_title(id, d.feed.title)
	
	for entry in d.entries:
		if not database.have_entry(entry.link, entry.title):
			database.add_entry(feed['id'], entry.link, entry.title)

def update_feeds():
	for feed in database.get_feeds():
		update_feed(feed=feed)
