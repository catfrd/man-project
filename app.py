from flask import Flask, g,render_template, request, redirect, session, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
# from datetime import datetime
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from flask_mail import Mail, Message
# from bson.objectid import ObjectId
# from emailer import send_email


app = Flask(__name__)
app.secret_key = "your_secret_key"

load_dotenv()

PORT            = os.environ.get('PORT')
MONGO_URI       = os.environ.get('MONGO_URI')


client = MongoClient(MONGO_URI)

DB_NAME = 'man-project'
database = client[DB_NAME]


@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/events", methods=['GET','POST'])
def events():
    return render_template('events.html')

@app.route("/rules", methods=['GET','POST'])
def rules():
    return render_template('rules.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    return render_template('contact.html')


@app.route('/register',methods=["GET","POST"])
def register():


    return render_template('register.html')

@app.route("/final-registration", methods=['GET','POST'])
def final_registration():
        

    if (request.method == "POST"):

        collection_name='registration'
        collection=database[collection_name]
        # if 'result_dict' not in g:
        #     result = {}

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

        # x= collection.insert_one(g.result).inserted_id
        # document_id = ObjectId("")


        # Update the document with the specified _id
        #         result = collection.update_one({"_id": document_id}, update_operation)

        for i in range(len(events)):
            if(events[i]=="master_of_masters"):
                eventName="master_of_masters"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")
                result["en1"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                result["tm3"]=[team_member3]
                result["tm4"]=[team_member4]
                result["tm5"]=[team_member5]
                result["tm6"]=[team_member6]
            #     update_operation = {"$set": {"eventName": eventName,"team_members":[team_member1,team_member2,team_member3,team_member4,team_member5,team_member6]}}
            #     collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="the_alpinist"):
                eventName="the_alpinist"
                team_member1=request.form.get("tm1")
                result["en2"]=eventName
                result["tm1"]=[team_member1]
                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1}}
                # collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="auction_play"):
                eventName="auction_play"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                result["en3"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2}}
                # collection.update_one({"_id": document_id}, update_operation)

            elif(events[i]=="haccer_mimica"):
                eventName="haccer_mimica"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")
                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3,"team_member4":team_member4,"team_member5":team_member5,"team_member6":team_member6}}
                # collection.update_one({"_id": document_id}, update_operation)
                result["en4"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                result["tm3"]=[team_member3]
                result["tm4"]=[team_member4]
                result["tm5"]=[team_member5]
                result["tm6"]=[team_member6]

            elif(events[i]=="guessing_games"):
                eventName="guessing_games"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                result["en4"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2}}
                # collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="ted_talk"):
                eventName="ted_talk"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                result["en5"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                result["tm3"]=[team_member3]
                result["tm4"]=[team_member4]
                result["tm5"]=[team_member5]

                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3,"team_member4":team_member4,"team_member5":team_member5}}
                # collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="tuzel_strut"):
                eventName="tuzel_strut"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")
                team_member7=request.form.get("tm7")
                result["en6"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                result["tm3"]=[team_member3]
                result["tm4"]=[team_member4]
                result["tm5"]=[team_member5]
                result["tm6"]=[team_member6]
                result["tm7"]=[team_member7]
                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3,"team_member4":team_member4,"team_member5":team_member5,"team_member6":team_member6,"team_member7":team_member7}}
                # collection.update_one({"_id": document_id}, update_operation)
            elif(events[i]=="sorting_the_chaos"):
                eventName="sorting_the_chaos"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                result["en7"]=eventName
                result["tm7"]=[team_member1,team_member2]
                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2}}
                # collection.update_one({"_id": document_id}, update_operation)

            elif(events[i]=="extrempore"):
                eventName="extrempore"
                team_member11=request.form.get("tm1")
                team_member21=request.form.get("tm2")
                team_member31=request.form.get("tm3")
                # update_operation = {"$set": {"eventName": eventName,"team_member1":team_member1,"team_member2":team_member2,"team_member3":team_member3}}
                # collection.update_one({"_id": document_id}, update_operation)
                result["en8"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                result["tm3"]=[team_member3]
            elif(events[i]=="hr_mind_maze"):
                eventName="hr_mind_maze"
                team_member1=request.form.get("tm1")
                team_member2=request.form.get("tm2")
                team_member3=request.form.get("tm3")
                team_member4=request.form.get("tm4")
                team_member5=request.form.get("tm5")
                team_member6=request.form.get("tm6")
                result["en9"]=eventName
                result["tm1"]=[team_member1]
                result["tm2"]=[team_member2]
                result["tm3"]=[team_member3]
                result["tm4"]=[team_member4]
                result["tm5"]=[team_member5]
                result["tm6"]=[team_member6]

        print("hello hellooo", result)

        session['result_dict'] = result

        return redirect(url_for('registration_success'))

    return render_template('register2.html')

@app.route("/registration-success", methods=['GET','POST'])
def registration_success():

    if (request.method == "POST"):
        # res=dict(request.args)
        res = session.get('result_dict')

        staffincharge=request.form.get("institution")
        staffemail=request.form.get("email")
        mobile=request.form.get("mobile_number")

        collection_name='registration'
        collection=database[collection_name]
        res['staffincharge']=staffincharge
        res['staffemail']=staffemail
        res['mobile']=mobile
        x = collection.insert_one(res)

        print(x)

        return render_template('registration_success.html')
    
    return render_template('register2.html')



if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=PORT)


