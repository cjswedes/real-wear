from django.db import models


class Citation(models.Model):

	author    = models.CharField(max_length=255)
	book      = models.CharField(max_length=255)
	publisher = models.CharField(max_length=255)


class Ledger(models.Model):
	slug      = models.SlugField(max_length=255) #self
	title     = models.CharField(max_length=255) 
	artifact  = models.CharField(max_length=255) #artifact description
	image     = models.ImageField(upload_to='ledger')

	materials = models.CharField(max_length=255)
	#dimensions = 

	date      = models.DateTimeField(blank = True)
	origin    = models.CharField(max_length=64)
	collection = models.CharField(max_length=255)
	link      = models.CharField(max_length=255)

	license   = models.CharField(max_length=64) #can limit to specific choices

	license_link = models.CharField(max_length=255)

	#ledger file name -- not used
	DEPARTMENTS = ("agriculture", "tools", "textiles")
	DEPARTMENT_CHOICES = ( for index, item in enumerate(DEPARTMENTS) (index, item) )

	department   = models.CharField(choices=DEPARTMENT_CHOICES, default=DEPARTMENTS[1])

	customer_first = models.CharField(max_length=64)
	customer_last  = models.CharField(max_length=64)
	page           = models.IntegerField()

	origin_description = models.TextField()
	production_country = models.CharField(max_length=64, blank=True)
	production_detail  = models.CharField(max_length=128, blank=True)
	materials_location = models.CharField(max_length=64, blank=True)
	description        = models.TextField()

	#citation
	citation = models.ManyToManyField(to=Citation, related_name='ledger_entries', on_delete=models.CASCADE)

	unit_number = models.IntegerField()
	unit_suffix = models.CharField(max_length=64)

	original_price = models.IntegerField(default=0.0) #price in pence. adjust manually once taken
	#price_suffix = models.CharField(max_length=64) #can make this choices as well for the time?

	modern_pounds = models.DecimalField(decimal_places=2)
	modern_dollars = models.DecimalField(decimal_places=2)

	analytics = models.TextField()

	#thumb things in the excel??



