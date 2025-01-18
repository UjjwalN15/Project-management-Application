User Endpoints
POST /users/register: Register a new user.
POST /users/login: Authenticate a user and retrieve a token.
POST /users/logout: Logout the user by deleting their token.
GET /users/: List all users (Admin only).
GET /users/id: Retrieve a specific user's details.
PUT /users/id: Update a specific user's details.
PATCH /users/id: Partially update a specific user's details.
DELETE /users/id: Delete a user (Admin only).



Project Endpoints
GET /projects/: List all projects.
POST /projects/: Create a new project.
GET /projects/id: Retrieve details of a specific project.
PUT /projects/id: Update details of a specific project.
PATCH /projects/id: Partially update a specific project.
DELETE /projects/id: Delete a specific project.




Task Endpoints
GET /projects/id/tasks: List all tasks under a specific project.
POST /projects/id/tasks: Create a new task under a specific project.
GET /tasks/id: Retrieve details of a specific task.
PUT /tasks/id: Update details of a specific task.
PATCH /tasks/id: Partially update a specific task.
DELETE /tasks/id: Delete a specific task.




Comment Endpoints
GET /tasks/id/comments: List all comments under a specific task.
POST /tasks/id/comments: Add a new comment to a specific task.
GET /comments/id: Retrieve details of a specific comment.
PUT /comments/id: Update details of a specific comment.
PATCH /comments/id: Partially update a specific comment.
DELETE /comments/id: Delete a specific comment.

Steps to set up a project locally:
1. Start a project
   ( django-admin startproject project_name )
2. Create a virtual env
   ( virtualenv env_name)
3. Create a app
   ( python manage.py startapp base )
4. Install the requirements.txt
   ( pip install -r requirements.txt )
5. Create Models Views and serializers as well as other files
   (Or you can copy them from above)
6. Makemigrations and migrate
   ( python manage.py makemigrations )
   ( python manage.py migrate )
7. Run the server
   ( python manage.py runserver)
8. Create a endpoints in Postman
9. Test the endpoints
