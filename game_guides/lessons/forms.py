from django import forms

from contributors.models import Contributor


class LessonsForm(forms.Form):
    contributors = Contributor.objects.all()
    contributor_pick = forms.ModelChoiceField(queryset=contributors, empty_label=None)
#            <li>Game</li>#}
#            <li>Player</li>#}
#            <li>Type</li>#}
#            <li>Additional Details</li>#}
