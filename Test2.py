from flask import Flask, request, jsonify
import  mysql.connector as conn

app = Flask(__name__)

@app.route("/testfun")
def test():
    name = request.args.get("get_name")
    if(name):
        return "Hello {}".format(name)
    else:
        return "Hello User"

@app.route("/testMongoDB")
def test1():
    db = request.args.get("dbname")
    table = request.args.get("tablename")
    mydb = conn.connect(host="localhost", user='root', passwd="Arc@7245")
    cursor = mydb.cursor()

    query = "SELECT * FROM {}.{}".format(str(db), str(table))



if(__name__ == "__main__"):
    app.run(port=5002)