import csv
import os
from components.flight import Flight
from datetime import datetime
from utilities import _get_latest_id


class Booking:
    # class constructor
    def __init__(self ,flight_number='', user_id='', name='', age='', phone_number=''):
        self.id=None #incremental id
        self.flight_number=flight_number
        self.user_id=user_id
        self.name=name
        self.age=age
        self.phone_number=phone_number
        
    
    def save_booking(self, file_path):
        '''This method saves the new booking to the system'''
        
        file_exists = os.path.isfile(file_path)        
        self.id = _get_latest_id(file_path,'id') + 1
       
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            #if file does not exist , write the header first .          
            if not file_exists:
                writer.writerow(["id","flight_number", "user_id", "name", "age", "phone_number"])           
            writer.writerow([self.id,self.flight_number,self.user_id,self.name,self.age ,self.phone_number])
        return self
    

    def getbookings(self, bookings_file_path, flight_file_path, user_id):
        '''
        This method returns all the bookings of a specific user.
        it takes the user id , finds all books related to him , joins with flight on flight number ,
        to show the user the details of the flight he booked for .
        '''
        bookings_file_exists = os.path.isfile(bookings_file_path)
        flights_file_exists = os.path.isfile(flight_file_path)

        self.user_id = user_id
        bookings = []
        
        if not bookings_file_exists or not flights_file_exists:
            return None
        
        # Retrieve all bookings for the user
        with open(bookings_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["user_id"] == self.user_id:
                    bookings.append(row)
        
        user_flights = []
        
        # If there are bookings, retrieve the corresponding flights
        if bookings:
            with open(flight_file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                flight_rows = list(reader)
                current_time = datetime.now()
                
                for booking in bookings:
                    for row in flight_rows:
                        if row["flight_number"] == booking['flight_number']:
                            
                            departure_time = datetime.fromisoformat(row["departure_time"])
                            
                            # Skip flights whose departure_time has already passed
                            if departure_time < current_time:
                                continue
                            
                            # Create Flight object and add additional booking details
                            flight = Flight(row["flight_number"], row["airplane_name"], row["departure_airport"], row["arrival_airport"],
                                            row["departure_time"], row["arrival_time"], row["flight_duration"])
                            
                            flight_dict = flight.to_dict()
                            flight_dict['reservation_id'] = booking['id']
                            flight_dict['name'] = booking['name']
                            flight_dict['age'] = booking['age']
                            flight_dict['phone_number'] = booking['phone_number']
                            
                            user_flights.append(flight_dict)
            
            return user_flights if user_flights else None
        else:
            return None
    
    
    def delete_booking(self, bookings_file_path, reservation_id):
        '''
        This method allows user to cancel a specific reservation given its id .
        '''
        # a temp file to add reservations to .
        temp_file_path = 'components/temp_bookings.csv'
        booking_found = False
        
        
        with open(bookings_file_path, mode='r', newline='') as file, open(temp_file_path, mode='w', newline='') as temp_file:
            
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            writer.writeheader()
        # if this is to be deleted reservation , do not copy it , skip .

            for row in reader:
                if row['id'] == reservation_id :
                    booking_found = True
                    continue
                writer.writerow(row)
        #rename file that contains new reservations .
        if booking_found:
            os.remove(bookings_file_path)
            os.rename(temp_file_path, bookings_file_path)
            return True
        else:
            os.remove(temp_file_path)
            return False
        
 