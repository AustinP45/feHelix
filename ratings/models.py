from django.db import models

class Tool(models.Model):
	name = 
	desc = 
	link = 
	overall_score = 
	free = 
	online = 
	review_count = 

class Category(models.Model):
	name = 
	desc = 
	
class ToolCat(models.Model):
	tool_id = models.ForeignKey(Tool)
	cat_id = models.ForeignKey(Category)
	
class Rating(models.Model):
	tool_id = models.ForeignKey(Tool)
	comment = 
	overall_rating = 
	qual_of_doc = 
	efficacy = 
	usability = 