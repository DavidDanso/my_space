from django.http import HttpResponse
from django.shortcuts import redirect

# Prevent User from viewing login or register page, once the user 
# is logged in
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# Prevent user from accessing certain pages
def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You're not allowed to access this Page!!")
        return wrapper_func
    return decorators


# Prevent user from accessing admin pages
def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'user':
			return redirect('user')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function