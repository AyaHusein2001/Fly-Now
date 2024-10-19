from datetime import datetime
from db import db
from sqlalchemy import func
class Flight(db.Model):
    __tablename__ = 'flights'
    
    id = db.Column(db.Integer, primary_key=True)  
    flight_number = db.Column(db.Integer, unique=True)
    airplane_name = db.Column(db.String(50))
    departure_airport = db.Column(db.String(50))
    arrival_airport = db.Column(db.String(50))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    flight_duration = db.Column(db.String(50))
    flight_capacity = db.Column(db.Integer)

    def __init__(self, flight_number='', airplane_name='', departure_airport='', arrival_airport='', departure_time=None, arrival_time=None, flight_duration=''):
        '''Class Constructor'''
        self.flight_number = int(flight_number) if flight_number else None
        self.airplane_name = airplane_name
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.flight_duration = flight_duration
        self.flight_capacity = 0

    @staticmethod
    def check_if_flight_exists(flight_number):
        """Check if the flight number already exists in the database."""
        try:
            flight = Flight.query.filter_by(flight_number=flight_number).first()
            if flight:
                return flight
            else:
                return None
        except Exception as e:
            return None
        
    @staticmethod
    def search_flights(arrival_airport,user_type):
        """Searches for flights with specific arrival airport name ."""
        try:
            
            flights = Flight.query.filter_by(arrival_airport=arrival_airport).all()
            if user_type == 1:
                # User type 1: Return only flights that are not old
                return [flight for flight in flights if not flight.is_old_flight and flight.flight_capacity <853 ]
            elif user_type == 2:
                # User type 2: Return all flights
                return flights
            else:
                # Default: Return only flights that are not old
                return [flight for flight in flights if not flight.is_old_flight and flight.flight_capacity <853]

        
        except Exception as e:
            return None

    def save_flight(self):
        """Save the flight to the database."""
        try:
            if Flight.check_if_flight_exists(self.flight_number):
                return None,-1  # Flight number exists, so do not accept it
            if self.is_old_flight:
                return None,-2  # this means the flight the user tries to insert is old
            if   self.departure_time > self.arrival_time :
                return None,0  # this means user tries to insert a flight that will arrive before it leaves , which is not logical
            
            db.session.add(self)
            db.session.commit()
            return self,1  
        except Exception as e:
            db.session.rollback()
            return None

    def edit_flight(self, flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration):
        """Edit flight details in the database."""
        try:
            flight = Flight.query.filter_by(flight_number=flight_number).first()
            
            if flight:
                flight.airplane_name = airplane_name
                flight.departure_airport = departure_airport
                flight.arrival_airport = arrival_airport
                flight.departure_time = departure_time
                flight.arrival_time = arrival_time
                flight.flight_duration = flight_duration
               
                db.session.commit()
                return flight  # Return the updated flight instance
            else:
                return None
                
        except Exception as e:
            db.session.rollback()
            return None

    def add_reservation(self):
            """Adds a new reservation to this flight by incrementing flight capacity."""
            try:
                flight = Flight.query.filter_by(flight_number=self.flight_number).first()
                
                if flight:
                    
                    flight.flight_capacity +=1
                    db.session.commit()
                    
                    
            except Exception as e:
                db.session.rollback()
                return None
            
    def cancel_reservation(self):
            """Cancels a reservation to this flight by decrementing flight capacity."""
            try:
                flight = Flight.query.filter_by(flight_number=self.flight_number).first()
                
                if flight:
                    
                    flight.flight_capacity -=1
                    db.session.commit()
                    
                    
            except Exception as e:
                db.session.rollback()
                return None

    @property
    def is_old_flight(self):
        """Determine if the flight is old (i.e., the departure time has passed)."""
        return self.departure_time < datetime.now()

    @staticmethod
    def get_all_flights(user_type):
        """Retrieve all flights from the database, filtered by user_type."""
        try:
            
            flights = Flight.query.all()
            

            if user_type == 1:
                # User type 1: Return only flights that are not old
                return [flight for flight in flights if not flight.is_old_flight and flight.flight_capacity <853 ]
            elif user_type == 2:
                # User type 2: Return all flights
                return flights
            else:
                # Default: Return only flights that are not old
                return [flight for flight in flights if not flight.is_old_flight and flight.flight_capacity <853]

        except Exception as e:
            return None

    def delete_flight(self):
        """Delete a specific flight given its number."""
        try:
            flight = Flight.query.filter_by(flight_number=self.flight_number).first()
            
            if flight:
                
                from models.booking import Booking  
                #when flight is deleted , delete its reservations too.
                bookings = Booking.query.filter_by(flight_number=self.flight_number)
                
                for booking in bookings:
                    try:
                        db.session.delete(booking)  
                        db.session.commit()
                    except Exception as e:
                
                        db.session.rollback()
                        return False
                    
                db.session.delete(flight)
                db.session.commit()
                return True
            else:
                return False        
        except Exception as e:
            
            
            db.session.rollback()
            return False
    
    def to_dict(self):
        """Convert the flight object to a dictionary."""
        return {
            "id": self.id,
            "flight_number": self.flight_number,
            "airplane_name": self.airplane_name,
            "departure_airport": self.departure_airport,
            "arrival_airport": self.arrival_airport,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "flight_duration": self.flight_duration,
            "flight_capacity": self.flight_capacity,
            "is_old_flight": self.is_old_flight  # Include flight status in the dictionary
        }
