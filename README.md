Flask Microservice with SQLAlchemy
============================================

This project demonstrates a simple CRUD (Create, Read, Update, Delete) microservice built with Flask and SQLAlchemy. It includes endpoints for managing user data stored in an SQLite database. The service supports the following HTTP methods: GET, POST, PUT, and DELETE.

### Features

GET: Retrieve all users or a specific user by ID.
POST: Create a new user.
PUT: Update an existing user's information.
DELETE: Delete a user by ID.
Uses SQLAlchemy for database operations.
Simple and lightweight, perfect for learning RESTful APIs.
Prerequisites
Python: Ensure Python 3.7 or higher is installed.
Flask: A microframework for building web applications.
Postman: (Optional) for testing API endpoints.

### Setup Instructions

Install Dependencies: Create and activate a virtual environment (optional but recommended):

python -m venv myenv
myenv\Scripts\activate    # Windows
Install the required packages:

pip install flask flask-sqlalchemy
Run the Application:

python app.py
The service will start on ******************.

### Endpoints

### 1. Retrieve All Users

Method: GET
URL: /users
### Response:
json
[
    {"id": 1, "name": "John Doe", "age": 25},
    {"id": 2, "name": "Jane Smith", "age": 30}
]
### 2. Retrieve a User by ID

Method: GET
URL: /users/<user_id>
Example: /users/1
### Response:
json
{"id": 1, "name": "John Doe", "age": 25}

### 3. Create a New User

Method: POST
URL: /users
Body (JSON):
{
    "name": "Alice Johnson",
    "age": 27
}
### Response:

json
{"id": 3, "name": "Alice Johnson", "age": 27}

### 4. Update a User

Method: PUT
URL: /users/<user_id>
Example: /users/1
Body (JSON):
json
{
    "name": "John Updated",
    "age": 26
}
### Response:
json
{"id": 1, "name": "John Updated", "age": 26}

### 5. Delete a User
Method: DELETE
URL: /users/<user_id>
Example: /users/1
### Response:
json
{"message": "User deleted"}

### Database
The database is an SQLite file named users.db.
The User table schema:
id: Integer (Primary Key)
name: String (Required)
age: Integer (Required)
To customize for other databases (e.g., MySQL, MongoDB), update the SQLALCHEMY_DATABASE_URI configuration.

### Testing with Postman
Open Postman and create a new request.
Use the appropriate HTTP method (GET, POST, PUT, DELETE).
Enter the URL and body (if needed).
Send the request and inspect the response.
Notes
This application is in development mode (debug=True). For production, disable debug mode and use a production-ready server like Gunicorn.
To reset the database, delete the users.db file and restart the application.

### License
This project is open-source and licensed under the MIT License. Feel free to modify and use it as needed.