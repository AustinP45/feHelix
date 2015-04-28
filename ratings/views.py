# Pretty good chance having two categories or tools with same names or spaces in place of underscores will cause problems.

from django.shortcuts import get_object_or_404, redirect, render
#from django.http import HttpResponseRedirect
import datetime

from ratings.forms import VoteForm
from ratings.models import Category
from ratings.models import Tool
from ratings.models import ToolCat
from ratings.models import Vote

from ratings.forms import VoteForm

# Create your views here.
def home(request):
    newvotes = Vote.objects.all().order_by('-review_date')[:5]
    return render(request, 'ratings/home.html', {'newvotes': newvotes})

def categorys_list(request):
    categorys = Category.objects.all()
    return render(request, 'ratings/categorys_list.html', {'categorys': categorys})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    tools = Tool.objects.filter(toolcat__cat_id = category)
    return render(request, 'ratings/category_detail.html', {'category': category, 'tools': tools})
    
def category_detail_by_name(request, cat_name):
    category = get_object_or_404(Category, name = cat_name.replace('_', ' '))
    return category_detail(request, category.id)

def tool_detail_by_name(request, tool_name):
    tool = get_object_or_404(Tool, name = tool_name.replace('_', ' '))
    return tool_detail(request, tool.id)
    
def tool_detail(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    votes = Vote.objects.filter(tool_id = tool)
    
    if request.method == "POST":
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit = False)
            vote.tool_id = tool
            vote.review_date = datetime.datetime.now()
            if (votes.count == 0):
                tool.overall_rating = vote.overall_rating
                tool.qual_of_doc = vote.qual_of_doc
                tool.efficacy = vote.efficacy
                tool.usability = vote.usability
            else:
                tool.overall_rating = (tool.overall_rating * votes.count() + vote.overall_rating) / (votes.count() + 1)
                tool.qual_of_doc = (tool.qual_of_doc * votes.count() + vote.qual_of_doc) / (votes.count() + 1)
                tool.efficacy = (tool.efficacy * votes.count() + vote.efficacy) / (votes.count() + 1)
                tool.usability = (tool.usability * votes.count() + vote.usability) / (votes.count() + 1)
            tool.save()
            vote.save()
            
        return redirect('.', pk = pk) # Redirects to same page.
    else:
        form = VoteForm()
        return render(request, 'ratings/tool_detail.html', {'tool': tool, 'votes': votes, 'form': form})

