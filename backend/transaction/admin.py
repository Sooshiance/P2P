from django.contrib import admin

from .models import (
    Peer,
)


class PeerAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Peer, PeerAdmin)
