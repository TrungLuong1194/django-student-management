from django import forms
from student.models import Major


class MajorForm(forms.ModelForm):
	code = forms.CharField(max_length=20, help_text="Please enter the major code.")
	viName = forms.CharField(max_length=128, help_text="Please enter the major vietnamese name.")
	enName = forms.CharField(max_length=128, help_text="Please enter the major english name.")


	class Meta:
	    model = Major
	    fields = ('code', 'viName', 'enName')