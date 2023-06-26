# **TODOs REST API**
___


## Getting Started
To get started with the REST API, follow the instructions below:


### **Installation**
1. *Clone the repository:* 
```
git clone https://github.com/arist-create/rest-api-todo.git
```
2. *To launch the app - enter the command:*
```
docker-compose -f docker-compose.yaml up
```
3. *If you want to run tests - enter the command:*
```
docker-compose -f test-docker-compose.yaml up
```
4. *In order to get acquainted with the features, follow the link:*
```
http://127.0.0.1:8000/docs
```
### **API Endpoints**
The REST API provides the following endpoints:
____
**! ! ! Superuser is added:**
```
username: admin
password: admin
```
#### **POST /registration**
*Description: Create a new user.
Request body: JSON object with title and description fields.
Response: JSON object with a message field indicating success.*
#### **POST /authorization**
*Description: Authorized you.
Request body: Form with username and password fields.
Response: JSON object with a message field indicating success.*
#### **GET /tasks**
*Description: Retrieve a list of all tasks.
Response: JSON array of tasks.*
#### **GET /tasks/{task_id}**
*Description: Retrieve a specific task.
Response: JSON object representing the task.*
#### **POST /tasks**
*Description: Create a new task.
Request body: JSON object with title and description fields.
Response: JSON object representing the created task.*
#### **PATCH /tasks/{task_id}**
*Description: Update an existing task.
Request body: JSON object with title and description fields.
Response: JSON object representing the updated task.*
#### **DELETE /tasks/{task_id}**
*Description: Delete an existing task.
Response: JSON object with a message field indicating success.*
____
#### **POST /users**
*Description: Create a new user.
*Request body: JSON object with username and password fields.
Response: JSON object with a message field indicating success.*
#### **DELETE /users/{user_id}**
*Description: Delete an existing user.
Response: JSON object with a message field indicating success.*
