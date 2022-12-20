from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User
from flask_app.models.recipes_model import Recipe
from flask_app import app

import sys
sys.dont_write_bytecode = True

#🧈 ========== SHOW RECIPE ============
@app.route('/show/recipe/<int:id>')
def showRecipe(id):
  currRecipe = Recipe.get_one_recipe({"id": id})
  currUser = User.get_user_by_id({"id": id})
  return render_template("showRecipe.html", currRecipe=currRecipe, currUser=currUser)

#🧈 ========== RECIPES ===============
@app.route('/recipes')
def recipes():
  userId = {"id": session["uid"]}
  currUser = User.get_user_by_id(userId)
  usersAndRecipes = Recipe.get_all_users_and_recipes()
  
  return render_template("recipes.html", currUser=currUser, usersAndRecipes=usersAndRecipes)

#🧈=========== NEW RECIPE ==================
@app.route('/new/recipe')
def newRecipe():
  return render_template("newRecipe.html")

#🧈 ============ NEW RECIPE DATA ============
@app.route('/new/recipe/data', methods=["POST"])
def newRecipeData():
  currRecipe = {**request.form}
  currRecipe["posted_by_user_id"] = session["uid"]
  
  if currRecipe["cook_time"] == "over_30_min":
    currRecipe["under_30_min"] = False

  if currRecipe["cook_time"] == "under_30_min":
    currRecipe["under_30_min"] = True
  
  currRecipe = Recipe.create_recipe(currRecipe)
  
  return redirect('/recipes')

