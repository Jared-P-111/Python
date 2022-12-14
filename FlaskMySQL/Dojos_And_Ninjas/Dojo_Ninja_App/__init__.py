from flask import Flask

app = Flask(__name__)

DATABASE = "dojo_ninjas_schema"

app.secret_key = 'stealthKey'
