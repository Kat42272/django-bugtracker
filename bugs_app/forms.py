from django import forms
from .models import MyUser, Ticket


class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)


class AddTicketForm(forms.ModelForm):

  class Meta:
    model = Ticket
    fields = [
      'title',
      'description',
    ]

