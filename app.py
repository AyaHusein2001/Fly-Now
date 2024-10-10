
from flask import Flask , request
from components.user import User
from components.flight import Flight

app = Flask('app')



def get_html(page_name):
    html_file=open(page_name+'.html')
    content=html_file.read()
    html_file.close()
    return content

def get_flights():
    all_flights = Flight.get_all_flights('components/flights.csv')
    actual_flights=''
    for flight in all_flights:
        actual_flights+='<div class="flight-card">'+'<p> Airplane Aame <span>'+ flight['airplane_name'] +'</span></p>'
        actual_flights+='<p> Flight Number <span class="flight-number">'+ flight['flight_number'] +'</span></p>'
        actual_flights+='<p> Departure Airport <span>'+ flight['departure_airport'] +'</span></p>'
        actual_flights+='<p> Arrival Airport <span>'+ flight['arrival_airport'] +'</span></p>'
        actual_flights+='<p> Departure Time <span>'+ flight['departure_time'] +'</span></p>'
        actual_flights+='<p> Arrival Time <span>'+ flight['arrival_time'] +'</span></p>'
     
        actual_flights+='<p> Flight Duration <span>'+ flight['flight_duration'] +'</span></p> </div>' 
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
    
@app.route("/editflight")
def editflightpage():
    flight_number = request.args.get('flight_number')
    flight=Flight()
    flight= flight.getflight('components/flights.csv',flight_number)
    editflightpage=get_html('editflight')
    editflightpage= editflightpage.replace('$$flight_number$$',flight.flight_number)
    editflightpage=editflightpage.replace('$$airplane_name$$',flight.airplane_name)
    editflightpage=editflightpage.replace('$$departure_airport$$',flight.departure_airport)
    editflightpage=editflightpage.replace('$$arrival_airport$$',flight.arrival_airport)
    editflightpage=editflightpage.replace('$$departure_time$$',flight.departure_time)
    editflightpage=editflightpage.replace('$$arrival_time$$',flight.arrival_time)
    editflightpage=editflightpage.replace('$$flight_duration$$',flight.flight_duration)
    return editflightpage

@app.route("/edit-flight")
def saveeditedflightpage():
    flight_number = request.args.get('flight_number')
    airplane_name = request.args.get('airplane_name')
    departure_airport = request.args.get('departure_airport')
    arrival_airport = request.args.get('arrival_airport')
    departure_time = request.args.get('departure_time')
    arrival_time = request.args.get('arrival_time')
    flight_duration = request.args.get('flight_duration')
    if flight_number:     
        flight=Flight()
        flight.edit_flight('components/flights.csv', flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration)
    return get_html('Home').replace('$$FLIGHTS$$',get_flights())
    
# @app.route("/insert-user")
# def insertuserpage():
#     first_name = request.args.get('first_name')
#     last_name = request.args.get('last_name')
#     email = request.args.get('email')
#     password = request.args.get('password')
#     phone_number = request.args.get('phone_number')
#     address = request.args.get('address')
#     user_type = request.args.get('user_type')
#     if first_name and last_name and email and password and phone_number and address and user_type:
#         user = User(first_name, last_name, email, password, phone_number, address, user_type)
#         user.save_user('components/users.csv')
#         return get_html('Home').replace('$$FLIGHTS$$',get_flights())
#     else:
#         return get_html('signup')

@app.route('/insert-user', methods=['POST'])
def insertuserpage():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    phone_number = request.form['phone_number']
    address = request.form['address']
    user_type = request.form['user_type']
    user = User(first_name, last_name, email, password, phone_number, address, user_type)
    user.save_user('components/users.csv')

    return get_html('Home').replace('$$FLIGHTS$$',get_flights())
    
@app.route("/insert-flight")
def insertflightpage():
    flight_number = request.args.get('flight_number')
    airplane_name = request.args.get('airplane_name')
    departure_airport = request.args.get('departure_airport')
    arrival_airport = request.args.get('arrival_airport')
    departure_time = request.args.get('departure_time')
    arrival_time = request.args.get('arrival_time')
    flight_duration = request.args.get('flight_duration')
    if flight_number and airplane_name and departure_airport and arrival_airport and departure_time and arrival_time and flight_duration:
        flight = Flight(flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration)
        flight.save_flight('components/flights.csv')
        return get_html('Home').replace('$$FLIGHTS$$',get_flights())
    else:
        return get_html('signup')
    
@app.route("/login-user", methods=["POST"])
def loginuserpage():
    
    email = request.form.get('email')  
    password = request.form.get('password')

    if email and password:
        user = User()
        user = user.login('components/users.csv', email, password)
        
        if user:
            return {"success": True, "user": user.to_dict()}
        else:
            return {"success": False, "error": "Invalid email or password"}
    else:
        return {"success": False, "error": "Missing email or password"}

