# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import inspect
import requests


class ActiveCampaign(models.Model):
    sync_key = models.IntegerField(null=True, blank=True, default=0)
    end_point = settings.ACTIVECAMPAIGN_PATH
    secret = settings.ACTIVECAMPAIGN_PASS

    class Meta:
        abstract = True

    def request(self, method, parameters=None, data=None):
        return requests.request(
            method,
            self.end_point,
            params=[
                ('api_output', 'json'),
                ('api_key', self.secret),
                ('api_action', self.__class__.__name__.lower() + '_' + inspect.stack()[1][3]),
            ] + (parameters if parameters else []),
            headers={
                'content-type': 'application/x-www-form-urlencoded'
            },
            data=data
        )
