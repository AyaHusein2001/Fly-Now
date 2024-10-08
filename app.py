import flask

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
