from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/login', methods=['POST'])


def user_id():
    user_id = request.form['login_id']

    error_msg = "Your ID  must be more than 3 letters, less than 20, and have no spaces"
    
    if user_id == '':
        return error_msg
    if len(user_id) > 20 or len(user_id) < 3: 
        return error_msg 
    if " " in user_id:
        return error_msg
    else:
        return redirect("/welcome")
    
def password_login():
    user_password = request.form['password']

    error_msg = "Password must be more than 3 letters, less than 20, and have no spaces"

    if user_password == "":
        return error_msg
    if len(user_password) > 20 or len(user_password) < 3: 
        return error_msg
    if " " in user_password:
        return error_msg
    else:
        return redirect('/welcome')

def password_verify():
    verify_password = request.form['veryify']
    og_password = request.form['password']

    error_msg = "Your passwords must match!"

    if verify_password != og_password:
        return error_msg
    else:
        return redirect('/welcome')


@app.route("/welcome")

def welcome():
    return render_template("welcome.html")


@app.route('/')
def index():
    return render_template("index.html")

app.run()