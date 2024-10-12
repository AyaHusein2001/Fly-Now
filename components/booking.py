import csv
import os
from components.flight import Flight
import random
class Booking:
    def __init__(self ,flight_number='', user_id='', name='', age='', phone_number=''):
        self.id=None #incremental id
        self.flight_number=flight_number
        self.user_id=user_id
        self.name=name
        self.age=age
        self.phone_number=phone_number
        
        
    def _get_latest_id(self, file_path):
        """Private method to get the latest  ID from the file."""
        if not os.path.isfile(file_path):
            return 0
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            last_id = 0
            for row in reader:
                last_id = int(row['id'])
            return last_id        

    def save_booking(self, file_path):
        file_exists = os.path.isfile(file_path)        
        self.id = self._get_latest_id(file_path) + 1
       
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)            
            if not file_exists:
                writer.writerow(["id","flight_number", "user_id", "name", "age", "phone_number"])           
            writer.writerow([self.id,self.flight_number,self.user_id,self.name,self.age ,self.phone_number])
        return self

    def getbookings(self, bookings_file_path,flight_file_path,user_id):
        file_exists = os.path.isfile(bookings_file_path)
        file_exists = os.path.isfile(flight_file_path)

        self.user_id = user_id
        bookings=[]
        
        if not file_exists:
            return None
        
        with open(bookings_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(self.user_id)
                print(row["user_id"])
                if row["user_id"] == self.user_id:
                        bookings.append(row) 
                        
        user_flights=[]    
        # print(bookings)
                    
        if bookings:
            with open(flight_file_path, mode='r', newline='') as file:
                
                reader = csv.DictReader(file)
                flight_rows = list(reader)
                for booking in bookings :
                    for row in flight_rows:
                        print(booking)
                        if row["flight_number"] == booking['flight_number']:
                            print('ahhhhhhhh')
                            flight = Flight(row["flight_number"], row["airplane_name"], row["departure_airport"], row["arrival_airport"],
                                    row["departure_time"], row["arrival_time"], row["flight_duration"])
                            flight.id = row["id"] 
                            flight_dict = flight.to_dict()
                            flight_dict['name'] = booking['name']
                            flight_dict['age'] = booking['age']
                            flight_dict['phone_number'] = booking['phone_number']
                             
                            user_flights.append(flight_dict)
            # print(user_flights)
            return user_flights
                        
        else:
            return None
    
    
    def delete_booking(self, bookings_file_path, user_id, flight_number):
        
        temp_file_path = 'components/temp_bookings.csv'
        booking_found = False
        
        with open(bookings_file_path, mode='r', newline='') as file, open(temp_file_path, mode='w', newline='') as temp_file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                if row['user_id'] == user_id and row['flight_number'] == flight_number:
                    booking_found = True
                    continue
                writer.writerow(row)

        if booking_found:
            os.remove(bookings_file_path)
            os.rename(temp_file_path, bookings_file_path)
            return True
        else:
            os.remove(temp_file_path)
            return False
        
    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
            "id": self.id,
            "flight_number": self.flight_number,
            "user_id": self.user_id,
            "name": self.name,
            "age": self.age,
            "phone_number": self.phone_number
        }
 