import csv
import os

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

    def getbookings(self, file_path,user_id):
        file_exists = os.path.isfile(file_path)

        self.user_id = user_id
        
        if not file_exists:
            return None
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["user_id"] == self.user_id:
                    booking = Booking(row["flight_number"], row["user_id"], row["name"], row["age"], row["phone_number"]) 
                    booking.id = row["id"] 
                    
                    return booking
        return None  
          
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
 