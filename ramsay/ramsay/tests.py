from django.test import TestCase
from ledger import models

# Create your tests here.

class ProjectTests(TestCase):
    # Test url linkage
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_visualpage(self):
        response = self.client.get('/visual/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_categoriespage(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)

    def test_profilepage(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_categorypage(self):
        cat = models.Category("Tools", "tools")
        response = self.client.get('/categories/Tools/')
        self.assertEqual(response.status_code, 200)

    def test_productpage(self):
        prod = models.Product("Hammer", "hammer", "Hammer of Thor", "https://google.com", "Steel", "10x10x10", "Somewhere", "wikipedia", "google.com", "description of somewhere", "CN", "toys produced in China", "Steel from China", "this is a fake hammer", "MIT", "https://opensource.org/licenses/MIT", "1000", "50", "40", "2", "1", "tools")
        response = self.client.get('/categories/Tools/awl/')
        self.assertEqual(response.status_code, 200)

    ''' testing absolute url
    def test_get_absolute_url(self):
        user = get_user_model().objects.create(username='some_user')
        entry = Ledger.objects.create(title="My entry title", author=user)
        self.assertIsNotNone(entry.get_absolute_url())
    
    def test_title_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.title)

    def test_body_in_entry(self):
        response = self.client.get(self.entry.get_absolute_url())
        self.assertContains(response, self.entry.body)
    '''

# TODO: test onclick behavior
# class ViewDetailTests(TestCase):
# Class AddItemTests(TestCase):
# Class ViewCartTests(TestCase):