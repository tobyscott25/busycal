# Python (Flask) REST API

## Installation

### 1. Create virtualenv
```sh
$ python3 -m venv venv
```

### 2. Activate the virtualenv

```sh
# MacOS & Linux
$ . venv/bin/activate
```
```sh
# Windows Powershell
> venv\Scripts\activate
```

### 3. Install pip dependancies within the virtualenv

```
$ pip install flask python-dotenv ics requests
```

### 4. Create `.env` file

- Duplicate `.env.example` and rename copy to `.env`
- Make changes to `.env` as required



## Starting the Development Server

### 1. Activate the virtualenv

```sh
# MacOS & Linux
$ . venv/bin/activate
```
```sh
# Windows Powershell
> venv\Scripts\activate
```

### 2. Start the Flask development server

```sh
$ flask run
```


## Usage Instructions

Send a HTTP `POST` request to the flask development server (usually `http://localhost:5000`)

Required headers:
```
Content-Type: application/json
```
JSON body data
```json
[
	"first_ics_url",
	"second_ics_url",
	// add as many as you like ...
]
```

You will get a response with the combined following header 

```
Content-Type: text/calendar
```

Enjoy!