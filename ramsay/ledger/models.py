from django.db import models


class Citation(models.Model):

	author    = models.CharField(max_length=255)
	book      = models.CharField(max_length=255)
	publisher = models.CharField(max_length=255)

class Ledger(models.Model):

	#foreignkey from customer, called 'customer'
	#foreignkey from product, called 'product'

	#citation

	date      = models.DateTimeField(blank = True)
	analytics = models.TextField() #recorded analytic description in ledger

	citation = models.ManyToManyField(to=Citation, related_name='ledger_entries')#, on_delete=models.CASCADE)


	#thumb things in the excel??

class Product(models.Model):
	slug      = models.SlugField(max_length=255) #self
	title     = models.CharField(max_length=255) 
	artifact  = models.CharField(max_length=255) #artifact description
	image     = models.ImageField(upload_to='ledger')

	materials = models.CharField(max_length=255)
	#dimensions = 

	
	origin    = models.CharField(max_length=64)
	collection = models.CharField(max_length=255)
	link      = models.CharField(max_length=255)

	origin_description = models.TextField()
	production_country = models.CharField(max_length=64, blank=True)
	production_detail  = models.CharField(max_length=128, blank=True)
	materials_location = models.CharField(max_length=64, blank=True)
	description        = models.TextField()

	license   = models.CharField(max_length=64) #can limit to specific choices

	license_link = models.CharField(max_length=255)


	unit_number = models.IntegerField()
	unit_suffix = models.CharField(max_length=64)

	original_price = models.IntegerField(default=0.0) #price in pence. adjust manually once taken
	#price_suffix = models.CharField(max_length=64) #can make this choices as well for the time?

	modern_pounds = models.DecimalField(max_digits=10, decimal_places=2)
	modern_dollars = models.DecimalField(max_digits=10, decimal_places=2)

	page           = models.IntegerField()

	sales = models.ForeignKey(to=Ledger, related_name="product", on_delete=models.CASCADE)


class Department(models.Model):
	DEPARTMENTS = ("agriculture", "tools", "textiles")
	DEPARTMENT_CHOICES = ( (index, item) for index, item in enumerate(DEPARTMENTS))
	department  = models.IntegerField(choices=DEPARTMENT_CHOICES, default=DEPARTMENTS[1])

	products = models.ForeignKey(to=Product, related_name="department", on_delete=models.CASCADE)

class Customer(models.Model):
	first_name = models.CharField(max_length=64)
	last_name  = models.CharField(max_length=64)

	occupation = models.CharField(max_length=64) 

	purchases  = models.ForeignKey(to=Ledger, related_name="customer", on_delete=models.CASCADE)


