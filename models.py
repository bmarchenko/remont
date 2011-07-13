# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin

STATUS_CHOICES = (
    ('u', 'Unpublished'),
    ('p', 'Published'),
)

class Feedback(models.Model):
    company = models.TextField(max_length=100)
    position = models.TextField(max_length=100)
    comment = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
 
    def __unicode__(self):
       return self.company
 
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['company', 'status']
    search_fields = ["company"]
    
    
    def make_published(self, request, queryset):
      queryset.update(status='p')
    make_published.short_description = "Make feedback published"
    
    actions = [make_published]
admin.site.register(Feedback, FeedbackAdmin)
