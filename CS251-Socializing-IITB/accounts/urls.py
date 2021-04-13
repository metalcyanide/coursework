from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	url(r'^$',views.home),
	url(r'^logout/$', login, {'template_name': 'accounts/logout.html'}),
	url(r'^register/$', views.register, name='register'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^edit_deeper_profile/$', views.edit_deeper_profile, name='edit_deeper_profile'),
	url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
	url(r'^post_new/$', views.post_new, name='post_new'),
	url(r'^template/$', views.template, name='template'),
	url(r'^posts/$', views.posts, name='posts'),
	url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
	url(r'^friendship/', include('friendship.urls'))
]