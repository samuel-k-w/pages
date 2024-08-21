# setting up project 

1. **pipenv install django==4.2**
2. to active virtual environment **pipenv shell**
3. **django-admin startproject django_project .**
4. **python manage.py startapp pages**
5. add to installed apps **pages.apps.PagesConfig**
6. **python manage.py migrate**

# Templates
- used for adding html files, we have to namespace it
1. inside pages app templates/pages/home.html
2. OR a project level template folder at root folder create templates/pages/home.html
3. update settings.py add **TEMPLATES = ['DIRS' : [BASE_DIR / 'templates']],**
4. templates useful when came to extending

# class based views
1. inside views **from django.views.generics import TemplateView** it have all logic needed
2. **class HomePageView(TemplateView):**
3. inside the class **template_name = 'hello.html'

# urls
1. add **urls.py** file inside pages app
2. add about page view as above and register to urls

# template inheritance
1. create **base.html** were parent html
2. inside base.html add required html file
3. add **{% block content %} {% endblock %}** which child templates inserted
4. inside about and home templates at first line add **{% extends 'base.html' %}**
5. inside child templates **{% block content %}<h1>About page</h1>{% endblock content %}**

# testing
- "Code without tests is broken as designed."
- there are unit and integration testing
- there are for test classes
  1. SimpleTestCase - no database needed
  2. TestCase - database used
  3. TransactionTestCase - test transactional cases
  4. LiveServerTestCase - to tst browser based test like selenium
1. **from django.test import SimpleTestCase**
2. **HomePagesTests(SimpleTestCase)**
3. **def test_url_exists_at_correct_location(self):**
4. add method validation **response = self.client.get("/about/") self.assertEqual(response.status_code, 200)**
5. **python manage.py test**


# Deployment Checklist
1. install Gunicorn - producton ready webserver for project **pipenv install gunicorn** uses wsgi.py
2. create requirements.txt
3. update **ALLOWED_HOSTS = ["*"]**
4. create Procfile
5. create runtime.txt