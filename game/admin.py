from django.contrib import admin

# Register your models here.
from .models import FigureSet, Game, GameConfig, Phalanx, Victory, Player, Figure, Effect, Action

class GameAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)
admin.site.register(GameConfig, GameAdmin)

#https://github.com/fabiocaccamo/django-treenode
admin.site.register(Phalanx, GameAdmin)
admin.site.register(Victory, GameAdmin)
admin.site.register(Player, GameAdmin)
admin.site.register(Figure, GameAdmin)
admin.site.register(FigureSet, GameAdmin)
admin.site.register(Effect, GameAdmin)
admin.site.register(Action, GameAdmin)

