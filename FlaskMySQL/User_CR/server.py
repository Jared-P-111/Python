from flask_app import app

from flask_app.controllers import user_controller

#* ============== RUN APP ================

if __name__=="__main__":   
    app.run(debug=True) 
