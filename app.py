from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from flask_mail import Mail, Message
from bson.objectid import ObjectId
# from emailer import send_email


app = Flask(__name__)

load_dotenv()

PORT            = os.environ.get('PORT')
MONGO_URI       = os.environ.get('MONGO_URI')


client = MongoClient(MONGO_URI)

DB_NAME = 'man-project'
database = client[DB_NAME]


@app.route("/", methods=['GET','POST'])
def home():

    return render_template('index.html')

@app.route('/register',methods=["GET","POST"])
def register():
    if (request.method == "POST"):

        return redirect('/final-registration')

    return render_template('index.html')

@app.route("/final-registration", methods=['GET','POST'])
def registered():
    if(request.method == "POST"):
        collection_name='registration'
        collection=database[collection_name]

        institutionName=request.values.get("institution")
        department=request.values.get("Department")
        pgug=request.values.get("pg/ug")
        year=request.values.get("year")
        events = request.form.getlist("event")
        result = {
            "institutionName": institutionName,
            "department": department,
            "pgug": pgug,
            "year": year,
            "events": events
        }
        x= collection.insert_one(result).inserted_id
        document_id = ObjectId(x)


# Update the document with the specified _id
        # result = collection.update_one({"_id": document_id}, update_operation)



        print(events)
        for i in range(len(events)):
            if(events[i]=="master_of_masters"):
                eventName="master_of_masters"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")
                update_operation = {"$set": {"eventName": eventName,"team_members":[team_member1,team_member2,team_member3,team_member4,team_member5,team_member6]}}
                collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="The Alpinist"):
                eventName="The Alpinist"
                team_member1=request.form.get("tm1")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1}}
                collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="Auction Play"):
                eventName="Auction Play"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2}}
                collection.update_one({"_id": document_id}, update_operation)

            elif(events[i]=="Haccer Mimica"):
                eventName="Haccer Mimica"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3,"team_member4":team_member4,"team_member5":team_member5,"team_member6":team_member6}}
                collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="Guessing Games"):
                eventName="Guessing Games"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2}}
                collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="Ted Talk"):
                eventName="Ted Talk"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3,"team_member4":team_member4,"team_member5":team_member5}}
                collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="Tuzel Strut"):
                eventName="Tuzel Strut"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")
                team_member7=request.form.get("tm7")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3,"team_member4":team_member4,"team_member5":team_member5,"team_member6":team_member6,"team_member7":team_member7}}
                collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="Sorting the chaos"):
                eventName="Sorting the chaos"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2}}
                collection.update_one({"_id": document_id}, update_operation)

            elif(events[i]=="Extrempore"):
                eventName="Extrempore"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3}}
                collection.update_one({"_id": document_id}, update_operation)

            elif(events[i]=="The Alpinist"):
                eventName="The Alpinist"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")

                update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3,"team_member4":team_member4,"team_member5":team_member5,"team_member6":team_member6}}
                collection.update_one({"_id": document_id}, update_operation)

        return render_template('final_registration.html')
    return render_template('index.html')




@app.route("/registration-success", methods=['GET','POST'])
def registration_success():
    if (request.method == "POST"):
        staffincharge=request.form.get("institution")
        staffemail=request.form.get("email")
        mobile=request.form.get("mobile_number")

        collection_name='staff-details'
        collection=database[collection_name]

    return render_template('index.html')


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=PORT)
