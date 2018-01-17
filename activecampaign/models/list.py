# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from .activecampaign import ActiveCampaign


class List (ActiveCampaign):
    name = models.CharField(max_length=255, null=False, blank=False)
    subscription_notify = models.CharField(max_length=255, blank=True)
    unsubscription_notify = models.CharField(max_length=255, blank=True)
    sender_remember = models.TextField(null=True, blank=True)
    sender_url = models.URLField(null=False, blank=False)

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            response = self.edit()
            if response.status_code == 200:
                return super(List, self).save(*args, **kwargs)
        else:
            response = self.add()
            if response.status_code == 200:
                result = response.json()
                if result['id']:
                    self.sync_key = result['id']
                    return super(List, self).save(*args, **kwargs)
        return False

    def add(self):
        return self.request(
            'POST',
            None,
            {
                'name': self.name,
                'subscription_notify': self.subscription_notify,
                'unsubscription_notify': self.unsubscription_notify,
                'sender_remember': self.sender_remember,
                'sender_url': self.sender_url,
                'sender_name': settings.ACTIVECAMPAIGN_SENDER_NAME,
                'sender_addr1': settings.ACTIVECAMPAIGN_SENDER_ADDR1,
                'sender_city': settings.ACTIVECAMPAIGN_SENDER_CITY,
                'sender_country': settings.ACTIVECAMPAIGN_SENDER_COUNTRY,
            }
        )

    def delete(self, using=None, keep_parents=False):
        self.request('GET', [('id', self.sync_key)])
        return super(List, self).delete(using, keep_parents)

    def edit(self):
        return self.request(
            'POST',
            None,
            {
                'id': self.sync_key,
                'name': self.name,
                'subscription_notify': self.subscription_notify,
                'unsubscription_notify': self.unsubscription_notify,
                'sender_remember': self.sender_remember,
                'sender_url': self.sender_url,
                'sender_name': settings.ACTIVECAMPAIGN_SENDER_NAME,
                'sender_addr1': settings.ACTIVECAMPAIGN_SENDER_ADDR1,
                'sender_city': settings.ACTIVECAMPAIGN_SENDER_CITY,
                'sender_country': settings.ACTIVECAMPAIGN_SENDER_COUNTRY,
            }
        )

    def field_add(self):
        pass

    def field_delete(self):
        pass

    def field_edit(self):
        pass

    def field_view(self):
        pass

    def list(self):
        pass

    def paginator(self):
        pass

    def view(self):
        pass
