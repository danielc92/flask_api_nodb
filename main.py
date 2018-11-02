from flask import Flask, session, render_template, jsonify,request

# Initiate and configure app
app = Flask(__name__)
app.config['API_VERSION'] ='1.0'
app.config['SECRET_KEY'] ='secrety'

# Store the data
employees = [
	{'employee_id':'00001',
	'full name':'duke rogers',
	'dob':'1991-12-23',
	'position':'data analyst',
	'salary':60000}
]

@app.route('/api/employees/show', methods = ['GET'])
def retrieve_all():

	return jsonify(employees)


@app.route('/api/employees/show/<id>', methods = ['GET'])
def retrieve_one(id):

	employee = [emp for emp in employees if emp['employee_id']==id]

	if len(employee) > 0:
	    return jsonify(employee[0])
	else:
		return jsonify({'failed':'no employees with this id'})


@app.route('/api/employees/create', methods = ['POST'])
def create():

	data = request.get_json()
	employees.append(data)

	return jsonify(employees)


if __name__ == '__main__':
	app.run(debug = True, port = 4998)