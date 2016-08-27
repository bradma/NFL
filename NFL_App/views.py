from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from NFL_App.forms import loginForm
from Select.models import user

# Login View
def login_site(request):
    template_name = 'login.html'
    if request.method == 'POST':
        _username = request.POST['name']
        _password = request.POST['passw']
        userlogin = authenticate(username=_username, password=_password)
        if userlogin:
            if userlogin.is_active:
                login(request, userlogin)
                user_id = user.objects.get(user_name__iexact=_username)
                redirect = '/User/' + str(user_id.id)
                return HttpResponseRedirect(redirect)

            else:
                return HttpResponse('Invalid')

        else:
            return HttpResponse('Invalid Username or Password')

    else:
        form = loginForm(auto_id='%s')

    context = {'loginForm' : form,}

    return render(request, template_name, context)

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('login'))
