import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass


    def GET(self, id_cliente, **k):
        message = None
        id_cliente = config.check_secure_val(str(id_cliente))
        result = config.model.get_clientes(int(id_cliente)) 
        result.id_cliente = config.make_secure_val(str(result.id_cliente))
        return config.render.delete(result, message) 

    def POST(self, id_cliente, **k):
        form = config.web.input() 
        form['id_cliente'] = config.check_secure_val(str(form['id_cliente']))
        result = config.model.delete_clientes(form['id_cliente']) 
        if result is None: 
            message = "El registro no se puede borrar"
            id_cliente = config.check_secure_val(str(id_cliente)) 
            id_cliente = config.check_secure_val(str(id_cliente))  
            result = config.model.get_clientes(int(id_cliente)) 
            result.id_cliente = config.make_secure_val(str(result.id_cliente)) 
            return config.render.delete(result, message) 
        else:
            raise config.web.seeother('/clientes') 
