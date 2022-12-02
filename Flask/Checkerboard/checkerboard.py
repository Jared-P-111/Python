from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<int:rowLength>/<int:rowHeight>/<color1>/<color2>')
def index(rowLength, rowHeight, color1, color2):
  return render_template("index.html", rowLength=rowLength, color1=color1, color2=color2, rowHeight=rowHeight)


if __name__ == "__main__":
  app.run(debug=True)


