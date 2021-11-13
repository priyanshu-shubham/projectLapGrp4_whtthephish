from flask import Flask, render_template
from flask import redirect, url_for, request,session
from src.common.database import Database
from src.models.user import User 
from src.secrets import SECRET_KEY

PORT = 8000

app = Flask("__main__")
app.secret_key=SECRET_KEY

@app.before_first_request
def initialize_database():
    Database.initialize()
    session['email']=None

@app.route("/")
def index():
    return "Welcome"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        email=request.form['email']
        u_password=request.form['password']
        if User.login_valid(email=email,password=u_password):
            User.login(email)
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Username Or Password"
    return render_template('index.html')



@app.route("/signUp",methods=["GET","POST"])
def signUp():
    if request.method == "POST":
        email=request.form['email']
        u_password=request.form['password']
        name=request.form['name']
        if not User.validate_Form(name,email,u_password):
            return "Form Validation Failed!"
        if User.get_by_email(email) is not None:
            return "Email Already Registered!"
        success=User.register(email,u_password,name)
        if not success:
            return "Something Went Wrong. Please try Again Later."
        return redirect('/dashboard')
        
    return render_template('signUp.html')


@app.route("/dashboard")
def dashboard():
    if session['email'] is not None:
        user=User.get_by_email(session['email'])
        return render_template('dashboard.html',user=user)
    else:
        return redirect(url_for('login'))

@app.route('/level1',methods=["GET","POST"])
def level1():
    if session['email'] is not None: 
        if request.method=='POST':
            print(request.form['question1'])
            print(request.form['question2'])
            print(request.form['question3'])
            print(request.form['question4'])
        return render_template('Level1.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    User.logout()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = PORT, debug = True)