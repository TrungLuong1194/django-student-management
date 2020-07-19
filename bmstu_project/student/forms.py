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

	GRADE_CHOICES = (
		("Giỏi", "Отлично"),
		("Khá", "Хорошо"),
		("Trung Bình", "Удовлетворительно"),
		("Đạt", "Зачтено")
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
	phone = forms.CharField(max_length=128)
	workPlace = forms.CharField(max_length=128, required=False)
	dateOfAdmission = forms.DateField()  # Ngay nhap hoc
	dateOfStudy = forms.DateField()  # Ngay bat dau khoa hoc
	timeOfStudy = forms.CharField(max_length=128)  # Thoi gian dao tao
	infoOfStudy = forms.CharField(max_length=128)  # Dang hoc hoc ki ?

	# Result of study
	ruSubject1 = forms.CharField(max_length=128, required=False)
	viSubject1 = forms.CharField(max_length=128, required=False)
	resultSubject1 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	# Information of Bank
	nameBank = forms.CharField(max_length=128)
	nameAccount = forms.CharField(max_length=128)  # Ten tieng nga


	class Meta:
		model = UserProfile
		exclude = ('user',)