from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("/index.html", times=3)

@app.route('/<color>')
@app.route('/<color>/<int:num>')
def displayBoxes(num = 3, color="crimson"):
  return render_template("/index.html", times=num, color=color)

if __name__ == "__main__":
  app.run(debug=True)