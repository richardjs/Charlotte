from charlotte import app
from charlotte.database import init_db
from os import mkdir
from os.path import exists

if not exists('instance'):
	mkdir('instance')

with app.app_context():
	init_db()
