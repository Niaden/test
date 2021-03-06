from django.db import models


## Create your models here.
class Item (models.Model):
	class Meta():
		db_table = 'Item'
	item_name = models.CharField(max_length = 200)
	item_number = models.IntegerField(default=1)
	item_unit_measure = models.CharField(max_length = 20)

	def __unicode__(self):
		return "{} - {} {}".format(self.item_name, self.item_number, self.item_unit_measure)
