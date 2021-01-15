from django import forms
# from django.contrib.auth.models import Group
from registration.models import Startup, User, TeamMemberProfileInfo, IndividualProfileInfo, TeamLeaderProfileInfo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))


    class Meta():
        model = User
        fields = ('username','password','first_name','last_name','university','email','portfolio_link','profile_pic')
        widgets = {
            'startupID': forms.HiddenInput(),
            'name_of_the_startup': forms.HiddenInput(),
        }


class IndividualProfileInfoForm(forms.ModelForm):
    class Meta():
        model = IndividualProfileInfo
        fields = ()


class TeamLeaderProfileInfoForm(forms.ModelForm):
    class Meta():
        model = TeamLeaderProfileInfo
        fields = ()
        widgets = {
            'startupID': forms.HiddenInput(),
        }

class TeamMemberProfileInfoForm(forms.ModelForm):

    class Meta():
        model = TeamMemberProfileInfo
        fields = ()
        widgets = {
            'startupID': forms.HiddenInput(),
        }

class StartupForm(forms.ModelForm):
    name_of_the_startup = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of the Startup'}))

    class Meta:
        model = Startup
        fields = ('name_of_the_startup','portfolio_link_of_the_Startup','profile_logo')
        widgets = {
            'group': forms.HiddenInput(),
        }

    def getModel(self):
        return model


class EditProfileForm(UserChangeForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    class Meta():
        model = User
        fields = {
        'email',
        'first_name',
        'last_name',
        'username',
        'university',
        'portfolio_link',
        'profile_pic',
        }
        exclude = ('password',)



class EditStartupForm(forms.ModelForm):
    name_of_the_startup = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'New Name of the Startup'}))


    class Meta():
        model = Startup
        fields = ('name_of_the_startup','portfolio_link_of_the_Startup','profile_logo')
        widgets = {
            'group': forms.HiddenInput(),
        }

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
