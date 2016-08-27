from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.core.urlresolvers import reverse

from User.forms import change_password, add_team
from Select.models import user, game_pick, game_week

class week_detail(TemplateView):
    template_name = 'user_show_week_content.html'

    def get_context_data(self, **kwargs):
        context = super(week_detail, self).get_context_data(**kwargs)
        context['selected_week'] = self.kwargs['week_id']
        context['user'] = self.kwargs['user_id']
        return context

def main_user(request, user_id):
    if request.user.is_authenticated():
        template_name = 'user_main.html'
        my_user = user.objects.get(id=user_id)
        stats = user.objects.all()
        if request.method == 'POST':
            form = change_password(request.POST)
            if form.is_valid():
                newPass = request.POST["newpassword"]
                curr_user = request.user
                curr_user.set_password(newPass)
                curr_user.save()
        else:
            form = change_password()
        context = {
            'MyUser' : my_user.id,
            'username' : str(my_user.user_name),
            'stats' : stats,
            'form' : form,
        }
        return render(request, template_name, context)
    else:
        return HttpResponseForbidden('<h1><b>Restricted</b>: Please Login</h1>')

def user_team(request, user_id):
    template_name = 'create_team.html'
    if request.method == 'POST':
        form = add_team(request.POST)
        if form.is_valid():
            current_user = user.objects.get(id=user_id)
            get_team_name_form = request.POST['teamName']
            current_user.team_name = get_team_name_form
            current_user.save()
            return HttpResponseRedirect(reverse('user_main:user_core', args=[user_id]))
    else:
        form = add_team()
    my_team_name = user.objects.get(id=user_id).team_name
    context = {
        'form' : form,
        'team' : my_team_name,
        'user' : user_id,
    }
    return render(request, template_name, context)

#Depreciate -> Remove
def change_(request, user_id):
    template_name = 'user_main.html'
    my_user = user.objects.get(id=user_id)
    stats = user.objects.all()
    if request.method == 'POST':
        form = change_password(request.POST)
        if form.is_valid():
            newPass = request.POST["newpassword"]
            curr_user = request.user
    else:
        form = change_password()
    context = {
        'MyUser' : my_user.id,
        'username' : str(my_user.user_name),
        'stats' : stats,
        'form' : form,
    }
    return render(request, template_name, context)
