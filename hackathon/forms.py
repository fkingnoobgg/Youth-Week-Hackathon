#Django imports
from django import forms
from django.contrib.admin import widgets
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, mail_admins
from django.template import Context,Template
from django.core.validators import RegexValidator, EmailValidator
from django.urls import reverse

#Logbook app imports
from .models import *
from django.conf import settings

#General imports
import os
import re
import socket

class EmailField(forms.CharField):
    default_validators = [EmailValidator()]
    widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'})

class UsernameField(forms.CharField):
    widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'})

class PasswordField(forms.CharField):
    widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})

class SignupFormBase(forms.Form):
    username = forms.CharField()
    email = EmailField(label='')
    password = PasswordField(label='')
    passwordVerify = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password Again'}))
    def clean(self):
        cleaned_data = super().clean()

        # Check that passwords match
        password = cleaned_data.get('password')
        passwordVerify = cleaned_data.get('passwordVerify')
        if password == '':
            raise forms.ValidationError('Password cannot be empty')
        if password != passwordVerify:
            raise forms.ValidationError('Passwords do not match')

        return cleaned_data

class SignupForm(SignupFormBase):
    username = UsernameField(label='')
    email = EmailField(label='')
    def save(self, data):
        user = User.objects.create_user(data['username'],data['email'],data['password'])
        
        ht_user =  HTUser()
        ht_user.user = user
        ht_user.activation_key = data['activation_key']
        ht_user.save()
    
    #Used for account creation, where users must verify their email address by clicking link.
    def sendVerifyEmail(self, mailData):
        hostname = socket.gethostbyname(socket.gethostname())
        link = "http://"+hostname+":8000/hackathon/activate/"+mailData['activation_key']
        contxt = Context({'activation_link':link,'username':mailData['username'],})
        EMAIL_PATH = os.path.join(settings.BASE_DIR,'hackathon','static', mailData['email_path'])
        file = open(EMAIL_PATH,'r')
        temp = Template(file.read())
        file.close
        message = temp.render(contxt)
        send_mail(mailData['email_subject'],message,'Homeless Services <sam.j.s.heath@gmail.com>',[mailData['email']], fail_silently=False)
        
class LoginForm(forms.Form):
    username = UsernameField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

#Suspends a users account so that their logbooks are kept in the database
#but they cant log in, will need to see about th rules regarding deleting accounts.
class DeleteUserForm(forms.ModelForm):
    is_active = forms.BooleanField(label='', initial=False)
    

"""
Below forms SetPasswordForm and ChangePasswordForm are taken directly
from the django documentation except I've flipped the position of the
old_password and altering the placeholders and attrs{} of the password fields.
"""
class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch':("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    new_password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password Again'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(self.error_messages['password_mismatch'],code='password_mismatch',)
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user

class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': ("Your old password was entered incorrectly. Please enter it again."),})
    old_password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Old Password'}))

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(self.error_messages['password_incorrect'],code='password_incorrect',)
        return old_password
