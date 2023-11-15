# About

Flask app to manage contacts with a simple to use API

This project was made as part of the Kodemia bootcamp for learning Backend and Cloud Technologies with Python and AWS

You can read the description of the project in the file `instructions.md`

# Getting started

Firstly activate your virtual python envrionment

## Tech requirements

- Python v3+
- PostgreSQL 16+

## Create your virtual environments

### 1. Create your virtual environment

With Venv:

```python

python -m venv ./.venv

```

With pyenv:

```python

pip install pyenv


# Install your desired python version with...

pyenv install YOUR_DESIRED_PYTHON_VERSION

# Create your virtual environment with the new version you installed

pyenv virtualenv YOUR_INSTALLED_PYTHON_VERSION THE_NAME_OF_YOUR_APP

# Please notice that this folder will be created at your pyenv installation dir

```

### 2. Activate your virtual environemtn

With Venv:

```python

source ./.venv/bin/activate

```

With pyenv:

```python
pyenv activate THE_NAME_OF_YOUR_APP
```

## Install required dependencies

Once your virtual environment is active, you can install pip dependencies on it

### Install current dependencies

```python

pip install -r requirements.txt

```

### Update requirements.txt every time you install a new package

```python

pip install my_super_awesome_package

# Update requirements.txt

pip freeze > requirements.txt

```

## Create your .env file with the .env.example format

```shell
cp .env.example .env \
# Or your favorite text/code editor of your preference
vi .env
```

## Initialize your flask server

```python

 flask --app __init__  run --debug

```

# CODE AS YOU MEAN IT

# [Postman Test](https://www.postman.com/irfdev/workspace/pygenda/globals)
