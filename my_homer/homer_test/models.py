from django.db import models

# Create your models here.
class person(models.Model):
	name 	= models.CharField(max_length=100)
	DOB 	= models.DatetimeField(null=True, blank=True)

	def __unicode__(self):
		return self.name


