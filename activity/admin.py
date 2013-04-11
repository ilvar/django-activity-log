from django.contrib import admin

from activity.models import Activity, ACTION_VIEWED


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['content_object', 'user', 'action', 'timestamp']

    def queryset(self, request):
        return Activity.objects.exclude(action=ACTION_VIEWED)

admin.site.register(Activity, ActivityAdmin)

