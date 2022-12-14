from flask_app import app
from flask_app.controllers.user_controller import hello

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')