import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    
    def GET(self, id_cliente, **k):
        message = None 
        id_cliente = config.check_secure_val(str(id_cliente)) 
        result = config.model.get_clientes(int(id_cliente)) 
        result.id_cliente = config.make_secure_val(str(result.id_cliente)) 
        return config.render.edit(result, message) 

    def POST(self, id_cliente, **k):
        form = config.web.input()  
        form['id_cliente'] = config.check_secure_val(str(form['id_cliente'])) 
        
        result = config.model.edit_clientes(
            form['id_cliente'],form['nombre'],form['apellido_paterno'],form['apellido_materno'],form['telefono'],form['email'],
        )
        if result == None: 
            id_cliente = config.check_secure_val(str(id_cliente)) 
            result = config.model.get_clientes(int(id_cliente)) 
            result.id_cliente = config.make_secure_val(str(result.id_cliente)) 
            message = "Error al editar el registro" 
            return config.render.edit(result, message) 
        else: 
            raise config.web.seeother('/clientes') 
