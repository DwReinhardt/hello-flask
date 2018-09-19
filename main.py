from flask import Flask, request, redirect
import cgi
import os
import jinja2

# include the following lines when using templates
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True) 

app = Flask(__name__)
app.config['DEBUG'] = True
# up

form = """

"""

@app.route("/")
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render()

@app.route("/hello", methods=['post'])

def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(first_name=first_name) # escaped html, prevents hacking


time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value="{hours}" />
        </label>
        <p class="error">{hours_error}</p>
        
        <label>Minutes
            <input name="minutes" type="text" value="{minutes}" />
        </label>
        <p class="error">{minutes_error}</p>

        <input type="submit" value="Validate" />
"""

@app.route("/validate-time")
def display_time_form():
    return time_form.format(hours='', hours_error='',
    minutes='', minutes_error='')

def is_integer(num): #determine if string can be converted to int
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/validate-time", methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

# Error checking for Hours
    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''  #keeps invalid values from being passed along
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hours value out of range (0-23)'
            hours = ''  #keeps invalid values from being passed along

# Error checking for Minutes
    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''  #keeps invalid values from being passed along
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''  #keeps invalid values from being passed along

# Clears all errors
    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))

    else:
        return time_form.format(hours_error=hours_error, minutes_error=minutes_error, 
        hours=hours, minutes=minutes )

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)

app.run()