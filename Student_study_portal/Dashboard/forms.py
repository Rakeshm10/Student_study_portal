from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field,Submit


class NotesForm(forms.ModelForm):
    pdf = forms.FileField(label='Upload PDF', required=False)  # Add this line

    class Meta:
        model = Notes
        fields = ['title','description','pdf']

    
    def __init__(self, *args, **kwargs):
        super(NotesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('description', css_class='form-control'),
            'pdf',
            Submit('submit', 'Submit', css_class='btn btn-success')
        )

class DateInput(forms.DateInput):
    input_type='date'


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']

    



class UploadPdfForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['file_field']

    file_field = forms.FileField()


class DashoardForm(forms.Form):
    text = forms.CharField(max_length=100,label="Enter Your Search ")




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields =['title','is_finished']
        