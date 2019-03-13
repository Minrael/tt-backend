#! /usr/bin/python3

from app import app, db
from flask_script import Manager
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand )

@manager.command
def hello():
  print("Hello, Maria!")

if __name__ =="__main__":
  app.run(debug=False)
  #manager.run()

