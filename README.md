# busycal
Combining subscribable iCals to publish a public iCal for yourself that respects your privacy settings

## Install

Create virtualenv and activate it:

```sh
# MacOS & Linux

$ python3 -m venv venv
$ . venv/bin/activate
```
```sh
# Windows Powershell

> python3 -m venv venv
> venv\Scripts\activate.bat
```

Install dependancies within the virtualenv

```
$ pip install flask
```

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