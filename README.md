# detectorover_webapp
webapp to display information about and control parts of the Detectorover

# environment variables;
-   DB_PASSWORD
-   SECRET_KEY

# local develop psql commands
-   windows pgadmin4 - psql 11

# virtualenv
-   environment name = env
-   command to activate on windows `.\env\Scripts\activate`
-   command to actvate on ubuntu `source bin/activate`

# requirements
-   do `pip3 freeze > requirements.txt` with venv activated only, to make sure no unnecessary modules are added.

# local dev mode
-   comment out `django_heroku.settings(locals())` in settings file