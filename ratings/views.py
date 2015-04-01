from django.shortcuts import render, get_object_or_404
from ratings.models import Category
from ratings.models import Tool
from ratings.models import ToolCat
from ratings.models import Vote

# Create your views here.
def categorys_list(request):
    categorys = Category.objects.all()
    return render(request, 'ratings/categorys_list.html', {'categorys': categorys})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    tools = Tool.objects.filter(toolcat__cat_id = category)
    return render(
        request,
        'ratings/category_detail.html',
        {'category': category, 'tools': tools})

def tool_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    votes = Vote.objects.filter(tool_id = tool)
    return render(
            request, 
            'ratings/tool_detail.html', 
            {'tool': tool, 'votes': votes})
