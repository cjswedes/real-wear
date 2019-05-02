from django.db import models
from django.template.defaultfilters import slugify
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()


#TODO: decide lengths for efficiency in storage
class Citation(models.Model):
	author = models.CharField(max_length=255)
	book = models.CharField(max_length=255)
	publisher = models.CharField(max_length=255)

class Customer(models.Model):
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	occupation = models.CharField(max_length=64, null=True, blank=True)

class Category(models.Model):
	name      = models.CharField(max_length=64, primary_key=True)
	name_slug = models.SlugField(unique=True, editable=False)
	def save(self, *args, **kwargs):
		self.name_slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

class Product(models.Model):
  #primary key is automatically generated by django when we dont specify it, but we specify title_slug since products should have unique titles
	title     = models.CharField(max_length=255)
	title_slug      = models.SlugField(max_length=255, primary_key=True, editable=False) #self
	
	artifact  = models.CharField(max_length=255) #artifact description
	image     = models.ImageField(storage=fs, blank=True, null=True)

	materials = models.CharField(max_length=255 , blank=True, null=True)
	dimensions = models.CharField(max_length=255, blank=True, null=True)



	#origin    = models.CharField(max_length=64, blank=True, null=True) deleted by morgan
	collection = models.CharField(max_length=255, blank=True, null=True)
	link       = models.CharField(max_length=255, blank=True, null=True)


	origin_description   = models.TextField(blank=True, null=True)
	production_country   = models.CharField(max_length=64, blank=True, null=True)
	production_city      = models.CharField(max_length=64, blank=True, null=True)
	production_longitude = models.DecimalField(max_digits=7, decimal_places=4, default=0.0, blank=True, null=True) #east is positive
	production_latitude  = models.DecimalField(max_digits=6, decimal_places=4, default=0.0, blank=True, null=True)  #north is positive
	#production_detail    = models.CharField(max_length=128, blank=True, null=True)
	materials_country    = models.CharField(max_length=64, blank=True, null=True)
	materials_longitude  = models.DecimalField(max_digits=7, decimal_places=4, default=0.0, blank=True, null=True) #east is positive
	materials_latitude   = models.DecimalField(max_digits=6, decimal_places=4, default=0.0, blank=True, null=True)  #north is positive
	description          = models.TextField(blank=True, null=True)

	license   = models.CharField(max_length=64, blank=True, null=True) #can limit to specific choices

	license_link = models.CharField(max_length=255, blank=True, null=True)


	#unit_number = models.IntegerField(default=0)
	#unit_suffix = models.CharField(max_length=64, blank=True, null=True)

	# original_price = models.IntegerField(default=0.0) #price in pence. adjust manually once taken
	original_price = models.CharField(max_length=64)
	#price_suffix = models.CharField(max_length=64) #can make this choices as well for the time?

	modern_pounds = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
	modern_dollars = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)

	# TODO: is page a part of a product or a ledger entry?
	page           = models.IntegerField(blank=True, null=True)

	quantity = models.CharField(max_length=64, blank=True, null=True)

	#subcategory = models.CharField()

	category      = models.ForeignKey(to=Category, related_name="products", on_delete=models.CASCADE)
	def save(self, *args, **kwargs):
		self.title_slug = slugify(self.title)
		super(Product, self).save(*args, **kwargs)

class Ledger(models.Model):

	#foreignkey from customer, called 'customer'
	#foreignkey from product, called 'product'

	#citation
	date      = models.CharField(max_length=64, blank = True)
	analytics = models.TextField() #recorded analytic description in ledger

	citation = models.ForeignKey(to=Citation, related_name='ledger_entries', on_delete=models.CASCADE, null=True)

	customer = models.ForeignKey(to=Customer, related_name="purchases",on_delete=models.CASCADE)
	product  = models.ForeignKey(to=Product, related_name="sales", on_delete=models.CASCADE)
	#thumb things in the excel??
