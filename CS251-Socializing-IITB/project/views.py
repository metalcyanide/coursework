from django.shortcuts import redirect

def login_redirect(resquest):
	return redirect('/accounts/login')