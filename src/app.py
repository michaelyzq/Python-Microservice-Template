'''
Created on Dec 28, 2017

@author: mike
'''
import os
from flask import Flask
from OpenSSL import crypto
import json
app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
       return "hello"



if __name__ == '__main__':   
   import client_action as ca 
   ca.register()
   #app.run(port=7001,debug=True, ssl_context= (p12.get_certificate().to_cryptography().public_bytes(), p12.get_privatekey().to_cryptography_key()))
   #app.run(port=7001,debug=True, ssl_context= (os.getcwd()+"\\resource\\cert.crt", (os.getcwd()+"\\resource\\cert.key" )  ))
   app.run(port=7001,debug=True   )
   print "APP is stated"  
   try:  
       while 1:  
           pass  
   except KeyboardInterrupt:  
       print "shutting down now"
       ca.delete()
       os._exit
    
    
