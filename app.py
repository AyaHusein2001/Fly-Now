from flask import Flask, request, redirect, session
from datetime import timedelta
from datetime import datetime
from db import db 
from models.user import User  
from models.flight import Flight  
from models.booking import Booking  

app = Flask('app')

app.secret_key = 'IloveSecurity2001'
app.permanent_session_lifetime = timedelta(days=15)  # session expires after 15 days
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flightbookingsystem.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)  

def get_html(page_name):
    '''
    Utility function to read html page .
    '''
    html_file=open(page_name+'.html')
    content=html_file.read()
    html_file.close()
    return content


def get_flights(user_type):
    '''
    Utility function to dynamically render flights from the db .
    '''
    
    all_flights = Flight.get_all_flights(user_type)
    actual_flights=''
    if all_flights:
        actual_flights+="<div id='content'>"
        for flight in all_flights:
            #set different background for old flights
            flight_class = "flight-card old-flight" if flight.is_old_flight else "flight-card"
            
            actual_flights += f'<div class="{flight_class}">'
            if flight.is_old_flight:
                actual_flights+='<div style="align-self:center; padding-bottom: 15px;"> <p> Old Flight </p> </div>'
            actual_flights+='<div class="flight-card-content"> <p> Flight Number </p> <span class="flight-number">'+str(flight.flight_number)  +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Airplane Name  </p><span >'+str(flight.airplane_name) +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Departure Airport </p><span>'+str(flight.departure_airport)  +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Arrival Airport</p> <span>'+str(flight.arrival_airport)  +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Departure Time </p><span>'+str( flight.departure_time) +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Arrival Time </p><span>'+str(flight.arrival_time)  +'</span></div>'
        
            actual_flights+='<div class="flight-card-content"><p> Flight Duration </p> <span>'+ str(flight.flight_duration) +'</span></div>' 
            
            actual_flights+='<div class="flight-card-content"><p> Flight Capacity </p> <span>'+ str(flight.flight_capacity) +'</span></div> </div>' 
                
        actual_flights+="</div>"
    else:
            actual_flights+="<h1 style='padding-top: 60px; margin: 20px;'> There is no flights in the system yet !</h1>"
  
    return actual_flights


