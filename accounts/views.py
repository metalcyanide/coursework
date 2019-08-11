from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from accounts.forms import EditProfleForm, PostForm, TemplateForm, ProfileForm, UserCreationForm2
from .models import Post, Template, Profile


# Create your views here.
def home(request):
	return render(request,'accounts/home.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm2(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
		form = UserCreationForm2()
		args = {'form': form}
		return render(request, 'accounts/reg_form.html', args)

def profile(request):
	args = {'user': request.user}
	#users = User.objects.all().select_related('profile')
	return render(request, 'accounts/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form =  EditProfleForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			args = {'user': request.user}
			return render(request, 'accounts/profile.html', args)
	else:
		form =  EditProfleForm(instance=request.user)
		args = {'form': form}
		return render(request, 'accounts/edit_profile.html', args)

def posts(request):
	posts = Post.objects.order_by('published_date')
	args = {'user': request.user, 'posts' : posts}
	return render(request, 'accounts/posts.html', args)

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			return redirect('/accounts')
	else:
		form = PostForm()
		args = {'form': form,'user': request.user}
		return render(request, 'accounts/post_new.html', args)

def template(request):
	if request.method == 'POST':
		form = TemplateForm(request.POST, instance=request.user.template)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
		form = TemplateForm(instance=request.user.template)
		args = {'form': form}
		return render(request, 'accounts/template.html', args)

def edit_deeper_profile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('/accounts')
	else:
		form = ProfileForm(instance=request.user.profile)
		args = {'form': form}
		return render(request, 'accounts/template.html', args)