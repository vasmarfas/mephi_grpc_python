import grpc
from flask import Flask, request

import ekassa.ekassa_client
import usermanager.usermanager_client

app = Flask(__name__)


@app.route('/')
def hello():
 return "Добро пожаловать в микросервисное приложение!"


@app.route('/create_payment')
def create_payment():
 payment_sum = request.args.get('payment_sum')
 email = request.args.get('email')
 out = ekassa.ekassa_client.create_payment(payment_sum=payment_sum, email=email)
 return out

@app.route('/create_user')
def create_user():
 name = request.args.get('name')
 email = request.args.get('email')

 out = usermanager.usermanager_client.create_user(name=name, email=email)

 return out

@app.route('/get_user')
def get_user():
 userid = request.args.get('user_id')
 out = usermanager.usermanager_client.get_user(userid=userid)

 return out



if __name__ == '__main__':
 app.run(host='0.0.0.0', port=8080, debug=True)