from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
  def test_url_exist_at_correct_location(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  def test_url_available_by_name(self):
    response = self.client.get(reverse('home'))

  def test_template_name_correct(self):
    response = self.client.get(reverse('home'))
    self.assertTemplateUsed(response, '<h1>Home Page</h1>')
    

class AboutPAgeTests(SimpleTestCase):
  def test_url_exists_at_correct_location(self):
    response = self.client.get('/about/')
    
    self.assertEqual(response.status_code, 200)

  def test_url_available_by_name(self):
    response = self.client.get(reverse('about'))

  def test_template_name_correct(self):
    response = self.client.get(reverse('about'))
    self.assertTemplateUsed(response, '<h1>About Page</h1>')