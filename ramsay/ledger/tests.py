'''
To run tests: python3 manage.py test --settings=ramsay.settings.dev
If you get an error that says:
	Creating test database for alias 'default'...
	Got an error creating the test database: permission denied to create database
Do: psql ramsay
	ALTER USER admin CREATEDB;

That should fix it
'''

from django.test import TestCase
from .models import Citation


# Create your tests here.


class CitationTest(TestCase):
	def test_string_representation(self):
		author = "fake author"
		book = "fake book"
		pub = "fake publisher"
		#@ yu-lin, might need to initialize all or test will not run.
		citat = Citation(author, book, pub)  #(author="auth) 
		citat.save()
		self.assertEqual(author, citat.author)
		self.assertEqual(book, citat.book)
		self.assertEqual(pub, citat.publisher)
