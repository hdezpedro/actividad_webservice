import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, id_cliente):
        id_cliente = config.check_secure_val(str(id_cliente)) 
        result = config.model.get_clientes(id_cliente) 
        return config.render.view(result) 
