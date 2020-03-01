# AutoReport-Maker-Sender
Run a query in python to have it automatically generate a .csv report and send it to a specific email with some content.

This script runs a SQL query on an online database, creates a csv file and automatically sends it to an email from a specific email address.
It also creates a unique id for the reports based on the date and the library uuid

Notes: 
- The email address has to have a SMTP server enabled with their provider.
- Python does not automatically come with a library to communicate with MySQL, so the mysql library must be installed using pip.


**Steps
- Add to environment_variables.py the user and receiver information, as well as the database access login.
- Run sales_report.py
