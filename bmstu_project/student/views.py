from django.shortcuts import render
from django.http import HttpResponse
from student.models import Major
from student.forms import MajorForm


def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

	return render(request, 'student/index.html', context=context_dict)

def majors_list(request):
	majors_list = Major.objects.all()

	return render(
		request, 
		'student/majors_list.html',
		{'majors_list' : majors_list}
	)

def add_major(request):
    form = MajorForm()

    if request.method == 'POST':
        form = MajorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)

    return render(request, 'student/add_major.html', {'form': form})