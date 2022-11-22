## Getting Started
Clone this repository in the wanted directory:
> git clone https://github.com/FredPerr/django-vue-template.git [project_name]

Create a Python virtual environment with the dependencies:

_(In the root folder of the app)_
> python -m venv venv/

Activate the environment
Unix:
> venv/Scripts/activate
Windows:
> venv/Scripts/Activate.ps1

Install the requirements
> pip install -r requirements.txt


Setup the database authentication credentials:

_(In settings.py in the python backend:)_
Change the database name, port if needed.
Then, **ADD TWO ENVIRONMENT VARIABLES: DB_USER (user of the database) and DB_PASSWORD (password of the user accessing the database)**.

Make sure to **create the database and use the correct password and username** setup in the database manager.
