from flask import Flask, jsonify, abort, request, make_response
from werkzeug.exceptions import HTTPException
import json

# Create an instance of the class
app = Flask(__name__)


@app.route('/<string:name>', methods=['GET', 'POST'])
def hello(name):

	# abort(404, description="Resource not found")

	print(request.get_data())

	response = make_response(jsonify(
		"Hello " + name
	), 200)

	response.headers['X-Something'] = 'A value'

	return response


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