#For running the app locally
#Hosting handles flask_app.py is used by hosting solution to run it using the app configured there.

from os import getenv
from flask_app import app

app.run(debug=(getenv('DEBUG')=='True'))