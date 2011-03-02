from django.contrib import admin

from reviews.models import *


class VoteAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'ip_address', 'like', 'date_changed', 'date_added')
    list_filter = ('like', 'date_changed', 'date_added', 'user', 'ip_address')
    search_fields = ('user',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'user', 'score', 'date_changed', 'date_added') #, 'ip_address'
    list_filter = ('score', 'date_changed', 'date_added', 'user') #, 'content_type'
    search_fields = ('user',)#, 'ip_address',)

admin.site.register(Vote, VoteAdmin)
admin.site.register(Review, ReviewAdmin)
