from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
	"""
	Major of students
	Ex: IU7 - Kỹ thuật phần mềm - Software Engineering
	"""
	code = models.CharField(max_length=20, blank=False, unique=True)
	# Vietnamese Name of Major
	viName = models.CharField(max_length=128, blank=False, unique=True)
	# English Name of Major
	enName = models.CharField(max_length=128, blank=False, unique=True)


	class Meta:
		verbose_name_plural = 'majors'


	def __str__(self):
		return self.code


class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	major = models.ForeignKey(Major, on_delete=models.CASCADE, blank=False)
	fullName = models.CharField(max_length=128, blank=False)
	gender = models.CharField(max_length=20, blank=False)
	birthday = models.DateField(blank=False)
	ethnic = models.CharField(max_length=20, blank=False)  # Dan toc
	religion = models.CharField(max_length=20, blank=False)  # Ton giao
	studyYear = models.IntegerField(blank=False)
	addressVN = models.CharField(max_length=128, blank=False)
	addressRu = models.CharField(max_length=128, blank=False)
	phone = models.CharField(max_length=128, blank=False)
	workPlace = models.CharField(max_length=128, blank=True)
	dateOfAdmission = models.DateField(blank=False)  # Ngay nhap hoc
	dateOfStudy = models.DateField(blank=False)  # Ngay bat dau khoa hoc
	timeOfStudy = models.CharField(max_length=128, blank=False)  # Thoi gian dao tao
	infoOfStudy = models.CharField(max_length=128, blank=False)  # Dang hoc hoc ki ?

	# Result of study
	ruSubject1 = models.CharField(max_length=128, blank=True)
	viSubject1 = models.CharField(max_length=128, blank=True)
	resultSubject1 = models.CharField(max_length=20, blank=True)

	ruSubject2 = models.CharField(max_length=128, blank=True)
	viSubject2 = models.CharField(max_length=128, blank=True)
	resultSubject2 = models.CharField(max_length=20, blank=True)

	ruSubject3 = models.CharField(max_length=128, blank=True)
	viSubject3 = models.CharField(max_length=128, blank=True)
	resultSubject3 = models.CharField(max_length=20, blank=True)

	ruSubject4 = models.CharField(max_length=128, blank=True)
	viSubject4 = models.CharField(max_length=128, blank=True)
	resultSubject4 = models.CharField(max_length=20, blank=True)

	ruSubject5 = models.CharField(max_length=128, blank=True)
	viSubject5 = models.CharField(max_length=128, blank=True)
	resultSubject5 = models.CharField(max_length=20, blank=True)

	ruSubject6 = models.CharField(max_length=128, blank=True)
	viSubject6 = models.CharField(max_length=128, blank=True)
	resultSubject6 = models.CharField(max_length=20, blank=True)

	ruSubject7 = models.CharField(max_length=128, blank=True)
	viSubject7 = models.CharField(max_length=128, blank=True)
	resultSubject7 = models.CharField(max_length=20, blank=True)

	ruSubject8 = models.CharField(max_length=128, blank=True)
	viSubject8 = models.CharField(max_length=128, blank=True)
	resultSubject8 = models.CharField(max_length=20, blank=True)

	ruSubject9 = models.CharField(max_length=128, blank=True)
	viSubject9 = models.CharField(max_length=128, blank=True)
	resultSubject9 = models.CharField(max_length=20, blank=True)

	ruSubject10 = models.CharField(max_length=128, blank=True)
	viSubject10 = models.CharField(max_length=128, blank=True)
	resultSubject10 = models.CharField(max_length=20, blank=True)

	ruSubject11 = models.CharField(max_length=128, blank=True)
	viSubject11 = models.CharField(max_length=128, blank=True)
	resultSubject11 = models.CharField(max_length=20, blank=True)

	ruSubject12 = models.CharField(max_length=128, blank=True)
	viSubject12 = models.CharField(max_length=128, blank=True)
	resultSubject12 = models.CharField(max_length=20, blank=True)

	# Information of Bank
	nameBank = models.CharField(max_length=128, blank=True)
	nameAccount = models.CharField(max_length=128, blank=True)  # Ten tai khoan tieng Nga


	def __str__(self):
		return self.user.username