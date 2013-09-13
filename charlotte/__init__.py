import os

from flask import Flask

app = Flask('charlotte')

if not os.path.exists(app.instance_path):
	os.mkdir(app.instance_path)

import charlotte.views
