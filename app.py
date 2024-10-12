
from flask import Flask , request,redirect,render_template
from components.user import User
from components.booking import Booking
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
    if all_flights:
        actual_flights+="<div id='content'>"
        for flight in all_flights:
            actual_flights+='<div class="flight-card">'+'<div class="flight-card-content"> <p> Flight Number </p> <span class="flight-number">'+ flight['flight_number'] +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Airplane Name  </p><span >'+ flight['airplane_name'] +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Departure Airport </p><span>'+ flight['departure_airport'] +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Arrival Airport</p> <span>'+ flight['arrival_airport'] +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Departure Time </p><span>'+ flight['departure_time'] +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Arrival Time </p><span>'+ flight['arrival_time'] +'</span></div>'
        
            actual_flights+='<div class="flight-card-content"><p> Flight Duration </p> <span>'+ flight['flight_duration'] +'</span></div> </div>' 
        actual_flights+="</div>"
    else:
            actual_flights+="<h1 style='padding-top: 60px; margin: 20px;'> There is no flights in the system yet !</h1>"
  
    return actual_flights


def add_bookings_to_the_page(bookings,user_id):

    actual_bookings=''
    if bookings:
        actual_bookings+="<div id='content'>"
        for booking in bookings:
            
            actual_bookings+='<div class="flight-card">'+'<div class="flight-card-content"> <p> Flight Number </p> <span class="flight-number">'+ booking['flight_number'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Airplane Name  </p><span >'+ booking['airplane_name'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Departure Airport </p><span>'+ booking['departure_airport'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Arrival Airport</p> <span>'+ booking['arrival_airport'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Departure Time </p><span>'+ booking['departure_time'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Arrival Time </p><span>'+ booking['arrival_time'] +'</span></div>'
     
            actual_bookings+='<div class="flight-card-content"><p> Flight Duration </p> <span>'+ booking['flight_duration'] +'</span></div>' 
    
            actual_bookings+='<hr style="border: 1px solid #ccc; margin: 10px 0;">' 
            actual_bookings+='<div class="flight-card-content"><p> Name :</p><span>'+ booking['name'] +'</span></div>' 
            actual_bookings+='<div class="flight-card-content"><p> Age : </p><span>'+ booking['age'] +'</span></div>' 
            actual_bookings+='<div class="flight-card-content"><p> Phone Number : </p><span>'+ booking['phone_number'] +'</span></div>' 
 
            actual_bookings += f"<div class='cancel-button'><a href='/delete-booking?user_id={user_id}&flight_number={booking['flight_number']}'>Cancel</a></div></div>"
        actual_bookings+="</div>"
    else:
            actual_bookings+="<h1 style='padding-top: 60px; margin: 20px;' > You havn't booked  any flights yet , go book flights !</h1>"
         
    return actual_bookings

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
    return get_html('book').replace('$$flight_number$$',request.args.get('flight_number')).replace('$$user_id$$',request.args.get('user_id'))

@app.route("/book-flight", methods=['POST'])
def bookflightpage():
    
    name = request.form['name']
    age = request.form['age']
    phone_number = request.form['phone_number']
    flight_number = request.form.get('flight_number')
    user_id = request.form.get('user_id')

    
    booking = Booking(flight_number=flight_number,user_id=user_id,name=name, age=age,phone_number=phone_number)
    booking.save_booking('components/bookings.csv')

    return redirect(f'/reservations?user_id={user_id}')  

@app.route("/reservations")
def reservationspage():
    user_id = request.args.get('user_id')
    
    booking=Booking()
    bookings = booking.getbookings('components/bookings.csv','components/flights.csv',user_id)
    return get_html('reservations').replace('$$RESERVATIONS$$',add_bookings_to_the_page(bookings,user_id))


@app.route("/delete-booking")
def deletebookingpage():
    user_id = request.args.get('user_id')
    flight_number = request.args.get('flight_number')
    
    booking=Booking()
    deleted = booking.delete_booking('components/bookings.csv',user_id,flight_number)
    
    return redirect(f'/reservations?user_id={user_id}') 


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
    return redirect('/')


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
    user = user.save_user('components/users.csv')
    
    if user:
            return {"success": True, "user": user.to_dict()}
    else:
            return {"success": False, "error": " Email already exists,Try another one ."}
    
    
    
    
@app.route("/insert-flight",methods=['POST'])
def insertflightpage():
    flight_number = request.form['flight_number']
    airplane_name = request.form['airplane_name']
    departure_airport = request.form['departure_airport']
    arrival_airport = request.form['arrival_airport']
    departure_time = request.form['departure_time']
    arrival_time = request.form['arrival_time']
    flight_duration = request.form['flight_duration']
    
    if flight_number and airplane_name and departure_airport and arrival_airport and departure_time and arrival_time and flight_duration:
        flight = Flight(flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration)
        flight = flight.save_flight('components/flights.csv')
    
    if flight:
            return {"success": True, "flight": flight.to_dict()}
    else:
            return {"success": False, "error": " Flight Number already exists,Try another one ."}
    
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

