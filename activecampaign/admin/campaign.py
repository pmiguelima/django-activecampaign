# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from activecampaign.models.campaign import Campaign


class CampaignForm(forms.ModelForm):
    sync_key = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Campaign
        fields = "__all__"


class CampaignAdmin(admin.ModelAdmin):
    form = CampaignForm
    actions = ['delete_model']

    def get_actions(self, request):
        actions = super(CampaignAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        if type(obj) is Campaign:
            obj.delete()
        else:
            for o in obj.all():
                o.delete()
    delete_model.short_description = 'Delete flow'


admin.site.register(Campaign, CampaignAdmin)
