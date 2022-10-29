# Simple backend app for Factored

Steps to run this project:

1. `python -m venv venv` to create the virtual environment
2. `./venv/Scripts/activate` to activate the virtual environment
3. `docker-compose up -d` to dockerize the project
4. `pip install -r requirements.txt` to install the dependencies
5. `uvicorn app.main:app` to run the app in the Uvicorn server