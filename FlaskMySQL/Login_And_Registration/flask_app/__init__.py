import sys
sys.dont_write_bytecode = True

from flask import Flask

app = Flask(__name__)

DATABASE = "login_and_registration"

app.secret_key = "secret_key"