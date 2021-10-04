# DataBash

**WHAT IT DOES**
Databash is a streamlined machine learning data collection platform.it aims to allow user to build machine learning datasets collaboratively and easily, so they can focus on the important parts of their project instead of having to get bogged down in trying to gather data.


1. Fork the repo
2. Clone the github repo onto your machine.
3. Rename the .env.example to .env which should include ```DEBUG=True``` and SECRET_KEY
4. Go to https://djecrety.ir/, create a secret key and paste it in the .env file
5. Install the pip packages: run ```pip install -r requirements.txt```
6. Make migrations: run ```python manage.py migrate```
7. Run the django server: ```python manage.py runserver```

