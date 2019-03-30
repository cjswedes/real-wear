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
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Citation, Customer, Category, Product, Ledger
import os

# Create your tests here.


class CitationTest(TestCase):
	def test_string_representation(self):
		at= "fake author"
		bk = "fake book"
		pub = "fake publisher"
		citat = Citation.objects.create(author=at, book=bk, publisher=pub) 
		self.assertEqual(at, citat.author)
		self.assertEqual(bk, citat.book)
		self.assertEqual(pub, citat.publisher)

class CustomerTest(TestCase):
	def test_string_representation(self):
		fn = "firstname"
		ln = "lastname"
		oc = "fake job"
		cust = Customer.objects.create(first_name=fn, last_name=ln, occupation=oc) 
		self.assertEqual(fn, cust.first_name)
		self.assertEqual(ln, cust.last_name)
		self.assertEqual(oc, cust.occupation)

class CategoryTest(TestCase):
	def test_string_representation(self):
		nm = "Tools"
		slg = "tools"
		cat = Category.objects.create(name=nm, name_slug=slg)
		self.assertEqual(nm, cat.name)
		self.assertEqual(slg, cat.name_slug)

prod = None

class ProductTest(TestCase):
	def test_string_representation(self):
		global prod
		ttle = "Hammer"
		tslg = "hammer"
		art = "fake artifact"
		# img = SimpleUploadedFile(name='Home.jpg', content=open(os.getcwd()+"/static/images/", 'rb').read(), content_type='image/jpeg')
		mat = "fake material"
		dim = "10x10x10"
		orig = "fake origin"
		col = "fake collection"
		lnk = "fake link"
		origdesc = "orign descript"
		prodctry = "fake production country"
		proddetl = "fake production detail"
		matloc = "fake material location"
		desc = "fake description"
		lic = "fake license"
		liclnk = "https://google.com"
		origprc = "5"
		modpd = "1.23"
		moddol = "4.56"
		pg = "30"
		qty = "123"
		cat = Category.objects.create(name="Tools", name_slug="tools")


		prod = Product.objects.create(
			title=ttle, title_slug=tslg, artifact=art, #image=img,
			materials=mat, dimensions=dim, origin=orig, collection=col,
			link=lnk, origin_description=origdesc, production_country=prodctry,
			production_detail=proddetl, materials_location=matloc, 
			description=desc, license=lic, license_link=liclnk, original_price=origprc,
			modern_pounds=modpd, modern_dollars=moddol, page=pg, quantity=qty,
			category=cat )
			
		self.assertEqual(ttle, prod.title)
		self.assertEqual(tslg, prod.title_slug)
		self.assertEqual(art, prod.artifact)
		# self.assertEqual(img, prod.image)
		self.assertEqual(mat, prod.materials)
		self.assertEqual(dim, prod.dimensions)
		self.assertEqual(orig, prod.origin)
		self.assertEqual(col, prod.collection)
		self.assertEqual(lnk, prod.link)
		self.assertEqual(origdesc, prod.origin_description)
		self.assertEqual(prodctry, prod.production_country)
		self.assertEqual(proddetl, prod.production_detail)
		self.assertEqual(matloc, prod.materials_location)
		self.assertEqual(desc, prod.description)
		self.assertEqual(lic, prod.license)
		self.assertEqual(liclnk, prod.license_link)
		self.assertEqual(origprc, prod.original_price)
		self.assertEqual(modpd, prod.modern_pounds)
		self.assertEqual(moddol, prod.modern_dollars)
		self.assertEqual(pg, prod.page)
		self.assertEqual(qty, prod.quantity)
		self.assertEqual(cat, prod.category)
		

class LedgerTest(TestCase):
	def test_string_representation(self):
		dt="2018"
		ana="fake analytics"
		citat = Citation.objects.create(author="author", book="book", publisher="publisher") 
		cust = Customer.objects.create(first_name="firtname", last_name="lastname", occupation="job") 
		prod = Product.objects.create(category=Category.objects.create(name="Tools", name_slug="tools")
)

		lgr = Ledger.objects.create(date=dt, analytics=ana, citation=citat,
							customer=cust, product=prod)

		self.assertEqual(dt, lgr.date)
		self.assertEqual(ana, lgr.analytics)
		self.assertEqual(citat, lgr.citation)
		self.assertEqual(cust, lgr.customer)
		self.assertEqual(prod, lgr.product)