from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/login', methods=['POST'])

def user_id():
    user_id = request.form['login_id']

    error_msg = "Your ID must be more than 3 characters and less than 20 characters"
    
    if user_id == '':
        return error_msg
    if len(user_id) > 20 or len(user_id) < 3: 
        return error_msg 
    


@app.route('/')
def index():
    return render_template("index.html")

app.run()