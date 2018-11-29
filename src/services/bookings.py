from services import root_dir, nice_json
from flask import current_app
from werkzeug.exceptions import NotFound



# class
# @app.route("/hello", methods=['GET'])
# def hello():
#    return "hello"

class ControllerClass:
    '''
    classdocs
    '''
    def __init__(self,app):
        '''
        Constructor
        '''
        self.app=app
    @app.route("/hello", methods=['GET'])
    def hello(self):
       return "hello"
  
