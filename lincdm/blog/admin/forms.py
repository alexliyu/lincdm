#-*- coding:utf-8 -*-
'''
Created on 2011-1-30

@author: 李昱
博客表单管理
'''
from django import forms
from django.db.models import ManyToOneRel
from django.db.models import ManyToManyRel
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

from lincdm.blog.models import Entry
from lincdm.blog.models import Category
from lincdm.blog.admin.widgets import TreeNodeChoiceField
from lincdm.blog.admin.widgets import MPTTFilteredSelectMultiple
from lincdm.blog.admin.widgets import MPTTModelMultipleChoiceField


class CategoryAdminForm(forms.ModelForm):
    """Form for Category's Admin"""
    parent = TreeNodeChoiceField(label=_('parent category').capitalize(),
                                 required=False,
                                 empty_label=_('No parent category'),
                                 queryset=Category.tree.all(),
                                 level_indicator=u'|--')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminForm, self).__init__(*args, **kwargs)
        rel = ManyToOneRel(Category, 'id')
        self.fields['parent'].widget = RelatedFieldWidgetWrapper(
            self.fields['parent'].widget, rel, self.admin_site)

    def clean_parent(self):
        """Check if category parent is not selfish"""
        data = self.cleaned_data['parent']
        if data == self.instance:
            raise forms.ValidationError(
                _('A category cannot be parent of itself.'))
        return data

    class Meta:
        """CategoryAdminForm's Meta"""
        model = Category


class EntryAdminForm(forms.ModelForm):
    """Form for Entry's Admin"""
    categories = MPTTModelMultipleChoiceField(
        Category.objects.all(), required=False, label=_('Categories'),
        widget=MPTTFilteredSelectMultiple(_('categories'), False,
                                          attrs={'rows': '10'}))

    def __init__(self, *args, **kwargs):
        super(EntryAdminForm, self).__init__(*args, **kwargs)
        rel = ManyToManyRel(Category, 'id')
        self.fields['categories'].widget = RelatedFieldWidgetWrapper(
            self.fields['categories'].widget, rel, self.admin_site)
        self.fields['sites'].initial = [Site.objects.get_current()]

    class Meta:
        """EntryAdminForm's Meta"""
        model = Entry
