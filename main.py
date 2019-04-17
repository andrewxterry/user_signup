from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/login', methods=['POST'])

def login():
    error_msg = ''
    user_id = request.form['login_id']
    user_password = request.form['password']
    password_verify = request.form['verify']
    email_verify = request.form['email']
    email_char = ['@', '.']
    
    if user_id == '' or len(user_id) > 20 or len(user_id) < 3 or " " in user_id:
        error_msg = "Your ID and Password must be more than 3 letters, less than 20, and have no spaces" 
        return render_template('index.html', error=error_msg, user_id=user_id, email_id=email_verify)
    
    elif user_password == '' or len(user_password) > 20 or len(user_password) < 3 or ' ' in user_password:
        pas_error = "Invalid password"
        return render_template('index.html', pas_error=pas_error, user_id=user_id, email_id=email_verify)

    elif user_password != password_verify:
        verify_error = "Your passwords must match"
        return render_template('index.html', error_ver=verify_error, user_id=user_id, email_id=email_verify)
    
    elif email_verify == "" or len(email_verify) > 20 or len(email_verify) < 3 or " " in email_verify or "@" not in email_verify or "." not in email_verify:
        email_msg = "Invaild user email"
        return render_template('index.html', email_error=email_msg, user_id=user_id, email_id=email_verify)

    else:
        return render_template("welcome.html", user_name=user_id)


@app.route('/')
def index():
    return render_template("index.html")

app.run()