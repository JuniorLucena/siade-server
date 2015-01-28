from django.contrib import messages


class MessageMixin(object):
    success_message = ''

    def delete(self, request, *args, **kwargs):
        response = super(MessageMixin, self).delete(request, *args, **kwargs)
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return response

    def form_valid(self, form):
        response = super(MessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data={}):
        return self.success_message % cleaned_data
