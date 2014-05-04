from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from contributors.models import Contributor


class LessonsForm(forms.Form):
    """
    Form for users to apply for lessons from a pro player.
    Should have a game field (Only counter-strike for now)
    Pro player they desire lessons from
    Type (team/individual, duration)

    Should create a "desired lesson" model to save an instance of the request, inform the player, & track lesson status
    & payment
    """
    contributors = Contributor.objects.all()
    contributor_pick = forms.ModelChoiceField(queryset=contributors, empty_label=None)
    name = forms.CharField(max_length=128)
    occupation = forms.CharField(max_length=128)
    ice_cream = forms.CharField(max_length=128)
    like_website = forms.TypedChoiceField(
        label="Do you like this website?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect,
        initial='1',
        required=True,
    )
    favorite_food = forms.CharField(
        label="What is your favorite food?",
        max_length=80,
        required=True,
    )
    favorite_color=forms.CharField(
        label="What is your favorite color?",
        max_length=80,
        required=True,
    )
    favorite_number = forms.IntegerField(
        label="Favorite number",
        required=False,
    )
    notes = forms.CharField(
        label="Additional notes or feedback",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(LessonsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-lessonForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_lesson'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-2'

        self.helper.add_input(Submit('submit', 'Submit'))

        self.helper.layout = Layout(
            'email',
            'password',
            'remember_me',
        )


#         helper.label_class = 'col-lg-x' #for example 'col-lg-2'
# helper.field_class = 'col-lg-x' #for example 'col-lg-10'