# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class RssFeed(models.Model):
    url = models.URLField(unique=True,db_index=True,verify_exists=False,default='')
    name = models.CharField(blank=True, default='', max_length=100)
    lastmodified = models.DateTimeField(editable=False, auto_now=True, auto_now_add=True, db_index=True)
    
    def __unicode__(self):
        if self.url:
            return "{} {}".format(self.name, self.url)
        else:
            return "RssFeed {}".format(self.pk)
    
class RssArticle(models.Model):
    feed = models.ForeignKey(RssFeed)
    url = models.URLField(max_length=200,db_index=True,verify_exists=False,default='')
    snippet = models.CharField(max_length=500,default='')
    is_read = models.BooleanField(default=True)
    lastmodified = models.DateTimeField(editable=False, auto_now=True, auto_now_add=True, db_index=True)
    
    def __unicode__(self):
        if self.url:
            return "{} {} {}".format(self.feed, self.url, self.snippet[:10])
        else:
            return "RssArticle {}".format(self.pk)
    
    class Meta:
        unique_together = ['feed', 'url']