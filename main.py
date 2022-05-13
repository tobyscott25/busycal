from flask import Flask, jsonify, abort, request, make_response
from werkzeug.exceptions import HTTPException
import json
import ics_combiner

# Create an instance of the class
app = Flask(__name__)



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
		
		body = "Hit this with a POST request to get a combined calendar. Read the project's README.md"

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