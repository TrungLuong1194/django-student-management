from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import Major, UserProfile
from student.forms import MajorForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

	return render(request, 'student/index.html', context=context_dict)

@login_required
def majors_list(request):
	majors_list = Major.objects.all()

	return render(request, 'student/majors_list.html',
		{'majors_list' : majors_list})

@login_required
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

@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form':form}

    return render(request, 'student/profile_registration.html', context_dict)


class StudentRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({
            'major': userprofile.major,
            'fullName': userprofile.fullName,
            'gender': userprofile.gender,
            'birthday': userprofile.birthday,
            'ethnic': userprofile.ethnic,
            'religion': userprofile.religion,
            'studyYear': userprofile.studyYear,
            'addressVN': userprofile.addressVN,
            'addressRu': userprofile.addressRu,
            'phone': userprofile.phone,
        })
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    
    return render(request, 'student/profile.html', 
            {'userprofile': userprofile, 'selecteduser': user, 'form': form})

@login_required
def profiles_list(request):
    userprofile_list = UserProfile.objects.all()

    return render(request, 'student/profiles_list.html',
            {'userprofile_list' : userprofile_list})