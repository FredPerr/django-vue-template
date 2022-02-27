## Getting Started
Clone this repository in the wanted directory:
> git clone https://github.com/FredPerr/django-vue-template.git [project_name]

Create a Python virtual environment with the dependencies:

_(In the root folder of the fullstack app)_
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


## Tips for development

Some software are useful when developping an an using an API. To test request that will be made between the frontend and backend. You can use [Postman](https://www.postman.com/downloads/).

Additionally, the django backend uses [PostgreSQL](https://www.postgresql.org/download/) by default, and not SQLite3 as django initially configure. <i>You might want ot use pgAdmin (provided by PostgreSQL) to view and test the database.</i> The default configuration can be changed in the _settings.py_ of the django project.