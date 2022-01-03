from django.contrib import admin
from cards.models import Card


class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'front', 'streak', 'created_at']

admin.site.register(Card, CardAdmin)
