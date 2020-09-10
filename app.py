from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from datetime import datetime
from sqlalchemy import desc
from flask import render_template

app=Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] ='postgres://brjgqjmnamwnxc:2038ec5ace178f7e6f34d1015384a39e7274126f60488b14a5403582ae5a8966@ec2-3-95-87-221.compute-1.amazonaws.com:5432/d3s7d1dsfli0sd'

app.config[
    'SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
groupId=0
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

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        groupId = request.values['groupId']
        SetMsgNumber = usermessage.query.filter(usermessage.group_id==groupId).filter(usermessage.status=='set').count()
        data_UserData = usermessage.query.filter(usermessage.group_id==groupId).filter(usermessage.status=='set')
        history_dic = {}
        history_list = []
        for _data in data_UserData:
            history_dic['nickname'] = _data.nickname
            history_list.append(history_dic)
            history_dic = {}
        final_list=[]
        for i in range(SetMsgNumber):
            final_list.append(str(history_list[i]['nickname']))
        new_list=[]
        for i in final_list:
            if not i in new_list:
                new_list.append(i)

        output_text=""
        for i in range(SetMsgNumber):
            output_text=output_text + final_list[i]+' '


        return render_template('index_form.html',**locals())

    return render_template('home.html',**locals())

@app.route('/submit',methods={'Post','Get'})
def submit():
    groupId = 0
    groupId = request.values['groupid']
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

    return groupId

if __name__ =="__main__":
    app.run()
