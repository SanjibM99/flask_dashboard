from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dashboard'
db=SQLAlchemy(app)

class List(db.Model):
    slno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(20),  nullable=False)
    phone=db.Column(db.String(12),  nullable=False)
    website= db.Column(db.String(120),  nullable=False)
    mssg= db.Column(db.String(120),  nullable=False)

@app.route("/",methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        website=request.form.get('website')
        message=request.form.get('mssg')

        entry=List(name=name,email=email,phone=phone,website=website,mssg=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("dashb.html")

app.run(debug=True)