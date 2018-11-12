from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.config.from_pyfile('../instance/config.py')


from .views import *
