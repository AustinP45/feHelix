from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=30, unique = True)
    desc =  models.TextField()
    link =  models.URLField(max_length=100)
    overall_rating = models.DecimalField(max_digits=4, decimal_places=3)
    qual_of_doc = models.DecimalField(max_digits=4, decimal_places=3)
    efficacy = models.DecimalField(max_digits=4, decimal_places=3)
    usability = models.DecimalField(max_digits=4, decimal_places=3)
    free = models.BooleanField(default=False)
    online = models.BooleanField(default=False)
    #review_count = models.IntegerField() #Not needed.

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True) # Must be unique
    desc = models.TextField()# No length limit

    def __str__(self):
        return self.name
	
# For many-to-many relationship	
class ToolCat(models.Model):
    tool_id = models.ForeignKey(Tool)
    cat_id = models.ForeignKey(Category)

    def __str__(self):
        return str(self.tool_id) + " in " + str(self.cat_id)
	
class Vote(models.Model):
    tool_id = models.ForeignKey(Tool)
    comment = models.TextField(blank = True)
    review_date = models.DateTimeField()
    overall_rating = models.PositiveSmallIntegerField()
    qual_of_doc = models.PositiveSmallIntegerField()
    efficacy = models.PositiveSmallIntegerField()
    usability = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.tool_id) + ' ' + str(self.overall_rating) + ' ' + str(self.review_date)