def add_bookings_to_the_page(bookings):
    '''
    Utility function to dynamically render user bookings .
    '''
    actual_bookings=''
    if bookings:
        actual_bookings+="<div style='padding-top:60px;' id='content'>"
        for booking in bookings:
            
            actual_bookings+='<div class="flight-card">'+'<div class="flight-card-content"> <p> Flight Number </p> <span class="flight-number">'+ str(booking['flight_number']) +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Airplane Name  </p><span >'+ booking['airplane_name'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Departure Airport </p><span>'+ booking['departure_airport'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Arrival Airport</p> <span>'+ booking['arrival_airport'] +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Departure Time </p><span>'+ str(booking['departure_time']) +'</span></div>'
            actual_bookings+='<div class="flight-card-content"><p> Arrival Time </p><span>'+ str(booking['arrival_time'])+'</span></div>'
     
            actual_bookings+='<div class="flight-card-content"><p> Flight Duration </p> <span>'+ booking['flight_duration'] +'</span></div>' 
            actual_bookings+='<div class="flight-card-content"><p> Flight Capacity </p> <span>'+ str(booking['flight_capacity']) +'</span></div>' 
            actual_bookings+='<hr style="border: 1px solid #ccc; margin: 10px 0;">'
            actual_bookings+='<div class="flight-card-content"><p> Reservation Number :</p><span>'+ str(booking['reservation_id']) +'</span></div>' 
            actual_bookings+='<div class="flight-card-content"><p> Name :</p><span>'+ booking['name'] +'</span></div>' 
            actual_bookings+='<div class="flight-card-content"><p> Age : </p><span>'+ str(booking['age']) +'</span></div>' 
            actual_bookings+='<div class="flight-card-content"><p> Phone Number : </p><span>'+ booking['phone_number'] +'</span></div>' 
 
            actual_bookings += f"<div class='cancel-button'><a href='/delete-booking?reservation_id={str(booking['reservation_id'])}&flight_number={str(booking['flight_number'])}'>Cancel</a></div></div>"
        actual_bookings+="</div>"
    else:
            actual_bookings+="<h1 style='padding-top: 60px; margin: 20px;' > You havn't booked  any flights yet , go book flights !</h1>"
         
    return actual_bookings

@app.route("/")
def homepage():
    """
    This function handles the routing for the home page of the web application.

    Route:
    - GET /

    Functionality:
    - Returns the home page HTML content.
    - The placeholder string `$$FLIGHTS$$` in the HTML template is replaced with the actual flights.
    
    """
    with app.app_context():  # Use app context to create tables
        
        db.create_all()
        if session:
            
            user_type=session['user_type']
        else:
            user_type='1'
        return get_html('Home').replace('$$FLIGHTS$$',get_flights(user_type))
    
#-----------------------------------User-----------------------------------------------
@app.route("/signup")
def signuppage():
    """
    This function handles the routing for the signup page of the web application.
    Route:
    - GET /signup

    Functionality:
    - Returns the HTML content for the signup page.
    """
    
    return get_html('signup')

@app.route("/login")
def loginpage():
    """
    This function handles the routing for the login page of the web application.
    Route:
    - GET /login

    Functionality:
    - Returns the HTML content for the login page.
    """
    return get_html('login')

@app.route('/insert-user', methods=['POST'])
def insertuserpage():
    """
    This function handles the insertion of a new user into the system.

    Route:
    - POST /insert-user
    Functionality:
    - Retrieves all the user details from the form submission.
    - Attempts to save the user to the db .
    - If the user is successfully saved, returns a success response with the user's details.
    - If the email already exists in the system, returns a failure response with an appropriate error message.
    
    """
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    phone_number = request.form['phone_number']
    address = request.form['address']
    user_type = request.form['user_type']
    employee_number = request.form['employee_number'] if request.form['employee_number'] else ''
    
    user = User(first_name, last_name, email, password, phone_number, address, user_type)
    # print('ah',user_type,employee_number)
    user,flag = user.save_user(employee_number)
    print('ah',user,flag)
    
    #-1: wrong email , 0: not allowed to be admin , 1: signed up suceessfuly
    
    if user and flag==1:
        session.permanent=True
        session['user']=user.user_id
        session.permanent=True
        session['user_type']=user.user_type
        
        return {"success": True, "user": user.to_dict()}
 
    elif user==None and flag==0:
        return {"success": False, "error": "You are not autherized to be admin "}
    elif user==None and flag==-1:
        return {"success": False, "error": " Email already exists,Try another one ."}
    
    
@app.route("/login-user", methods=["POST"])
def loginuserpage():
    """
    This function handles the login process for users.

    Route:
    - POST /login-user

    Functionality:
    - Retrieves the user's email and password from the form data.
    - If both the email and password are provided:
        - Calls the `login` method of the `User` class to verify the credentials .
        - If the credentials match, returns a success response with the user details.
        - If the credentials are invalid, returns a failure response with an error message.
    - If either email or password is missing, returns a failure response with an appropriate error message.
    
    """
    email = request.form.get('email')  
    password = request.form.get('password')
    

    if email and password:
        user = User(email=email,password=password)
        user = user.login()
        session.permanent=True
        session['user']=user.user_id
        session.permanent=True
        session['user_type']=user.user_type
        
        
        if user:
            return {"success": True, "user": user.to_dict()}
        else:
            return {"success": False, "error": "Invalid email or password"}
    else:
        return {"success": False, "error": "Missing email or password"}



    
@app.route("/logout")
def logoutpage():
    """
    This function logs out user of the web application by removing his credintials from the session.
    Route:
    - GET /logout

    Functionality:
    - removes user id from the session
    """
    session.pop('user',None)
    session['user_type']='1'
    return redirect('/')
    
@app.route("/addadmin")
def addadminpage():
    """
    This function handles the routing for the addnewadmin page of the web application.
    Route:
    - GET /addadmin

    Functionality:
    - renders add new admin page
    """
    
    return get_html('addnewadmin')

@app.route("/add-admin",methods=['POST'])
def addnewadminpage():
    """
    This function adds a new admin to the web application by saving the employee number 
    to a text file.

    Route:
    - POST /add-admin

    Functionality:
    - Retrieves the employee number from the submitted form data .
    - Writes the employee number to the 'data/employeesnumbers.txt' file. 
      
    """
    employee_number=request.form['employee_number']
    with open('data/employeesnumbers.txt', 'a') as file:
        file.write(employee_number+"\n")
        
    return get_html('adminadded')

#-----------------------------------Flight-----------------------------------------------
@app.route("/addflight")
def addflightpage():
    """
    This function handles the rendering of the flight addition page.

    Route:
    - GET /addflight

    Functionality:
    - Returns the rendered HTML content to be displayed in the user's browser.

    """
    return get_html('addflight')

    
    
@app.route("/insert-flight",methods=['POST'])
def insertflightpage():
    """
    This function handles the insertion of a new flight into the system.

    Route:
    - POST /insert-flight

    Functionality:
    - Retrieves all necessary flight details from the form submission.
    - Validates that all required fields (flight number, airplane name, airports, times, and duration) are provided.
    - If valid, creates a new `Flight` object and saves it to the db file.
    - Returns a success response with the flight details if the flight is successfully saved.
    - If the flight number already exists, returns a failure response with an appropriate error message.
    
    
    """
    flight_number = request.form['flight_number']
    airplane_name = request.form['airplane_name']
    departure_airport = request.form['departure_airport']
    arrival_airport = request.form['arrival_airport']
    departure_time_str = request.form['departure_time']
    arrival_time_str = request.form['arrival_time']
    flight_duration = request.form['flight_duration']
    
     # Convert the string to datetime object
    departure_time = datetime.strptime(departure_time_str, '%Y-%m-%dT%H:%M')
    arrival_time = datetime.strptime(arrival_time_str, '%Y-%m-%dT%H:%M')
    
    if flight_number and airplane_name and departure_airport and arrival_airport and departure_time and arrival_time and flight_duration:
        flight = Flight(flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration)
        flight = flight.save_flight()
    
    if flight:
            return {"success": True, "flight": flight.to_dict()}
    else:
            return {"success": False, "error": " Flight Number already exists,Try another one ."}

    
@app.route("/editflight")
def editflightpage():
    """
    This function handles the rendering of the flight editing page.

    Route:
    - GET /editflight

    Functionality:
    - Retrieves the `flight_number` from the query string.
    - Creates an instance of the `Flight` class and retrieves the flight details .
    - Replaces placeholders in the HTML template with the actual flight details .
    - Returns the updated HTML content .

    """
    
    flight_number = request.args.get('flight_number')
    
    flight= Flight.check_if_flight_exists(flight_number)
    if flight:
        editflightpage=get_html('editflight')
        
        editflightpage= editflightpage.replace('$$flight_number$$',str(flight.flight_number))
        editflightpage=editflightpage.replace('$$airplane_name$$',flight.airplane_name)
        editflightpage=editflightpage.replace('$$departure_airport$$',flight.departure_airport)
        editflightpage=editflightpage.replace('$$arrival_airport$$',flight.arrival_airport)
        editflightpage=editflightpage.replace('$$departure_time$$',str(flight.departure_time))
        editflightpage=editflightpage.replace('$$arrival_time$$',str(flight.arrival_time))
        editflightpage=editflightpage.replace('$$flight_duration$$',flight.flight_duration)
        return editflightpage
    else:
        redirect('/')

    
@app.route("/edit-flight",methods=['POST'])
def saveeditedflightpage():
    """
    This function handles the saving of edited flight details.

    Route:
    - GET /edit-flight

    Functionality:
    - Retrieves all necessary flight details from the query string.
    - If a `flight_number` is provided, update the flight details in db.
    - After saving the changes, redirects the user to the homepage.

    """
    flight_number = request.form['flight_number']
    airplane_name = request.form['airplane_name']
    departure_airport = request.form['departure_airport']
    arrival_airport = request.form['arrival_airport']
    departure_time_str = request.form['departure_time']
    arrival_time_str = request.form['arrival_time']
    flight_duration = request.form['flight_duration']
    
     # Convert the string to datetime object
    departure_time = datetime.strptime(departure_time_str, '%Y-%m-%dT%H:%M')
    arrival_time = datetime.strptime(arrival_time_str, '%Y-%m-%dT%H:%M')
    
    if flight_number:     
        flight=Flight()
        flight.edit_flight( flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration)
    return redirect('/')


@app.route("/deleteflight")
def deleteflightpage():    
    """
    This function handles the deletion of a specific flight.

    Route:
    - GET /deleteflight

    Functionality:
    - Retrieves the  `flight_number` from the query string.
    - Calls the `delete_flight` method of the `Flight` class to remove the booking .
    - After deleting the booking, redirects the user back to the home page .

    """
    flight_number = request.args.get('flight_number')
    
    flight=Flight(flight_number=flight_number)
    deleted = flight.delete_flight()
    return redirect('/')

#-----------------------------------Booking-----------------------------------------------


@app.route("/book")
def bookpage():
    """
    This function handles the routing for the flight booking page of the web application.

    Route:
    - GET /book
    
    Functionality:
    - Returns the HTML content for the booking page.
    - The placeholders `$$flight_number$$` in the HTML template are replaced with the corresponding values from the request query parameters.
    """
    return get_html('book').replace('$$flight_number$$',request.args.get('flight_number'))


@app.route("/book-flight", methods=['POST'])
def bookflightpage():
    """
    This function handles the flight booking form submission.

    Route:
    - POST /book-flight

    Functionality:
    - Extracts the user details and flight information from the form submission.
    - Saves the booking details to the db .
    - Redirects the user to the reservations page .
    
   """
    name = request.form['name']
    age = request.form['age']
    phone_number = request.form['phone_number']
    flight_number = request.form.get('flight_number')
    user_id = session['user']

    booking = Booking(flight_number=flight_number,user_id=user_id,name=name, age=age,phone_number=phone_number)
    booking.save_booking()

    return redirect('/reservations')  

@app.route("/reservations")
def reservationspage():
    """
    This function handles the routing for the user's reservations page.

    Route:
    - GET /reservations

    Functionality:
    - Retrieves the user's bookings .
    - The bookings are fetched from the db .
    - The placeholder `$$RESERVATIONS$$` in the HTML template is replaced with the user's bookings .
    """
    user_id = session['user']
    booking=Booking(user_id=user_id)
    bookings = booking.get_bookings()
    return get_html('reservations').replace('$$RESERVATIONS$$',add_bookings_to_the_page(bookings))


@app.route("/delete-booking")
def deletebookingpage():
    """
    This function handles the deletion of a specific booking for a user.

    Route:
    - GET /delete-booking
    
    Functionality:
    - Retrieves the  `reservation_id` from the query string.
    - Calls the `delete_booking` method of the `Booking` class to remove the booking .
    - After deleting the booking, redirects the user back to the reservations page .

    """
    reservation_id = request.args.get('reservation_id')
    flight_number = request.args.get('flight_number')
    
    booking=Booking(flight_number=flight_number)
    deleted = booking.delete_booking(id=reservation_id)
    
    return redirect('/reservations') 

