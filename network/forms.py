from django import forms
from django.conf import settings
from .models import Post
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

MAX_POST_LENGTH = settings.MAX_POST_LENGTH

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['tweet']
    
    def clean_tweet(self):
        tweet = self.cleaned_data.get("tweet")
        if len(tweet) > MAX_POST_LENGTH:
            raise forms.ValidationError("This post is too long")
        return tweet



class NewUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(NewUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user