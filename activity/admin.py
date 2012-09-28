from django.contrib import admin

from activity.models import Activity

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['content_object', 'user', 'action', 'timestamp']

admin.site.register(Activity, ActivityAdmin)

