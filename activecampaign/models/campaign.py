# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .activecampaign import ActiveCampaign
from .message import Message
from .list import List


class Campaign(ActiveCampaign):
    name = models.CharField(max_length=255, null=False, blank=False)
    sdate = models.DateTimeField(null=False, blank=False)

    message = models.ForeignKey(Message)
    list_contact = models.ForeignKey(List)

    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            return super(Campaign, self).save(*args, **kwargs)
        else:
            response = self.create()
            if response.status_code == 200:
                result = response.json()
                if result['id']:
                    self.sync_key = result['id']
                    return super(Campaign, self).save(*args, **kwargs)
        return False

    def create(self):
        return self.request(
            'POST',
            None,
            {
                'name': self.name,
                'sdate': self.sdate,
                'type': "single",
                'status': "1",
                'public': "1",
                'tracklinks': "all",
                'p[' + str(self.list_contact.sync_key) + ']': str(self.list_contact.sync_key),
                'm[' + str(self.message.sync_key) + ']': str(self.message.sync_key)
            }
        )
    
    def delete(self, using=None, keep_parents=False):
        r = self.request('GET', [('id', self.sync_key)])
        if r.status_code == 200:
            return super(Campaign, self).delete(using, keep_parents)
        return False
    
    def delete_list(self):
        pass

    def list(self):
        pass
    
    def paginator(self):
        pass
    
    def report_bounce_list(self):
        pass
    
    def report_bounce_totals(self):
        pass
    
    def report_forward_list(self):
        pass
    
    def report_forward_totals(self):
        pass
    
    def report_link_list(self):
        pass
    
    def report_link_totals(self):
        pass
    
    def report_open_list(self):
        pass
    
    def report_open_totals(self):
        pass
    
    def report_totals(self):
        pass
    
    def report_unopen_list(self):
        pass
    
    def report_unsubscription_list(self):
        pass
    
    def report_unsubscription_totals(self):
        pass
    
    def send(self):
        pass
    
    def status(self):
        pass