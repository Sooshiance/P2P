from django.contrib import admin

from .models import (
    Peer,
    SharedFile,
)


class PeerAdmin(admin.ModelAdmin):
    list_display = ['user']


class SharedFileAdmin(admin.ModelAdmin):
    list_display = ['owner']


admin.site.register(Peer, PeerAdmin)

admin.site.register(SharedFile, SharedFileAdmin)
