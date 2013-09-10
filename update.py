from charlotte import app, feed
with app.app_context():
	feed.update_feeds()
