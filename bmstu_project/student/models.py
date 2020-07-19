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

	# Information of Bank
	nameBank = models.CharField(max_length=128, blank=False)
	nameAccount = models.CharField(max_length=128, blank=False)  # Ten tai khoan tieng Nga


	def __str__(self):
		return self.user.username