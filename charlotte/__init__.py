import os

from flask import Flask

from charlotte.middleware import ReverseProxied

app = Flask('charlotte')

app.wsgi_app = ReverseProxied(app.wsgi_app)

app.config.from_object('charlotte.default_settings')
if 'CHARLOTTE_SETTINGS' in os.environ:
	app.config.from_envvar('CHARLOTTE_SETTINGS')

if not os.path.exists(app.instance_path):
	os.mkdir(app.instance_path)

import charlotte.views
