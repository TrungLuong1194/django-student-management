from django.conf.urls import url
from student import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^majors/$', views.majors_list, name='majors_list'),
	url(r'^add_major/$', views.add_major, name='add_major'),
]