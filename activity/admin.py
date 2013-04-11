from django.contrib import admin

from activity.models import Activity, ACTION_VIEWED


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['content_object', 'user', 'action', 'timestamp']

    def queryset(self, request):
        qs = Activity.objects.exclude(action=ACTION_VIEWED)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

admin.site.register(Activity, ActivityAdmin)

