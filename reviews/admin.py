from django.contrib import admin

from reviews.models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'user', 'score', 'date_changed') #, 'ip_address'
    list_filter = ('score', 'date_changed') #, 'content_type'
    search_fields = ('user',)#, 'ip_address',)

admin.site.register(Review, ReviewAdmin)
