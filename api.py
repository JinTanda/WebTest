from flask import Flask, request, jsonify,Response, abort, make_response
import json

app = Flask(__name__)

@app.route('/')
def index():
 print("index method executed")
 response = jsonify({'message':'Hello World!!!'})
 response.status_code = 200
 return make_response(response)

@app.route('/signup',methods=['GET','POST'])
def signup():
 user_id = request.form['user_id']
 password = request.form['password']
 return make_response(jsonify({'message':"Account successfully created",'user':{'user_id':user_id,'nickname':user_id}}))

@app.route('/users/<user_id>',methods=['GET'])
def get_user(user_id):
 return jsonify({"message": "User details by user_id","user":{
  "user_id": "TaroYamada",
  "nickname": "test",
  "comment": "test"
  }
})

if __name__ == '__main__':
 app.debug = True
 app.run(host='0.0.0.0', port=80)
