from django import forms
from .models import Vote

class HorizRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('overall_rating', 'qual_of_doc', 'efficacy', 'usability', 'comment')