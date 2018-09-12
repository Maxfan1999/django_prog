from django import forms
from models import Article,ForumUser
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ForumUser
        fields = ['photo']


class ArticleForm(forms.ModelForm):
    text = forms.CharField(max_length=1000,widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['head']
