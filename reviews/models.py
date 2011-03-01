import datetime

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from reviews.managers import ReviewManager


class Review(models.Model):
    """
    A generic review of a Django Model.
    """
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'), 
        related_name="reviews")
    object_id = models.PositiveIntegerField(_('object ID'))
    # key = models.CharField(_('key'), max_length=32)
    score = models.IntegerField(_('score'))
    content = models.TextField(_('content'))
    user = models.ForeignKey(User, verbose_name=_('user'), related_name="reviews")
    # ip_address = models.IPAddressField(_('IP address'))
    date_added = models.DateTimeField(_('date added'), 
        default=datetime.datetime.now, editable=False)
    date_changed = models.DateTimeField(_('date changed'), 
        default=datetime.datetime.now, editable=False)
    
    content_object  = generic.GenericForeignKey()
    
    objects = ReviewManager()
    
    # TODO: Add flagging of reviews...
    
    # def user_display(self):
    #     if self.user:
    #         return "%s (%s)" % (self.user.username, self.ip_address)
    #     return self.ip_address
    # user_display = property(user_display)
    # 
    # def partial_ip_address(self):
    #     ip = self.ip_address.split('.')
    #     ip[-1] = 'xxx'
    #     return '.'.join(ip)
    # partial_ip_address = property(partial_ip_address)
    # 
    # class Meta:
    #     unique_together = (('content_type', 'object_id', 'key', 'user')) #, 'ip_address'
    
    def save(self, *args, **kwargs):
        self.date_changed = datetime.datetime.now()
        super(Review, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return u"%s voted %s on %s" % (self.user.username, self.score, self.content_object)
        # return u"%s voted %s on %s" % (self.user_display, self.score, self.content_object)

    