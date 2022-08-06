from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost/demoDB'
db = SQLAlchemy(app)
# Define db model
class Data(db.Model):
 __tablename__ = "data"
 id=db.Column(db.Integer, primary_key=True)
 email_= db.Column(db.String(120), unique = True)

 def __init__(self,email):
     self.email= email

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/",methods=["POST"])
def thankyou():
    if request.method == "POST" :
        emial = request.fore["email_name"]
        print(request.form)

        data = Data(email)
        db.session.add(data)
        db.session.comit()
        return render_template("thankyou.html")
@app.route("/about")
def aboutUs():
    return "<h1> About Us<h1>"

if __name__ =="__main__":
    app.run()
    app.debug=Ture
