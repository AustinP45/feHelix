from django.db import models

class Tool(models.Model):
	name = models.CharField(max_length=30)
	desc =  models.TextField()
	link =  models.URLField(max_length=100)
	overall_score = models.DecimalField(max_digits=4, decimal_places=2)
	free = models.BooleanField(default=False)
	online = models.BooleanField(default=False)
	review_count = models.IntegerField()

class Category(models.Model):
	# Must be unique
	name = models.CharField(max_length=30,unique=True)
	# No length limit
	desc = models.TextField()
	
# For many-to-many relationship	
class ToolCat(models.Model):
	tool_id = models.ForeignKey(Tool)
	cat_id = models.ForeignKey(Category)
	
class Rating(models.Model):
	tool_id = models.ForeignKey(Tool)
	comment = models.TextField()
	reviewDate = models.DateField()
	overall_rating = models.PositiveSmallIntegerField()
	qual_of_doc = models.PositiveSmallIntegerField()
	efficacy = models.PositiveSmallIntegerField()
	usability = models.PositiveSmallIntegerField()