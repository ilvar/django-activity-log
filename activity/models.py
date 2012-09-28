from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

NAME_DESCRIPTION = _(u'Some user did something to THIS')

ACTION_ADDED = 'added'
ACTION_EDITED = 'edited'
ACTION_DELETED = 'deleted'

ACTIONS = (
    (ACTION_ADDED, _('Added')),
    (ACTION_EDITED, _('Edited')),
    (ACTION_DELETED, _('Deleted')),
)

class Activity(models.Model):
    content_type = models.ForeignKey(ContentType, verbose_name=_(u'Object type'))
    object_id = models.PositiveIntegerField(verbose_name=_(u'Object pk'))
    content_object = generic.GenericForeignKey()

    action = models.CharField(max_length=255, verbose_name=_(u'Action'), choices=ACTIONS)
    user = models.ForeignKey('auth.User', verbose_name=_(u'User'), blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Time'))

    def is_creation(self):
        return self.action == ACTION_ADDED

    def get_content_type_name_plural(self):
        return self.content_object._meta.verbose_name_plural

def record_activity(instance, action, user):
    if not user.is_authenticated():
        user = None
    Activity.objects.create(content_object=instance, action=action, user=user)