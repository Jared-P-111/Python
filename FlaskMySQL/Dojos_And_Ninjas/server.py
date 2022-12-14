import sys
sys.dont_write_bytecode = True

from  Dojo_Ninja_App import app

from  Dojo_Ninja_App.controllers import dojo_controller

#* ============== RUN APP ================

if __name__ == "__main__":   
    app.run(debug=True, host='0.0.0.0') 