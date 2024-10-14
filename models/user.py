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
        user = User.query.filter_by(email=email).first()

        if user:
            return user
        return None
    
    def save_user(self):
        """Save the user to the database."""
        if User.check_if_email_exists(self.email):
            # Email already exists, return None
            return None 
        
        try:
            db.session.add(self)
            db.session.commit()
            print(f"User {self.first_name} {self.last_name} saved successfully!")
            return self 
        except Exception as e:
            print(f"Error saving user: {e}")
            db.session.rollback()
            return False
        
    def login(self):
        """Login by checking the user credentials."""

        user=User.check_if_email_exists(self.email)
        if user:
            if user.password == self.password:
                # Return the user if email and password match
                return user
        
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