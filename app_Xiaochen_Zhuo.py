#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

users = [
 {
    "first_name": "Joe",
    "last_name": "Smith",
    "userid": "jsmith",
}

]




]

#Improve the handler    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
#Return all users
@app.route('/users', methods=['GET'])
def get_user1():
    return jsonify({'users': users})

#Returns the matching user record or 404 if none exist.
@app.route('/users/<userid>', methods=['GET'])
def get_user2(userid):
    user = [user for user in users if user['userid'] == str(userid)]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

#Create a user
@app.route('/users', methods=['POST'])
def create_user():
	id = request.json['userid']
	for u in users:
		if u['userid'] == id:
			abort(400)
	user = {
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'userid': request.json['userid'],
    }
	users.append(user)
	return jsonify({'user': user}), 201

#Delete a user
@app.route('/users/<userid>', methods=['DELETE'])
def delete_user(userid):
	user = [user for user in users if user['userid']==userid]
	if user == []:
		abort(404)
	users.remove(user[0])
	return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=False)
    