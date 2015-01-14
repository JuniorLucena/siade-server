from __future__ import unicode_literals
from django import forms
from django.utils.html import escape
from django.utils.safestring import mark_safe


class ReadOnlyWidget(forms.Widget):
    def render(self, name, value, attrs):
        #final_attrs = self.build_attrs(attrs, name=name)
        if not value and hasattr(self, 'initial'):
            value = self.initial
        #return mark_safe('<span %s>%s</span>' % (
                         #flatatt(final_attrs), escape(value) or ''))
        return mark_safe('<p class="form-control-static">%s</p>' % (
                         escape(value) or ''))

    def _has_changed(self, initial, data):
        return False


class ReadOnlyField(forms.FileField):
    widget = ReadOnlyWidget

    def __init__(self, widget=None, label=None, initial=None, help_text=None):
        forms.Field.__init__(self, label=label, initial=initial,
                             required=False,
                             help_text=help_text, widget=widget)

    def clean(self, value, initial):
        self.widget.initial = initial
        return initial
