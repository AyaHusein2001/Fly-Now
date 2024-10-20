from db import db 

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(15))
    address = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    user_type = db.Column(db.Integer)
    
    def __init__(self, first_name='', last_name='', email='', password='', phone_number=None, address=None, user_type='1'):
        '''Class Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.address = address
        self.user_type = int(user_type)if user_type else None 
    
    @staticmethod
    def check_if_email_exists(email):
        '''Utility function that checks if the email exists'''
        try:
            user = User.query.filter_by(email=email).first()
            
            if user:
                return user
            else:
                return None
        
        except Exception as e:
            return None
        
    
    def save_user(self,employee_number):
        """Save the user to the database."""
        #-1: wrong email , 0: not allowed to be admin , 1: signed up suceessfuly
        try:
            if User.check_if_email_exists(self.email):
                # Email already exists, return None
                return None,-1
                    
            if self.user_type==2:
                with open('data/employeesnumbers.txt') as employees_numbers_file:
                    employees_numbers = employees_numbers_file.read().split('\n')

                
                
                if employee_number not in employees_numbers:
                    return None,0
                # only one employee can register with this number
                
                employees_numbers.remove(employee_number)
                with open('data/employeesnumbers.txt', 'w') as file:
                    for emp_number in employees_numbers:
                        file.write(emp_number+"\n")
                
                
            #else sign up the user
            
            db.session.add(self)
            db.session.commit()
            return self,1
        except Exception as e:
            db.session.rollback()
            return None
        
        
    def login(self):
        """Login by checking the user credentials."""

        try:
            user = User.check_if_email_exists(self.email)
            if user and user.password == self.password:
                # Return the user if email and password match
                return user
            else:
                return None
        except Exception as e:
            return None
            
        
    
    def to_dict(self):
        """Convert the user object to a dictionary to be serializable"""
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "address": self.address,
            "user_type": self.user_type
        }
