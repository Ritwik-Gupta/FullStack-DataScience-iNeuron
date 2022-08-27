
from flask import Flask ,request,jsonify
import  mysql.connector as conn

app = Flask(__name__)


cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.tasktable  values(%s , %s)", (name, number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))


@app.route('/update', methods=['POST'])
def update():
    name = request.json["name"]

    dataBase = conn.connect(
        host="localhost",
        user="root",
        passwd="Arc@7245",
        database="taskdb"
    )

    query = ("UPDATE tasktable SET number = 100 WHERE name = %s;", str(name))
    cursor.execute(query)
    mydb.commit()

    return jsonify("Updated successfully")

if __name__ == '__main__':
    app.run()