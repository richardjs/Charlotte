from charlotte.database import (
	get_feeds, get_feed, add_feed_title,
	have_entry, add_entry
)
import feedparser

def update_feed(id=None, feed=None):
	assert id is not None or feed is not None
	if id is not None:
		feed = get_feed(id)
	else:
		id = feed['id']

	d = feedparser.parse(feed['url'])

	if not feed['title']:
		add_feed_title(id, d.feed.title)
		
	for entry in d.entries:
		if not have_entry(entry.id):
			add_entry(feed['id'], entry.id, entry.link, entry.title)

def update_feeds():
	for feed in get_feeds():
		update_feed(feed=feed)
