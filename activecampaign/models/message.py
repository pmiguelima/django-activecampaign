# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from .activecampaign import ActiveCampaign
from .list import List


class Message (ActiveCampaign):

    subject = models.CharField(max_length=255, null=False, blank=False)
    list_contact = models.ForeignKey(List, null=False, blank=False)
    html = models.TextField()

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    def __str__(self):
        return self.subject

    def __unicode__(self):
        return self.subject

    def save(self, *args, **kwargs):
        if self.pk:
            response = self.edit()
            if response.status_code == 200:
                return super(Message, self).save(*args, **kwargs)
        else:
            response = self.add()
            if response.status_code == 200:
                result = response.json()
                if result['id']:
                    self.sync_key = result['id']
                    return super(Message, self).save(*args, **kwargs)
        return False
    
    def add(self):
        data = {
            'format': 'mime',
            'subject': self.subject,
            'fromemail': settings.ACTIVECAMPAIGN_FROMMAIL,
            'fromname': settings.ACTIVECAMPAIGN_NAME,
            'reply2': settings.ACTIVECAMPAIGN_REPLAY,
            'priority': '3',
            'charset': 'utf-8',
            'encoding': 'quoted-printable',
            'htmlconstructor': 'editor',
            'html': self.html,
            'p[' + str(self.list_contact.sync_key) + ']': str(self.list_contact.sync_key)
        }
        return self.request(
            'POST',
            None,
            data
        )

    def delete(self, using=None, keep_parents=False):
        r = self.request('GET', [('id', self.sync_key)])
        if r.status_code == 200:
            return super(Message, self).delete(using, keep_parents)
        return False

    def edit(self):
        return self.request(
            'POST',
            None,
            {
                'id': self.sync_key,
                'format': 'mime',
                'subject': self.subject,
                'fromemail': settings.ACTIVECAMPAIGN_FROMMAIL,
                'fromname': settings.ACTIVECAMPAIGN_NAME,
                'reply2': settings.ACTIVECAMPAIGN_REPLAY,
                'priority': '3',
                'charset': 'utf-8',
                'encoding': 'quoted-printable',
                'htmlconstructor': 'editor',
                'html': self.html,
                'p[' + str(self.list_contact.sync_key) + ']': str(self.list_contact.sync_key)
            }
        )

    def list(self):
        pass

    def template_add(self):
        pass

    def template_delete(self):
        pass

    def template_delete_list(self):
        pass

    def template_edit(self):
        pass

    def template_export(self):
        pass

    def template_import(self):
        pass

    def template_list(self):
        pass

    def template_view(self):
        pass

    def view(self):
        pass