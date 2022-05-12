from flask import Flask, jsonify, abort
import json

# Create an instance of the class
app = Flask(__name__)


@app.route('/<string:name>/')
def hello(name):

	out = "Hello " + name
	# Return response in JSON format with status code 200
	return jsonify(out), 200


# Ensures the Flask app runs only when executed in the main file and not when imported in some other file
# Runs the application on a local development server. Do not use run() in a production setting.
# if __name__ == '__main__':
# 	app.run()