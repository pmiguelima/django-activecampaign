# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib import admin

from activecampaign.models.list import List


class ListForm(forms.ModelForm):
    sync_key = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = List
        fields = "__all__"


class ListAdmin(admin.ModelAdmin):
    form = ListForm
    actions = ['delete_model']

    def get_actions(self, request):
        actions = super(ListAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        if type(obj) is List:
            obj.delete()
        else:
            for o in obj.all():
                o.delete()
    delete_model.short_description = 'Delete flow'


admin.site.register(List, ListAdmin)
