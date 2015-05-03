from django.test import TestCase
from django.test import Client

def create_category(cat_name, cat_desc):
	"""
	Create a new category with given name and description
	"""
	return Category.models.create(name=cat_name, desc=cat_desc)

class QuestionViewTests(TestCase):
    def test_index_view(self):
		"""
        Ensure we get a response from the index
        """
        response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
	
	def test_categories_view(self):
		"""
        Ensure we get a response from the index
        """
		response = self.client.get('/categories')
		self.assertEqual(response.status_code, 200)
		
