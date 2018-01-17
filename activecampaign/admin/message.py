# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from activecampaign.models.message import Message
from activecampaign.models.campaign import Campaign


class CampaignInline(admin.StackedInline):
    model = Campaign
    max_num = 1


class MessageForm(forms.ModelForm):
    sync_key = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Message
        fields = "__all__"


class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    actions = ['delete_model']
    inlines = [CampaignInline, ]

    def get_actions(self, request):
        actions = super(MessageAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        if type(obj) is Message:
            obj.delete()
        else:
            for o in obj.all():
                o.delete()
    delete_model.short_description = 'Delete flow'


admin.site.register(Message, MessageAdmin)
