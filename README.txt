Setup:

	Change the path in 'app.py' accordingly before you start.

	Open 2 command line windows.

	Use window one, go to the folder and type "./app.py".

	Use window two to do all the tests.


Original Data:
	
	users = [
 	{
    "first_name": "Joe",
    "last_name": "Smith",
    "userid": "jsmith",
	}
	]


Test:

	1.Return all the users:
	
		***********
		curl -i http://localhost:5000/users
		***********
	

	2.Return user by userid, if no such user, return 404:
	
		***********
		curl -i http://localhost:5000/users/jsmith 
		***********  
	
			It will return a JSON since we have 'jsmith'.
			
		***********
		curl -i http://localhost:5000/users/mary 
		***********
	
			Since we don't have this user id 'mary' in our JSON, it will return 404.

	
	3.Create a user using JSON
		
		***********
		curl -i -H "Content-Type: application/json" -X POST -d '{"last_name":"lol","first_name":"lol","userid":"lolol"}' http://localhost:5000/users
		***********
		
		use the command once, you'll create a user. Twice you'll get 400 because we already have a same userid
	
	4.Delete a user using URL
	
		***********
		curl -X DELETE http://localhost:5000/users/lolol
		***********
		
		You can create user, show all user, delete user, and show all user again.
		It will return a 500 (I don't know why but will delete the user)
		If you delete the same id again it will output a 404
	
		
	
	

	
	
