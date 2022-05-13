# busycal
Combine subscribe-able calendars to publish a public calendar of your own that respects your privacy

## Getting up and running

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
```

### 4. Create `.env` file (if you haven't already)

- Duplicate `.env.example` and rename copy to `.env`
- Make changes to `.env` as required



## Run the Development Server

```sh
$ flask run
```