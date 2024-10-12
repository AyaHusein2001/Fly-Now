import csv
import os

class User:
    def __init__(self, first_name='', last_name='', email='', password='', phone_number=None, address=None, user_type='1'):
        self.user_id = None  # incremental user id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address
        self.user_type = user_type

    def _get_latest_id(self, file_path):
        """Private method to get the latest user ID from the file."""
        if not os.path.isfile(file_path):
            return 0
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            last_id = 0
            for row in reader:
                last_id = int(row['user_id'])
            return last_id
    def check_if_email_exists(self,file_path):
        file_exists = os.path.isfile(file_path)
        
        if not file_exists:
            return False
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["email"] == self.email :
                    return True
        return False
        
    def save_user(self, file_path):
        """Save the user data to the file."""
        file_exists = os.path.isfile(file_path)
        
        exists= self.check_if_email_exists(file_path)
        if exists :
            return None
        else:
            self.user_id = self._get_latest_id(file_path) + 1

            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["user_id", "first_name", "last_name", "email", "password", "phone_number", "address", "user_type"])
                writer.writerow([self.user_id, self.first_name, self.last_name, self.email,
                                self.password, self.phone_number, self.address, self.user_type])
            return self

    def login(self, file_path, email, password):
        """Login by checking the user credentials."""
        file_exists = os.path.isfile(file_path)

        self.email = email
        self.password = password
        if not file_exists:
            return None
        
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["email"] == self.email and row["password"] == self.password:
                    user = User(row["first_name"], row["last_name"], row["email"], row["password"],
                                row["phone_number"], row["address"], row["user_type"])
                    user.user_id = row["user_id"] 
                    return user
        return None

    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "user_type": self.user_type
        }

