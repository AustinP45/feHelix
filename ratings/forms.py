from django import forms
from .models import Vote
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