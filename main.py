from flask import Flask, jsonify, abort
from werkzeug.exceptions import HTTPException
import json

# Create an instance of the class
app = Flask(__name__)


@app.route('/<string:name>/')
def hello(name):

	abort(404, description="Resource not found")

	out = "Hello " + name
	return jsonify(out), 200


@app.errorhandler(HTTPException)
def handle_exception(error):
	# Start with the correct headers and status code from the error
	response = error.get_response()
	# Replace the body with JSON
	response.data = json.dumps({
		"code": error.code,
		"name": error.name,
		# "description": error.description,
	})
	# Set the content type header to idicate JSON
	response.content_type = "application/json"
	return response

# For specific errors
# @app.errorhandler(405)
# def handle_error(error):
# 	return {
# 		"code": 405,
# 		"name": "Method Not Allowed"
# 	}, 405


# Ensures the Flask app runs only when executed in the main file and not when imported in some other file
# Runs the application on a local development server. Do not use run() in a production setting.
# if __name__ == '__main__':
# 	app.run()