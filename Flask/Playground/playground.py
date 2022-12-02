from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("/index.html", times=3)

@app.route('/<color>/<int:num>')
def displayBoxes(num, color):
  return render_template("/index.html", times=num, color=color)

if __name__ == "__main__":
  app.run(debug=True)