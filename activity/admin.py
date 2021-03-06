from django.contrib import admin

from activity.models import Activity, ACTION_VIEWED


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['content_object', 'user', 'action', 'timestamp']
    list_filter = ['action']
    search_fields = ['object_id', 'user__username']

admin.site.register(Activity, ActivityAdmin)

