from django import forms
from student.models import Major, UserProfile
from django.contrib.auth.models import User


class MajorForm(forms.ModelForm):
	code = forms.CharField(max_length=20)
	viName = forms.CharField(max_length=128)
	enName = forms.CharField(max_length=128)


	class Meta:
	    model = Major
	    fields = ('code', 'viName', 'enName')


class UserProfileForm(forms.ModelForm):

	GENDER_CHOICES = ( 
		("Nam", "Male"),
		("Nữ", "Female"),
	) 

	major = forms.ModelChoiceField(queryset=Major.objects.all())
	fullName = forms.CharField(max_length=128)
	gender = forms.ChoiceField(choices=GENDER_CHOICES)
	birthday = forms.DateField()
	ethnic = forms.CharField(max_length=20)
	religion = forms.CharField(max_length=20)
	studyYear = forms.IntegerField()
	addressVN = forms.CharField(max_length=128)
	addressRu = forms.CharField(max_length=128)
	phone = forms.IntegerField()


	class Meta:
		model = UserProfile
		exclude = ('user',)