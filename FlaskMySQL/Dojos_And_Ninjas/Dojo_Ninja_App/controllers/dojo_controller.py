from flask import render_template, request, redirect
from Dojo_Ninja_App.models.dojo_model import Dojo
from Dojo_Ninja_App.models.ninja_model import Ninja
from Dojo_Ninja_App import app

#* ============ HOME VIEW =============

@app.route('/')
def index():
  currDojos = Dojo.get_all_dojos()
  return render_template("dojos.html", currDojos=currDojos)


@app.route('/new/dojo', methods=["POST"])
def newDojo():
  newDojo = {**request.form}
  Dojo.create_new(newDojo)
  return redirect('/')


#* ============ DOJO SHOW =============

@app.route('/dojo/show/<int:id>')
def showDojo(id):
  
  currId = { "id" : id }
  ninjasFromDojo = Dojo.get_all_ninjas_from_dojo(currId)
  
  #* print("NINJAS FROM DOJO QUERY!!!!  =======> ",ninjasFromDojo)
  
  return render_template("dojoShow.html", ninjasFromDojo=ninjasFromDojo)

#* ============ NEW NINJA =============

@app.route('/new/ninja')
def newNinja():
  currDojos = Dojo.get_all_dojos()
  return render_template("newNinja.html", currDojos=currDojos)

@app.route('/new/ninja/data', methods=["POST"])
def ninjaData():
  new_ninja_data = {**request.form}
  Ninja.create_new(new_ninja_data)
  print("My data =========>>>> ", new_ninja_data)
  return redirect(f'/dojo/show/{new_ninja_data["dojo_id"]}')



