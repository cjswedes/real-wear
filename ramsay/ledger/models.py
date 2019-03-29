from django.db import models
from django.template.defaultfilters import slugify
class Citation(models.Model):

	author    = models.CharField(max_length=255)
	book      = models.CharField(max_length=255)
	publisher = models.CharField(max_length=255)

class Customer(models.Model):
	first_name = models.CharField(max_length=64)
	last_name  = models.CharField(max_length=64)

	occupation = models.CharField(max_length=64)


class Category(models.Model):
	name      = models.CharField(max_length=64, primary_key=True)
	name_slug = models.SlugField(unique=True, editable=False)
	def save(self, *args, **kwargs):
		self.name_slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

class Product(models.Model):
	title     = models.CharField(max_length=255)
	title_slug      = models.SlugField(max_length=255, primary_key=True, editable=False) #self
	
	artifact  = models.CharField(max_length=255) #artifact description
	image     = models.ImageField(upload_to='ledger', blank=True, null=True)

	materials = models.CharField(max_length=255 , blank=True, null=True)
	#dimensions =


	origin    = models.CharField(max_length=64, blank=True, null=True)
	collection = models.CharField(max_length=255, blank=True, null=True)
	link      = models.CharField(max_length=255)

	origin_description = models.TextField(blank=True, null=True)
	production_country = models.CharField(max_length=64, blank=True, null=True)
	production_detail  = models.CharField(max_length=128, blank=True, null=True)
	materials_location = models.CharField(max_length=64, blank=True, null=True)
	description        = models.TextField(blank=True, null=True)

	license   = models.CharField(max_length=64) #can limit to specific choices

	license_link = models.CharField(max_length=255)


	unit_number = models.IntegerField(default=0)
	unit_suffix = models.CharField(max_length=64, blank=True, null=True)

	original_price = models.IntegerField(default=0.0) #price in pence. adjust manually once taken
	#price_suffix = models.CharField(max_length=64) #can make this choices as well for the time?

	modern_pounds = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
	modern_dollars = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)

	page           = models.IntegerField(blank=True, null=True)


	#subcategory = models.CharField()

	categories      = models.ForeignKey(to=Category, related_name="products", on_delete=models.CASCADE)
	def save(self, *args, **kwargs):
		self.title_slug = slugify(self.title)
		super(Product, self).save(*args, **kwargs)
class Ledger(models.Model):

	#foreignkey from customer, called 'customer'
	#foreignkey from product, called 'product'

	#citation

	date      = models.DateTimeField(blank = True)
	analytics = models.TextField() #recorded analytic description in ledger

	citation = models.ManyToManyField(to=Citation, related_name='ledger_entries')#, on_delete=models.CASCADE)

	customer = models.ForeignKey(to=Customer, related_name="purchases", on_delete=models.CASCADE)
	product  = models.ForeignKey(to=Product, related_name="sales", on_delete=models.CASCADE)
	#thumb things in the excel??
