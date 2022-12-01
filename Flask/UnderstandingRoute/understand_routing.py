from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/dojo')
def dojo():
  return 'dojo!'

@app.route('/hello/<name>')
def hello(name):
  print(name)
  return "Hello, " + name

@app.route('/multi/<name>/<age>/<location>')
def nameAgeLocation(name, age, location):
  print(name, age, location)
  return f"Hello {name} I can see your {age} years old, and you live in {location}"

if __name__ == "__main__":
  app.run(debug=True)

