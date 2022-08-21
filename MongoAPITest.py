#python -m pip install pymongo

from pymongo import MongoClient
from flask import Flask, jsonify, request

app = Flask(__name__)

def getDatabase():
    CONNECTION_STRING = "mongodb+srv://ritwik97:Arc%407245@cluster0.xbzeefb.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING) #connecting to Mongo server
    myDB = client["TestDB1"]
    return myDB

@app.route("/insertRecord", methods=["GET", "POST"])
def insertRecord():
    myDB = getDatabase()

    if(request.method == "POST"):
        name = request.json["Name"]
        age = request.json["Age"]
        email = request.json["Email"]
        empId = request.json["EmpId"]

    EmpObj = {
        "Name": name,
        "Age": age,
        "Email": email,
        "EmpId": empId
    }
    myCollection = myDB['myCollectionTest1']
    myCollection.insert_one(EmpObj)
    return jsonify("Record Inserted")

@app.route("/updateRecord", methods=["GET", "POST"])
def updateRecord():
    myDB = getDatabase()

    newName = request.json["Name"]
    newAge = request.json["Age"]
    newEmail = request.json["Email"]
    empId = request.json["EmpId"]

    newEmpObj = {
        "Name": newName,
        "Age": newAge,
        "Email": newEmail,
    }

    myCollection = myDB['myCollectionTest1']
    myQuery = {"EmpId": empId}
    newValues = {"$set": newEmpObj}
    myCollection.update_one(myQuery, newValues)
    print("Record updated")

@app.route("/deleteRecord", methods=["GET", "POST"])
def deleteRecord():
    myDB = getDatabase()

    empId = request.json["EmpId"]

    myCollection = myDB['myCollectionTest1']
    myQuery = {"EmpId": empId}
    myCollection.deleteone(myQuery)
    print("Record Deleted")

@app.route("/getRecord", methods=["GET", "POST"])
def getRecord():
    myDB = getDatabase()

    empId = request.json["EmpId"]

    myCollection = myDB['myCollectionTest1']
    myQuery = {"EmpId": empId}
    myCollection.find_one(myQuery)
    print("Record Fetched")

if(__name__ == "__main__"):
    app.run()





