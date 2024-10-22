
def get_html(page_name):
    '''
    Utility function to read html page .
    '''
    html_file=open(page_name+'.html')
    content=html_file.read()
    html_file.close()
    return content


def get_flights(all_flights,search):
    '''
    Utility function to dynamically render flights from the db .
    '''
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
            actual_flights+='<div class="flight-card-content"><p> Airplane Name  </p><span >'+flight.airplane_name +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Departure Airport </p><span>'+flight.departure_airport  +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Arrival Airport</p> <span>'+flight.arrival_airport  +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Departure Time </p><span>'+str( flight.departure_time) +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Arrival Time </p><span>'+str(flight.arrival_time)  +'</span></div>'
            actual_flights+='<div class="flight-card-content"><p> Flight Duration </p> <span>'+ flight.flight_duration +'</span></div>' 
            actual_flights+='<div class="flight-card-content"><p> Flight Price </p> <span>'+ str(flight.flight_price) +'$</span></div>' 
            
            actual_flights+='<div class="flight-card-content"><p> NO. Reservations </p> <span>'+ str(flight.flight_capacity) +'</span></div> </div>' 
                
        actual_flights+="</div>"
    else:
            # if function is used in search tell the user There is no flights to this airport !
            # else this mean there is no flights
            if not search:
                actual_flights+="<div class='flex-center'> <img  src='static/robo.png' width='300px' alt='no-result-found'></div>"
                actual_flights+="<h1 style='font-weight:bold; margin: 20px;'> There is no flights in the system yet !</h1>"
            else:
                actual_flights+="<div class='flex-center'> <img  src='static/robo.png' width='300px' alt='no-result-found'></div>"
                actual_flights+="<h1 style=' font-weight:bold; margin: 20px;'> There is no flights to this airport !</h1>"
                
  
    return actual_flights


def add_bookings_to_the_page(bookings,admin,search):
    '''
    Utility function to dynamically render user bookings .
    '''
    
    actual_bookings=''
    if bookings :
        if bookings[0] is not None:
            actual_bookings+="<div  id='content'>"
            for booking in bookings:
                
                actual_bookings+='<div class="flight-card">'+'<div class="flight-card-content"> <p> Flight Number </p> <span class="flight-number">'+ str(booking['flight_number']) +'</span></div>'
                actual_bookings+='<div class="flight-card-content"><p> Airplane Name  </p><span >'+ booking['airplane_name'] +'</span></div>'
                actual_bookings+='<div class="flight-card-content"><p> Departure Airport </p><span>'+ booking['departure_airport'] +'</span></div>'
                actual_bookings+='<div class="flight-card-content"><p> Arrival Airport</p> <span>'+ booking['arrival_airport'] +'</span></div>'
                actual_bookings+='<div class="flight-card-content"><p> Departure Time </p><span>'+ str(booking['departure_time']) +'</span></div>'
                actual_bookings+='<div class="flight-card-content"><p> Arrival Time </p><span>'+ str(booking['arrival_time'])+'</span></div>'
                actual_bookings+='<div class="flight-card-content"><p> Flight Duration </p> <span>'+ booking['flight_duration'] +'</span></div>' 
                actual_bookings+='<div class="flight-card-content"><p> Flight Price </p> <span>'+ str(booking['flight_price']) +'$</span></div>' 
                actual_bookings+='<div class="flight-card-content"><p> NO. Reservations </p> <span>'+ str(booking['flight_capacity']) +'</span></div>' 
                actual_bookings+='<hr style="border: 1px solid #ccc; margin: 10px 0;">'
                actual_bookings+='<div class="flight-card-content"><p> Reservation Number :</p><span>'+ str(booking['reservation_id']) +'</span></div>' 
                actual_bookings+='<div class="flight-card-content"><p> Name :</p><span>'+ booking['name'] +'</span></div>' 
                actual_bookings+='<div class="flight-card-content"><p> Age : </p><span>'+ str(booking['age']) +'</span></div>' 
                actual_bookings+='<div class="flight-card-content"><p> Phone Number : </p><span>'+ booking['phone_number'] +'</span></div>' 
                if not admin:
                    actual_bookings += f"<div class='cancel-button'><a href='/delete-booking?reservation_id={str(booking['reservation_id'])}&flight_number={str(booking['flight_number'])}'>Cancel</a></div></div>"
                else:
                    actual_bookings+='</div>'
            actual_bookings+="</div>"
            
        elif bookings[0] is None and search is not None:# if function is used for search , message will be different .
            actual_bookings+="<div class='flex-center'> <img  src='static/robo.png' width='300px' alt='no-result-found'></div>"
            actual_bookings+="<h1 style=' margin: 10px;' >No Bookings with this Reservation Number !</h1>"
            
    else:
        if not admin:
            actual_bookings+="<div class='flex-center'> <img  src='static/robo.png' width='300px' alt='no-result-found'></div>"
            actual_bookings+="<h1 style=' margin: 10px;' > You havn't booked  any flights yet , go book flights !</h1>"
        else:
            actual_bookings+="<div class='flex-center'> <img  src='static/robo.png' width='300px' alt='no-result-found'></div>"
            actual_bookings+="<h1 style=' margin: 10px;' > This Flight has no bookings yet !</h1>"
            
         
    return actual_bookings