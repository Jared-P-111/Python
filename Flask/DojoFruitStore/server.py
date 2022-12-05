from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  

app.secret_key = 'stealthKey'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session["strawberry"] = request.form["strawberry"]
    session["raspberry"] = request.form["raspberry"]
    session["apple"] = request.form["apple"]
    
    # print(f"Charging {session['name']}")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    