import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    
    def GET(self):
        result = config.model.get_all_clientes().list() # get clientes table list
        for row in result:
            row.id_cliente = config.make_secure_val(str(row.id_cliente)) 
        return config.render.index(result) # render clientes index.html
