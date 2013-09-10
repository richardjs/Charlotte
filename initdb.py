from charlotte import app
from charlotte.database import init_db

with app.app_context():
	init_db()
