# Git-Github-Actions Learner/Django Template
# Django Template
This is the web app for the Django Template project.


# Some Coding Practices to Follow
Please try to ensure these standards whenever you are coding in Python.

- Module and file names should follow [snake casing](https://en.wikipedia.org/wiki/Snake_case).
- All variable and function names should also follow snake casing.
- Class names should follow [Pascal case](https://www.theserverside.com/definition/Pascal-case).
- Global variables or constants should be in all caps.

IMPORTANT: Please be vary of accidently pushing any credentials/secrets in the repo.


# Deployment
API is deployed using github actions, Be sure to change, app.yml , add right secrets into github repo

### CAUTION: Before deploying, make sure you have ```DEBUG=False``` in the .env file.

# Local Development Setup

1) After cloning the repo, create a virtual env by running this in the root directory:
   
   ```
   python -m venv .venv
   ```

2) Activate the virtual venv either by opening up a new terminal in VSCode (it will automatically activate) or run:
   
   ```
   .venv\\Scripts\\activate
   ```
   
   (change with forward-slash for linux)

3) Install dependencies:
   
   ```
   pip install -r requirements.txt
   ```
   
   Follow the guidelines in the other Django Template repos for installing our private packages.

4) SKIP: Place the ```.env``` file in the root directory (if you don't have this file, ask the repo owner)
   
   The .env file also has settings for the production Cloud SQL database. If you want to use that database, create a new variable named ```GAE_APPLICATION``` in the .env file and assign it the value 1 or True. Then in the ```DB_PORT``` variable, use the port number that the cloud_sql_proxy is listening on. [Here's](https://cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy) some help on cloud_sql_proxy and how to connect to the remote database. 

   
5) Now run these in the root:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
6) Finally run the server with:
   
   ```python manage.py runserver```

