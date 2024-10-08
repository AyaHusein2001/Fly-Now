import csv
import os

class User:
    def __init__(self, user_id, first_name, last_name, email, password, phone_number=None, address=None,user_type='customer'):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address
        self.user_type=user_type

    def save_user(self, file_path):
        file_exists = os.path.isfile(file_path)        
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)            
            if not file_exists:
                writer.writerow(["user_id", "first_name", "last_name", "email", "password", "phone_number", "address","user_type"])           
            writer.writerow([self.user_id, self.first_name, self.last_name, self.email,
                             self.password, self.phone_number, self.address,self.user_type])
            
    def get_user_details(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if int(row["user_id"]) == self.user_id: 
                        return {
                            "user_id": row["user_id"],
                            "first_name": row["first_name"],
                            "last_name": row["last_name"],
                            "email": row["email"],
                            "phone_number": row["phone_number"],
                            "address": row["address"],
                            "user_type": row["user_type"]
                        }
        return None
        
        # print(f"User {self.first_name} {self.last_name} saved successfully.")
    


# user = User(1, "John", "Doe", "john.doe@example.com", "password123", "1234567890", "123 Street Name")
# user.save_user('users.csv')

