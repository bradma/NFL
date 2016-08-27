from django import template
#from django.forms import RadioSelect

register = template.Library()

@register.filter(name='is_game_picked')
def is_game_picked(field):
    pass_me = False
    if field.field.widget.attrs.get('disabled'):
        pass_me = True
    return pass_me