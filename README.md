# Backend Workshop
In this workshop we go over AWS and Python Flask. The slides can be found [here](https://docs.google.com/presentation/d/1u0lOjvQeCHM8IaPHoUb6EpbC5hCHY9Cb6YfZYXOzC_U/edit?usp=sharing)

## Installation
First clone the repository and open it in the terminal.

Assuming you already have Python 3 installed. The first thing you need to do is download Flask, Flask SQLAlchemy, dotenv and psycopg2-binary for making this application run as follows:
```
pip3 install Flask Flask-SQLAlchemy dotenv psycopg2-binary
```

You will have to set up a database by yourself. Once that is done follow the next steps.

We need to set up the .env file which will be used to connect the database to flask.

1. Create a .env file in the main directory
```
touch .env
```

2. Edit .env file and put in the variable you need to setup the database such as username, password, etc.

For example:
```
HOST=124.256.289.10
USERNAME=google
PASSWORD=alexa
```

### Why we use .env?
Since we do not want to put our credentials online for anyone to see. We create a .env file which containes these information for us. This .env file is added to .gitignore file so that any changes to this file is not registered by git.

## Running the application
To run the API we need to run the API file with python3 as shown:
```
python3 ./src/api.py
```

## Endpoints
```
GET /api/article
```
```
GET /api/article/:id
```
```
POST /api/article

Expected Type: raw JSON

Expected Data: {
    'title': 'Welcome to GDSC',
    'author': 'gdscutm',
    'body': 'Lists of workshop'
}
```
```
PUT /api/article/:id

Expected Type: raw JSON

Expected Data: {
    'title': 'Welcome to UTMGDSC'
}
```