"""
Import django modules.
"""
from django.db import models

class Tool(models.Model):
    """
    Tool class
    """
    name = models.CharField(max_length=30, unique = True)
    desc =  models.TextField()
    link =  models.URLField(max_length=100)
    overall_rating = models.DecimalField(max_digits=4, decimal_places=3)
    qual_of_doc = models.DecimalField(max_digits=4, decimal_places=3)
    efficacy = models.DecimalField(max_digits=4, decimal_places=3)
    usability = models.DecimalField(max_digits=4, decimal_places=3)
    free = models.BooleanField(default=False)
    online = models.BooleanField(default=False)

    # string method
    def __str__(self):
        return self.name

class Category(models.Model):
    """
    Category class
    """
    name = models.CharField(max_length=30, unique=True) # Must be unique
    desc = models.TextField()# No length limit

    # string method
    def __str__(self):
        return self.name
	
# Tool-Category class (many-to-many relationship)	
class ToolCat(models.Model):
    """
    Tool class
    """
    tool_id = models.ForeignKey(Tool)
    cat_id = models.ForeignKey(Category)

    # string method
    def __str__(self):
        return str(self.tool_id) + " in " + str(self.cat_id)

class Vote(models.Model):
    """
    Vote model
    """
    tool_id = models.ForeignKey(Tool)
    comment = models.TextField(blank = True)
    review_date = models.DateTimeField()
    overall_rating = models.PositiveSmallIntegerField()
    qual_of_doc = models.PositiveSmallIntegerField()
    efficacy = models.PositiveSmallIntegerField()
    usability = models.PositiveSmallIntegerField()

    # string method
    def __str__(self):
        return str(self.tool_id) + ' ' + str(self.overall_rating) + ' ' \
            + str(self.review_date)
