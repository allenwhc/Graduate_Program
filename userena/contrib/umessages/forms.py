#-*- coding: UTF-8 -*- 
from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.contrib.umessages.fields import CommaSeparatedUserField
from userena.contrib.umessages.models import Message, MessageRecipient

import datetime

class ComposeForm(forms.Form):
    to = CommaSeparatedUserField(label=_("发给谁".decode('utf-8')))
    body = forms.CharField(label=_("写信息".decode('utf-8')),
                           widget=forms.Textarea({'class': 'message'}),
                           required=True)

    def save(self, sender):
        """
        Save the message and send it out into the wide world.

        :param sender:
            The :class:`User` that sends the message.

        :param parent_msg:
            The :class:`Message` that preceded this message in the thread.

        :return: The saved :class:`Message`.

        """
        to_user_list = self.cleaned_data['to']
        body = self.cleaned_data['body']

        msg = Message.objects.send_message(sender,
                                           to_user_list,
                                           body)

        return msg
