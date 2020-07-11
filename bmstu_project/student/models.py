from django.db import models


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
