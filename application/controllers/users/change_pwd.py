"""
    Class for change the password
"""
from . import config
import hashlib
import app


class Change_pwd:
    def __init__(self):
        pass

    def GET(self, **k):
        if app.session.loggedin is True: {
            session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: 
                return self.GET_CHANGE_PWD(session_username) 
            elif session_privilege == 1: 
                return self.GET_CHANGE_PWD(session_username) 
        else:
            raise config.web.seeother('/login') 

    def POST(self, **k):
        if app.session.loggedin is True: 
            session_username = app.session.username 
            session_privilege = app.session.privilege 
            if session_privilege == 0: 
                return self.POST_CHANGE_PWD(session_username)
            elif session_privilege == 1: 
                return self.POST_CHANGE_PWD(session_username)
        else: 
            raise config.web.seeother('/login')

    @staticmethod
    def GET_CHANGE_PWD(username, **k):
        message = None # Error message
        result = config.model.get_users(username) # search for username data
        result.username = config.make_secure_val(str(result.username)) # apply HMAC for username
        return config.render.change_pwd(result, message) # render chage_pwd.html

    @staticmethod
    def POST_CHANGE_PWD(username, **k):
        message = None # Error message
        form = config.web.input() # get form data
        password = hashlib.md5(form.password + config.secret_key).hexdigest() # encrypt password
        password2 = hashlib.md5(form.password2 + config.secret_key).hexdigest() # encrypt password2

        if password == password2: # compare password with password2
            result = config.model.update_password(
                username,
                password,
                0
            )
            if result == None:
                message = "Error on change password" # Error message
                result = config.model.get_users(username) # search for username data
                result.username = config.make_secure_val(str(result.username)) # apply HMAC for username
                return config.render.change_pwd(result, message) # render chage_pwd.html
            else:
                raise config.web.seeother('/users')
        else:
            message = "Password confirm is not the same" # Error message
            result = config.model.get_users(username) # search for username data
            result.username = config.make_secure_val(str(result.username)) # apply HMAC for username
            return config.render.change_pwd(result, message) # render chage_pwd.html
