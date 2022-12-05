from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'stealthKey'

#-------------------------------- Home Route
@app.route('/')
def index():
  return redirect('/dashboard')

#-------------------------------- Clear Session
@app.route('/clear')
def clear():
  session.clear()
  return redirect('/order')

#-------------------------------- Order
@app.route('/order')
def order():
  return redirect('/dashboard')
#-------------------------------- Dashboard
@app.route('/dashboard')
def  dashboard():
  return render_template('dashboard.html')

#-------------------------------- Thanks
@app.route('/thanks')
def thanks():
  #edge case for if session does not have a "name" key
  if not 'name' in session:
    return redirect('/order')
  
  if not 'qty' in session:
    return redirect('./order')
  
  #HERE WE CAN ACCESS THE SESSION DATA DIRECTLY
  print("Session product: ", session['product'])
  
  return render_template("thanks_order.html")

#--------------------------------- Products 

@app.route('/order/<product>')
def place_order(product):
  return render_template("form.html", product=product)

@app.route('/accept_order', methods=['POST'])
def accept_order():
  
  #This request.form gives us the information of the form data. 
  #We treat this like an object/dictionary
  session["name"] = request.form['name']
  session["qty"] = request.form['qty']
  session["product"] = request.form['product']
  
  return redirect("/thanks")

if __name__ == "__main__":
  app.run(debug=True)