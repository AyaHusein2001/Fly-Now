import csv
import os
from datetime import datetime
from utilities import _get_latest_id
class Flight:
    # class constructor
    def __init__(self ,flight_number='',airplane_name='',departure_airport='',arrival_airport='' ,departure_time='',arrival_time='',flight_duration=''):
        self.id=None #incremental id
        self.flight_number=flight_number
        self.airplane_name=airplane_name
        self.departure_airport=departure_airport
        self.arrival_airport=arrival_airport
        self.departure_time=departure_time
        self.arrival_time=arrival_time
        self.flight_duration=flight_duration

    def check_if_flight_exists(self,file_path):
        '''This is a private method to check if this flight number already used before .'''
        file_exists = os.path.isfile(file_path)
        
        if not file_exists:
            return False
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # if u find this flight number , then it already exists .
                if row["flight_number"] == self.flight_number :
                    return True
        return False
    

    
    def save_flight(self, file_path):
        '''This method saves the new flight to the system'''
        file_exists = os.path.isfile(file_path)    
         # if flight number exists , return none   
        exists= self.check_if_flight_exists(file_path)
        if exists :
            return None
        else:
            self.id = _get_latest_id(file_path,'id') + 1
            #if file does not exist , write the header first .
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)            
                if not file_exists:
                    writer.writerow(["id" ,"flight_number","airplane_name","departure_airport","arrival_airport" ,"departure_time","arrival_time","flight_duration"])           
                writer.writerow([self.id ,self.flight_number,self.airplane_name,self.departure_airport,self.arrival_airport ,self.departure_time,self.arrival_time,self.flight_duration])
            return self
    
    def edit_flight(self, file_path, flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration):
        """
        This method is used to edit flight details .
        """
        file_exists = os.path.isfile(file_path)
        if not file_exists:
            return None
        
        updated_rows = []
        
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["flight_number"] == flight_number:
                    # if this is the flight to be edited , reflect the update
                    row["flight_number"] = flight_number
                    row["airplane_name"] = airplane_name
                    row["departure_airport"] = departure_airport
                    row["arrival_airport"] = arrival_airport
                    row["departure_time"] = departure_time
                    row["arrival_time"] = arrival_time
                    row["flight_duration"] = flight_duration
                    
                updated_rows.append(row)
        # rewrite file after update .
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ["id","flight_number", "airplane_name", "departure_airport", "arrival_airport", "departure_time", "arrival_time", "flight_duration"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)          
            writer.writeheader()
            writer.writerows(updated_rows)

        return self
    
    
    def get_flight(self, file_path, flight_number):
        '''
        This method is to get specific flight details .
        '''
        file_exists = os.path.isfile(file_path)

        self.flight_number = flight_number
        
        if not file_exists:
            return None
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["flight_number"] == self.flight_number:
                    flight = Flight(row["flight_number"], row["airplane_name"], row["departure_airport"], row["arrival_airport"],
                                row["departure_time"], row["arrival_time"], row["flight_duration"])
                    flight.id = row["id"] 
                    return flight
        return None
            
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
            "flight_duration": self.flight_duration
        }
        

    @staticmethod
    def get_all_flights(file_path):
        '''A static method to show all flights in the system to visitors .'''
       
        flights = []
        # retrieve all flights in the csv file
        
        
        if os.path.isfile(file_path):
            
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                current_time = datetime.now()
                for row in reader:
                    
                    departure_time = datetime.fromisoformat(row["departure_time"])
                    # if flight time has already passed , skip it .
                    if departure_time < current_time:
                        continue
                    
                    flights.append({
                        "id": row["id"],
                        "flight_number": row["flight_number"],
                        "airplane_name": row["airplane_name"],
                        "departure_airport": row["departure_airport"],
                        "arrival_airport": row["arrival_airport"],
                        "departure_time": row["departure_time"],
                        "arrival_time": row["arrival_time"],
                        "flight_duration": row["flight_duration"]
                    })
        return flights
    


