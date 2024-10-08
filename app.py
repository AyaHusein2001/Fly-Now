import flask
from components.user import User
app = flask.Flask('notes')

def get_html(page_name):
    html_file=open(page_name+'.html')
    content=html_file.read()
    html_file.close()
    return content

def get_notes():
    notes=open('notes.txt')
    content=notes.read()
    notes.close()
    notes_list = content.split('\n')
    return notes_list

@app.route("/")
def homepage():
    return get_html('Home')


@app.route("/signup")
def signuppage():
        return get_html('signup')

@app.route("/login")
def loginpage():
        return get_html('login')

    
@app.route("/insert-user")
def insertnotepage():
    first_name = flask.request.args.get('first_name')
    last_name = flask.request.args.get('last_name')
    email = flask.request.args.get('email')
    password = flask.request.args.get('password')
    phone_number = flask.request.args.get('phone_number')
    address = flask.request.args.get('address')
    user_type = flask.request.args.get('user_type')
    if first_name and last_name and email and password and phone_number and address and user_type:
        user = User(first_name, last_name, email, password, phone_number, address, user_type)
        user.save_user('components/users.csv')
        return get_html('Home')
    else:
        return get_html('signup')
         