from flask import Flask, jsonify, abort, request, make_response
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv
import os, json, mariadb
import ics_combiner

# Load environment variables
load_dotenv()

# Create an instance of the class
app = Flask(__name__)

db_config = {
	'host': 	os.getenv('DATABASE_HOST'),
	'port': int(os.getenv('DATABASE_PORT')),
	'user': 	os.getenv('DATABASE_USER'),
	'password': os.getenv('DATABASE_PASS'),
	'database': os.getenv('DATABASE_NAME')
}

@app.route('/', methods=['GET', 'POST'])
def root():

	if request.method == 'POST':

		ics_urls = request.json
		body = str(
			ics_combiner.combine_ics(ics_urls)
		)

		headers = { "Content-Type": "text/calendar" }
		return make_response(body, 200, headers)

	else:

		# This is here to be displayed if somebody opens the flask dev server in a browser without reading the docs.
		
		body = "Hit this with a POST request to get a combined calendar. Read the project's README.md"

		headers = { "Content-Type": "application/json" }
		return make_response(body, 200, headers)




# TEMPORARY ROUTE: MariaDB test and example before we start legitimately using it
@app.route('/db-example', methods=['GET'])
def index():

	# Connect to MariaDB
	db_connection = mariadb.connect(**db_config)
	# Create a connection cursor
	db_cursor = db_connection.cursor()
	# Query MariaDB
	db_cursor.execute("SELECT * FROM test-table")

	# Get all results from the executed query
	body = str(db_cursor.fetchall())

	headers = { "Content-Type": "application/json" }
	return make_response(body, 200, headers)




@app.route('/<string:name>')
def hello(name):

	abort(404, description="Resource not found")

	headers = { "Content-Type": "application/json" }
	body = jsonify(
		"Hello " + name
	)
	return make_response(body, 200, headers)


@app.errorhandler(HTTPException)
def handle_exception(error):
	# Start with the correct headers and status code from the error
	response = error.get_response()
	# Replace the body with JSON
	response.data = json.dumps({
		"code": error.code,
		"name": error.name,
		"description": error.description,
	})
	# Set the content type header to idicate JSON
	response.content_type = "application/json"
	return response


# Ensures the Flask app runs only when executed in the main file and not when imported in some other file
# Runs the application on a local development server. Do not use run() in a production setting.
# if __name__ == '__main__':
# 	app.run()