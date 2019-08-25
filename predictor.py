from flask import Flask, render_template,session,redirect, url_for, flash

from flask_wtf import FlaskForm

from wtforms import (IntegerField,StringField, BooleanField, DateTimeField, RadioField, SelectField, TextField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired
import pickle
filename='finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

app=Flask(__name__)
app.config["SECRET_KEY"]="mykey"

class InfoForm(FlaskForm):
	mob_bank=BooleanField("Is the customer a mobile bank user?")
	atm=BooleanField("Does the customer have an ATM card?")
	odrft_lim=BooleanField("Has hit the overdraft limit during last year?")
	age=IntegerField("Enter customer's age",default=18)
	cus_leng=SelectField("How long as a customer?", choices=[("1","less than 3 years"),("2","3 to 7 years"),("3","more than 7 years")]) 
	submit=SubmitField("Submit")


@app.route("/",methods=["GET","POST"])
def index():
	form=InfoForm()
	if form.validate_on_submit():
		session["mob_bank"]=int(form.mob_bank.data)
		session["atm"]=int(form.atm.data)
		session["odrft_lim"]=int(form.odrft_lim.data)
		session["age"]=form.age.data
		session["cus_leng"]=int(form.cus_leng.data)
		session["result"] = int(loaded_model.predict([[session["mob_bank"],session["atm"],session["odrft_lim"],session["age"],session["cus_leng"]]]))
		
		if session["result"]==0:
			flash("The customer will not accept the card")
		else:
			flash("The customer will accept the card")

		return redirect (url_for("index"))
	return render_template("index.html",form=form)


if __name__=="__main__":
	app.run(debug=True)