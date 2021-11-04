from flask import Flask

our_app = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    our_app.run(debug = True)