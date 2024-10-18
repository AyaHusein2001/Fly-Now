from datetime import datetime
from models.flight import Flight
from db import db 

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.Integer, db.ForeignKey('flights.flight_number'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    phone_number = db.Column(db.String)
    
    #lazy=True means that the related Flight object is loaded only when it is accessed,
    #not when the Booking object is initially queried.
   
    flight = db.relationship("Flight", backref="bookings", lazy=True)
    flight = db.relationship("User", backref="bookings", lazy=True)

    def __init__(self, flight_number='', user_id='', name='', age='', phone_number=''):
        '''Class Constructor'''
        self.flight_number = flight_number
        self.user_id = int(user_id)if user_id else None 
        self.name = name
        self.age = int(age)if age else None 
        self.phone_number = phone_number

    def save_booking(self):
        '''This method saves the new booking to the database'''
        try:
            flight=Flight(flight_number=self.flight_number)
            flight.add_reservation()
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            
            return None

    
    def get_bookings(self):
        '''
        This method returns all the bookings of a specific user.
        It takes the user id, finds all bookings related to him, 
        and joins with flight on flight number to show the user the details of the flight they booked for.
        '''
        try:
            bookings = Booking.query.filter_by(user_id=self.user_id).all()
            current_time = datetime.now()

            user_flights = []
            for booking in bookings:
                flight = Flight.query.filter_by(flight_number=booking.flight_number).first()
                
                if flight and flight.departure_time >= current_time:
                    flight_dict = flight.to_dict()
                    flight_dict['reservation_id'] = booking.id
                    flight_dict['name'] = booking.name
                    flight_dict['age'] = booking.age
                    flight_dict['phone_number'] = booking.phone_number

                    user_flights.append(flight_dict)

            return user_flights if user_flights else None
        except Exception as e:
            return None
        
    @staticmethod
    def get_bookings_of_flight(flight_number):
        '''
        This method returns all the bookings of a specific flight.
        It takes the flight number, finds all bookings related to it, 
        and joins with flight on flight number to show the the details of the flight and the booking too.
        '''
        try:
            bookings = Booking.query.filter_by(flight_number=flight_number).all()
          

            flights = []
            for booking in bookings:
                
                flight = Flight.query.filter_by(flight_number=booking.flight_number).first()
                
                if flight:
                    
                    flight_dict = flight.to_dict()
                    
                    flight_dict['reservation_id'] = booking.id
                    
                    flight_dict['name'] = booking.name
                    flight_dict['age'] = booking.age
                    flight_dict['phone_number'] = booking.phone_number
                    flights.append(flight_dict)

            return flights if flights else None
        except Exception as e:
          
            
            return None

    def find_booking(self,id,user_type,user_id,flight_number):
        '''
        This method returns the details of a specific booking joining it with the flight details.
        '''
        try:
            if user_type==1:#search with user id , because user can not access other users reservations
                booking = Booking.query.filter_by(id=id,user_id=user_id).first()
            else:
               #for an admin , he is viewing the reservations of a specific flight , so 
               #we also must search with flight number
                booking = Booking.query.filter_by(id=id,flight_number=flight_number).first()
                
            if booking:
                flight = Flight.query.filter_by(flight_number=booking.flight_number).first()
                current_time = datetime.now()
                # return only reservations for flights that its time has not passed
                if flight and flight.departure_time >= current_time:    
                    flight_dict = flight.to_dict()
                    flight_dict['reservation_id'] = booking.id
                    flight_dict['name'] = booking.name
                    flight_dict['age'] = booking.age
                    flight_dict['phone_number'] = booking.phone_number
                return flight_dict if flight_dict else None
        except Exception as e:
            return None

    
    def delete_booking(self,id):
        '''
        This method allows a user to cancel a specific reservation given its id.
        '''
        try:
            booking = Booking.query.get(id)
            if booking:
                flight=Flight(flight_number=self.flight_number)
                #decrement capacity
                flight.cancel_reservation()
                db.session.delete(booking)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            return False
