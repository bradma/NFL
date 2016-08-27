from django.contrib import admin
from .models import user, game_pick, game_week

admin.site.register(user)
admin.site.register(game_pick)
admin.site.register(game_week)