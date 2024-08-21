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

# class based views
1. inside views **from django.views.generics import TemplateView** it have all logic needed
2. **class HomePageView(TemplateView):**
3. inside the class **template_name = 'hello.html'

# urls
1. add **urls.py** file inside pages app
2. add about page view as above and register to urls