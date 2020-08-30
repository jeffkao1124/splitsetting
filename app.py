from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from datetime import datetime
from sqlalchemy import desc
from flask import render_template

app=Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] ='postgres://szcllceapwexar:6de14fbb3a64a6ac2c1f81d1a6f6e528ee13cdbf7e2abf80ee0f57396180b228@ec2-54-236-146-234.compute-1.amazonaws.com:5432/deu86ol7k69o7t'

app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class usermessage(db.Model):
    __tablename__ ='usermessage'
    id = db.Column(db.String(50), primary_key=True)
    group_num = db.Column(db.Text)
    nickname = db.Column(db.Text)
    group_id = db.Column(db.String(50))
    type = db.Column(db.Text)
    status = db.Column(db.Text)
    account = db.Column(db.Text)
    user_id = db.Column(db.String(50))
    message = db.Column(db.Text)
    birth_date = db.Column(db.TIMESTAMP)

@app.route('/')
def index():
    data_UserData = usermessage.query.order_by(usermessage.birth_date.desc()).all()
    history_dic = {}
    history_list = []
    for _data in data_UserData:
        history_dic['user_id'] = _data.user_id
        history_dic['group_id'] = _data.group_id
        history_dic['message'] = _data.message
        history_dic['account'] = _data.account
        history_list.append(history_dic)
        history_dic = {}

    return render_template('index.html',history_list[0])

if __name__ =="__main__":
    app.run()
