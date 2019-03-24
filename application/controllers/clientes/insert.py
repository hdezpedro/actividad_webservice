import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

  

    def GET(self):
        return config.render.insert() 

    def POST(self):
        form = config.web.input() 
        config.model.insert_clientes(
            form['nombre'],form['apellido_paterno'],form['apellido_materno'],form['telefono'],form['email'],
        )
        raise config.web.seeother('/clientes') 
