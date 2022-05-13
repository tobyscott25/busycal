# busycal
Combine subscribe-able calendars to publish a public calendar of your own that respects your privacy

## Install

### 1. Create virtualenv (if you haven't already)
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

### 3. Install dependancies within the virtualenv (if you haven't already)

```
$ pip install flask
$ pip install python-dotenv
$ pip install ics
$ pip install requests
```

### 4. Create `.env` file (if you haven't already)

- Duplicate `.env.example` and rename copy to `.env`
- Make changes to `.env` as required



## Run the Development Server

```sh
$ flask run
```


## Usage

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