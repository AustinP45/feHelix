from django import forms
from .models import Vote
from .models import Category
from .models import Tool
from django.utils.safestring import mark_safe

class HorizRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class HorizRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
        fields = ('overall_rating', 'qual_of_doc', 'efficacy', 'usability', 'comment')
        widgets = {
            'overall_rating': forms.RadioSelect(renderer = HorizRadioRenderer, choices = CHOICES), 
            'qual_of_doc': forms.RadioSelect(renderer = HorizRadioRenderer, choices = CHOICES), 
            'efficacy': forms.RadioSelect(renderer = HorizRadioRenderer, choices = CHOICES), 
            'usability': forms.RadioSelect(renderer = HorizRadioRenderer, choices = CHOICES),
            'comment': forms.Textarea(attrs={'cols': 35, 'rows': 3})}
        labels = {
            'overall_rating': "Overall Rating", 'qual_of_doc': "Quality of Documentation",
            'efficacy': "Efficacy", 'usability': "Usability", 'comment': "Optional Comments:"}
            
class CategoryNominationForm(forms.ModelForm):
    nominator_name = forms.CharField(max_length=30)
    nominator_email = forms.EmailField(max_length=30)
    class Meta:
        model = Category
        fields = ('name', 'desc', 'nominator_name', 'nominator_email')
        widgets = {'desc': forms.Textarea(attrs={'cols': 35, 'rows': 3})}
        labels = {'name': "Category Name", 'desc': "Category Description", 'nominator_name': "Your Name", 'nominator_email': "Your email", 'free': "Is the tool free to use?&nbsp", 'online': "Is the tool web-based?&nbsp"}
        
        
class ToolNominationForm(forms.ModelForm):
    category = forms.CharField(max_length=100)
    nominator_name = forms.CharField(max_length=30)
    nominator_email = forms.EmailField(max_length=30)
    class Meta:
        model = Tool
        link = forms.CharField(max_length=100)
        fields = ('name', 'desc', 'link', 'free', 'online', 'category', 'nominator_name', 'nominator_email')
        widgets = {'desc': forms.Textarea(attrs={'cols': 35, 'rows': 3})}
        labels = {'name': "Tool Name", 'desc': "Tool Description", 'nominator_name': "Your Name", 'nominator_email': "Your email", 'link': "Link to tool home page:"}