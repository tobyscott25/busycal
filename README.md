# busycal
Combining subscribable iCals to publish a public iCal for yourself that respects your privacy settings

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
```

### 4. Create `.env` file

- Duplicate `.env.example` and rename copy to `.env`
- Make changes to `.env` as required



## Run the Development Server

```sh
# MacOS & Linux

$ export FLASK_APP=main
$ flask run
```

```sh
# Windows Powershell

> $env:FLASK_APP = "main"
> flask run
```