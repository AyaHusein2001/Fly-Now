import flask
from components.user import User
from components.flight import Flight
app = flask.Flask('notes')



def get_html(page_name):
    html_file=open(page_name+'.html')
    content=html_file.read()
    html_file.close()
    return content

def get_flights():
    all_flights = Flight.get_all_flights('components/flights.csv')
    actual_flights=''
    for flight in all_flights:
        actual_flights+='<div class="flight-card">'+'<p> airplane name <span>'+ flight['airplane_name'] +'</span></p>'
        actual_flights+='<p> flight_number <span class="flight-number">'+ flight['flight_number'] +'</span></p>'
        actual_flights+='<p> departure airport <span>'+ flight['departure_airport'] +'</span></p>'
        actual_flights+='<p> arrival airport <span>'+ flight['arrival_airport'] +'</span></p>'
        actual_flights+='<p> departure time <span>'+ flight['departure_time'] +'</span></p>'
        actual_flights+='<p> arrival time <span>'+ flight['arrival_time'] +'</span></p>'
     
        actual_flights+='<p> flight duration <span>'+ flight['flight_duration'] +'</span></p> </div>' 
    return actual_flights

@app.route("/")
def homepage():

        
        
    return get_html('Home').replace('$$FLIGHTS$$',get_flights())


@app.route("/signup")
def signuppage():
        return get_html('signup')

@app.route("/login")
def loginpage():
        return get_html('login')



@app.route("/book")
def bookpage():
        return get_html('book')

@app.route("/addflight")
def addflightpage():
        return get_html('addflight')
    
@app.route("/insert-user")
def insertuserpage():
    first_name = flask.request.args.get('first_name')
    last_name = flask.request.args.get('last_name')
    email = flask.request.args.get('email')
    password = flask.request.args.get('password')
    phone_number = flask.request.args.get('phone_number')
    address = flask.request.args.get('address')
    user_type = flask.request.args.get('user_type')
    if first_name and last_name and email and password and phone_number and address and user_type:
        user = User(first_name, last_name, email, password, phone_number, address, user_type)
        user.save_user('components/users.csv')
        return get_html('Home').replace('$$FLIGHTS$$',get_flights())
    else:
        return get_html('signup')

@app.route("/login-user")
def loginuserpage():
    email = flask.request.args.get('email')
    password = flask.request.args.get('password')

    if email and password:
        user = User()
        user = user.login('components/users.csv', email, password)
        
        if user:
            return {"success": True, "user": user.to_dict()}
        else:
            return {"success": False, "error": "Invalid email or password"}
    else:
        return {"success": False, "error": "Missing email or password"}
