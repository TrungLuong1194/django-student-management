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
		("Nam", "Nam"),
		("Nữ", "Nữ"),
	)

	GRADE_CHOICES = (
		("Отлично", "Отлично"),
		("Хорошо", "Хорошо"),
		("Удовлетворительно", "Удовлетворительно"),
		("Зачтено", "Зачтено")
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

	ruSubject2 = forms.CharField(max_length=128, required=False)
	viSubject2 = forms.CharField(max_length=128, required=False)
	resultSubject2 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject3 = forms.CharField(max_length=128, required=False)
	viSubject3 = forms.CharField(max_length=128, required=False)
	resultSubject3 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject4 = forms.CharField(max_length=128, required=False)
	viSubject4 = forms.CharField(max_length=128, required=False)
	resultSubject4 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject5 = forms.CharField(max_length=128, required=False)
	viSubject5 = forms.CharField(max_length=128, required=False)
	resultSubject5 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject6 = forms.CharField(max_length=128, required=False)
	viSubject6 = forms.CharField(max_length=128, required=False)
	resultSubject6 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject7 = forms.CharField(max_length=128, required=False)
	viSubject7 = forms.CharField(max_length=128, required=False)
	resultSubject7 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject8 = forms.CharField(max_length=128, required=False)
	viSubject8 = forms.CharField(max_length=128, required=False)
	resultSubject8 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject9 = forms.CharField(max_length=128, required=False)
	viSubject9 = forms.CharField(max_length=128, required=False)
	resultSubject9 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject10 = forms.CharField(max_length=128, required=False)
	viSubject10 = forms.CharField(max_length=128, required=False)
	resultSubject10 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject11 = forms.CharField(max_length=128, required=False)
	viSubject11 = forms.CharField(max_length=128, required=False)
	resultSubject11 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	ruSubject12 = forms.CharField(max_length=128, required=False)
	viSubject12 = forms.CharField(max_length=128, required=False)
	resultSubject12 = forms.ChoiceField(choices=GRADE_CHOICES, required=False)

	# Information of Bank
	nameBank = forms.CharField(max_length=128, required=False)
	nameAccount = forms.CharField(max_length=128, required=False)  # Ten tieng nga


	class Meta:
		model = UserProfile
		exclude = ('user',)