from flask import Flask 
from flask_restful import Api , Resource , reqparse

app = Flask(__name__)
api = Api(app)

users = [
		{
		'name':"Ram",
		'phone':919199911,
		'job':'Conductor',
		'city':'Mahabubnagar'
		},
		{'name':"Raghu",
		'phone':991122334,
		'job':'Owner',
		'city':'Hyderabad'
		},
		{'name':"Lakshman",
		'phone':8543151878,
		'job':'Pilot',
		'city':'Mumbai'
		},
		{'name':"Raghavan",
		'phone':3434567687,
		'job':'Driver',
		'city':'Mahabubnagar'
		} 
		]


class User(Resource):

	#The get method is used to retrieve 
	#a particular user details by 
	#specifying the name

	def get(self,name):
		for user in users:
			if(name==user['name']):
				return (user , 200)
			return ("User not found" , 404)


	def post(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument('job')
		parser.add_argument('phone')
		args = parser.parse_args()

		for user in users:
			if (name == user['name']):
				return ('User {} already exists'.format(name),400)

		user = {
			'name' : name,
			'job' : args['job'],
			'phone' : args['phone']
		}
		users.append(user)
		return (user ,201)


	def put(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument('job')
		parser.add_argument('phone')
		args = parser.parse_args()

		for user in users:
			if (name == user['name']):
				user['job'] = args['job']
				user['phone'] = args['phone']

		user = {
			'name' : name,
			'job' : args['job'],
			'phone' : args['phone']
		}
		users.append(user)
		return (user ,201)

	def delete(self,name):
		global users
		users = [user for user in users if user['name']!=name]
		return ("{} is deleted ..".format(name),200)

api.add_resource(User,'/user/<string:name>')


 
if __name__ == '__main__':
 	app.run(debug = True)