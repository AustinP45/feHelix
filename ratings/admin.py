from django.contrib import admin
from .models import Tool
from .models import Category
from .models import ToolCat
from .models import Vote
admin.site.register(Tool)
admin.site.register(Category)
admin.site.register(ToolCat)
admin.site.register(Vote)
