import csv
import os

class Flight:
    def __init__(self ,flight_number='',airplane_name='',departure_airport='',arrival_airport='' ,departure_time='',arrival_time='',flight_duration=''):
        self.id=None #incremental id
        self.flight_number=flight_number
        self.airplane_name=airplane_name
        self.departure_airport=departure_airport
        self.arrival_airport=arrival_airport
        self.departure_time=departure_time
        self.arrival_time=arrival_time
        self.flight_duration=flight_duration
    
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

    def check_if_flight_exists(self,file_path):
        file_exists = os.path.isfile(file_path)
        
        if not file_exists:
            return False
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["flight_number"] == self.flight_number :
                    return True
        return False
    
    def save_flight(self, file_path):
        file_exists = os.path.isfile(file_path)        
        exists= self.check_if_flight_exists(file_path)
        if exists :
            return None
        else:
            self.id = self._get_latest_id(file_path) + 1
        
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)            
                if not file_exists:
                    writer.writerow(["id" ,"flight_number","airplane_name","departure_airport","arrival_airport" ,"departure_time","arrival_time","flight_duration"])           
                writer.writerow([self.id ,self.flight_number,self.airplane_name,self.departure_airport,self.arrival_airport ,self.departure_time,self.arrival_time,self.flight_duration])
            return self
    
    def edit_flight(self, file_path, flight_number, airplane_name, departure_airport, arrival_airport, departure_time, arrival_time, flight_duration):
        file_exists = os.path.isfile(file_path)
        if not file_exists:
            return None
        
        updated_rows = []
        
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["flight_number"] == flight_number:
                    row["flight_number"] = flight_number
                    row["airplane_name"] = airplane_name
                    row["departure_airport"] = departure_airport
                    row["arrival_airport"] = arrival_airport
                    row["departure_time"] = departure_time
                    row["arrival_time"] = arrival_time
                    row["flight_duration"] = flight_duration
                    
                updated_rows.append(row)

        with open(file_path, mode='w', newline='') as file:
            fieldnames = ["id","flight_number", "airplane_name", "departure_airport", "arrival_airport", "departure_time", "arrival_time", "flight_duration"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)          
            writer.writeheader()
            print(updated_rows)
            writer.writerows(updated_rows)

        return self
    
    def getflight(self, file_path, flight_number):
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
        """Convert the user object to a dictionary."""
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
        flights = []
        if os.path.isfile(file_path):
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
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
    

# flight1 = Flight(1, 1001, "XY123", "Cairo", "London", "2024-10-10 14:00", "2024-10-10 18:00", "4 hours")
# flight1.save_flight('flights.csv')

# flight2 = Flight(2, 2001, "XY123", "Cairo", "London", "2024-10-10 14:00", "2024-10-10 18:00", "5 hours")
# flight2.save_flight('flights.csv')


all_flights = Flight.get_all_flights('components/flights.csv')
print(all_flights[0]['id'])
