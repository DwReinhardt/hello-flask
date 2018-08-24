from flask import Flask # imports Flask class from flask module.

#app will be the object created by the constructor Flask. 
# __name__ is a variable controlled by Python that tells code what module it's in
app = Flask(__name__) 

#the DEBUG configuration setting for the Flask application will be enabled.
# This enables some behaviors that are helpful when developing Flask apps, 
# such as displaying errors in the browser, and ensuring file changes are 
# reloaded while the server is running (aka "host swapping")
app.config['DEBUG'] = True

@app.route("/")#decorator creates a mapping between the path 
               # - in this case the root, or "/", and the function 
               # that we're about to define

def index():#a function of zero variables
    return "Hello World"#function returns a string literal

#Pass control to the Flask object. 
# The run function loops forever and never returns, so put it last. 
# It carries out the responsibilities of a web server, listening for requests
# and sending responses over a network connection
app.run()