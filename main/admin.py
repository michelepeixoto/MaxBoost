from django.contrib import admin
from .models import User, Game, GameStat


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_online')
    list_display_links = ('username',)
    search_fields = ('username',)


admin.site.register(User, UserAdmin)
admin.site.register(Game)
admin.site.register(GameStat)
