from django.test import TestCase

# Create your tests here.

class ProjectTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
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