

from django.forms import ModelForm
from sondages.models import Sondage

#tuto1
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from sondages.models import Drinker



class SondageForm(ModelForm):
    class Meta:
        model=Sondage
        exclude = ('moderator',)





class RegistrationForm(ModelForm):
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Adress'))
    password = forms.CharField(label=(u'Password'),widget= forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'verify password'),widget= forms.PasswordInput(render_value=False))



    class Meta:
          model = Drinker
          exclude = ('user',)


    def clean_username(self):
        username = self.cleaned_data['username']

        try:

            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken , please select another")



    def clean_password1(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']

        if not (password1 and password1 == password):
            raise forms.ValidationError("passwords dissmatch")

        return password1


class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))



#modificaion





'''class DatePicker(forms.DateInput):
    template_name = 'register.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }


class DateForm(forms.Form):
    date = forms.DateField(widget=DatePicker)'''