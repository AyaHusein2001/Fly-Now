import csv
import os

class Flight:
    def __init__(self,id ,airplane_name,flight_number,departure_airport,arrival_airport ,departure_time,arrival_time,flight_duration):
        self.id=id
        self.airplane_name=airplane_name
        self.flight_number=flight_number
        self.departure_airport=departure_airport
        self.arrival_airport=arrival_airport
        self.departure_time=departure_time
        self.arrival_time=arrival_time
        self.flight_duration=flight_duration
    
    
    def save_flight(self, file_path):
        file_exists = os.path.isfile(file_path)        
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)            
            if not file_exists:
                writer.writerow(["id" ,"airplane_name","flight_number","departure_airport","arrival_airport" ,"departure_time","arrival_time","flight_duration"])           
            writer.writerow([self.id ,self.airplane_name,self.flight_number,self.departure_airport,self.arrival_airport ,self.departure_time,self.arrival_time,self.flight_duration])
            
    @staticmethod
    def get_all_flights(file_path):
        flights = []
        if os.path.isfile(file_path):
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    flights.append({
                        "id": row["id"],
                        "airplane_name": row["airplane_name"],
                        "flight_number": row["flight_number"],
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


# all_flights = Flight.get_all_flights('flights.csv')
# print(all_flights)