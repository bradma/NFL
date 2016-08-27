from django import template

from NFL_App.media._help import weeks_to_date

register = template.Library()

@register.inclusion_tag('select_week_modal_games.html', takes_context=True)
def show_only_games_available(context):
    user_id = context['user']
    show_these_weeks = weeks_to_date.assign_weeks()
    return {'weeks' : show_these_weeks,
        'MyUserSpecial' : user_id,
    }

@register.inclusion_tag('user_main_modal_games.html', takes_context=True)
def show_only_user_games_available(context):
    user_id = context['user']
    show_these_weeks = weeks_to_date.assign_weeks()
    return {'weeks' : show_these_weeks,
        'MyUserSpecial' : user_id.id,
    }
