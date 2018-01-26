from django import forms
from .models import *

class AppForm(forms.ModelForm):

	class Meta:
		model = Application
		fields = ('fio', 'phone', 'email', 'works', 'comment')