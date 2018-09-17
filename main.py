from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first name">First Name:</label>
            <input id="first name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/hello", methods=['post'])

def hello():
    first_name = request.form['first_name']
    return "<h1> Hello, " + first_name + "</h1>"



time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>

        <input type="submit" value="Validate" />
"""
#@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',
    minutes='', minutes_error='')

@app.route('/validate-time', methods=['POST'])

def is_integer(num): #determine if string can be converted to int
    try:
        int(num)
        return True
    except ValueError:
        return False

def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''  #keeps invalid values from being passed along

    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hours value out of range (0-23)'
            hours = ''  #keeps invalid values from being passed along

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''  #keeps invalid values from being passed along

    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''  #keeps invalid values from being passed along

    if not minutes_error and not hours_error:
        return "success!"
    else:
        time_form.format(hours_error=hours_error, minutes_error=minutes_error, 
        hours=hours, minutes=minutes )

app.run()