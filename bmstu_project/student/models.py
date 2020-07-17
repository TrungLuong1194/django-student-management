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
	major = models.ForeignKey(Major, on_delete=models.CASCADE, null=True)
	fullName = models.CharField(max_length=128, null=True)
	gender = models.CharField(max_length=20, null=True)
	birthday = models.DateField(null=True)
	ethnic = models.CharField(max_length=20, null=True)  # Dan toc
	religion = models.CharField(max_length=20, null=True)  # Ton giao
	studyYear = models.IntegerField(null=True)
	addressVN = models.CharField(max_length=128, null=True)
	addressRu = models.CharField(max_length=128, null=True)
	phone = models.IntegerField(unique=True, null=True)


	def __str__(self):
		return self.user.username