linkedin_connections
====================

Collect all your linkedin collections

1) clone the repo 

	$ git clone https://github.com/sparkajai/linkedin_connections.git

2) install the requirements

	$ pip install -r requirements.txt

3) run syncdb

	$ python manage.py syncdb

4) run the server 

	$ python manage.py runserver

click on the register link to register a new user or register using linkedin, 

after logging in all your connections will be displayed and you may edit their names and save into the database.

5) access url /linkedin/ to view the rest API data.
