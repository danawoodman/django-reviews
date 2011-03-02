import datetime

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from reviews.managers import *


class Vote(models.Model):
    """
    A vote for or against a Review.
    
    This let's users rate up or down a review that they found useful.
    
    Usage::
        
        >>> vote = Vote(like=True, user=1, review=1)
        >>> review.votes.add(vote)
    
    """
    like = models.BooleanField(default=True)
    user = models.ForeignKey(User, verbose_name=_('user'), 
        related_name='votes', blank=True, null=True)
    ip_address = models.IPAddressField(blank=True)
    review = models.ForeignKey('Review', verbose_name=_('review'), 
        related_name='votes')
    date_added = models.DateTimeField(_('date added'), 
        default=datetime.datetime.now, editable=False)
    date_changed = models.DateTimeField(_('date changed'), 
        default=datetime.datetime.now, editable=False)
    
    objects = VoteManager()
    
    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')
    
    def save(self, *args, **kwargs):
        self.date_changed = datetime.datetime.now()
        super(Vote, self).save(*args, **kwargs)
    
    def __unicode__(self):
        
        # Get their vote; either up or down.
        if self.like:
            v = "up"
        else:
            v = "down"
        
        # Get the user string
        if self.user != None:
            u = "%s [%s]" % (self.user.username, self.ip_address)
        else:
            u = "[%s]" % self.ip_address
        
        return u"%s voted %s Review #%s" % (u, v, 
            self.review.id)
    

class Review(models.Model):
    """
    A generic Review of a Django Model.
    
    Usage::
    
        from django.db import models
        
        from reviews.models import Review
        
        class MyModel(models.Model):
            foo = models.TextField()
            reviews = models.ForeignKey(Review)
    
    """
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'), 
        related_name="reviews")
    object_id = models.PositiveIntegerField(_('object ID'))
    
    # key = models.CharField(_('key'), max_length=32)
    score = models.IntegerField(_('rating'))
    content = models.TextField(_('review'))
    user = models.ForeignKey(User, verbose_name=_('user'), 
        related_name='reviews')
    # votes = models.ManyToManyField(Vote, verbose_name=_('reviews'), 
    #     related_name='reviews')
    # ip_address = models.IPAddressField(_('IP address'))
    date_added = models.DateTimeField(_('date added'), 
        default=datetime.datetime.now, editable=False)
    date_changed = models.DateTimeField(_('date changed'), 
        default=datetime.datetime.now, editable=False)
    
    content_object = generic.GenericForeignKey()
    
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
    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
        # unique_together = (('content_type', 'object_id', 'key', 'user')) #, 'ip_address'
    
    def save(self, *args, **kwargs):
        self.date_changed = datetime.datetime.now()
        super(Review, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return u"Review of %s by %s" % (self.content_object, self.user.username)
        # return u"%s voted %s on %s" % (self.user_display, self.score, self.content_object)


    