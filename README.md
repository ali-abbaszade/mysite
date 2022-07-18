# Django Tutorial Project
## Installation
1. clone repo https://github.com/ali-abbaszade/mysite
2. create a virtual environment and activate
* pip install virtualenv
* python -m venv venv
* venv\Scripts\activate(Windows)
* source venv/bin/activate(Linux and Mac)
3. cd into project directory
4. pip install -r requirements.txt
5. Running the Project
* python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.dev (development settings)
* python manage.py runserver 0.0.0.0:8000 --settings=mysite.setting.prod (production settings)
