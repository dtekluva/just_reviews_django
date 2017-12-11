from django import forms
from django.contrib.auth.models import User
from reviews.models import Category, Comment, Product, UserAccount,Message


class CategoryForm(forms.ModelForm):


    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model  =  Category
        fields = ('name',)

class ProductForm(forms.ModelForm):

    name         = forms.CharField(max_length=30,
                                   help_text="Name     ::")
    details      = forms.CharField(max_length=300,
                                   help_text="Details :")
    views        = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    thumbsUp     = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    thumbsDown   = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug         = forms.CharField(widget=forms.HiddenInput(), required=False)
    Comment      = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    image        = forms.FileField(required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model   = Product
        fields  = ('name' ,'details', 'image',)

class CommentForm(forms.ModelForm):

    title       = forms.CharField(max_length=128, help_text="Enter Title :: ")

    body        = forms.CharField(max_length=300, help_text="Comment ::")

    image       = forms.FileField(required=False)

    
    class Meta:
        # Provide an association between the ModelForm and a model

        model = Comment

        fields  = ('title','body','image')

class SearchForm(forms.ModelForm):
    name   = forms.CharField(max_length=128,
                            help_text="Please enter product name.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model   = Product
        fields  = ('name',)
    
class UserRegistrationForm(forms.ModelForm):
    username    = forms.CharField(max_length=256, widget=forms.TextInput(), help_text="UserName     ::")
    first_name  = forms.CharField(max_length=256, help_text="First name     ::")
    last_name   = forms.CharField(max_length=256, help_text="Last name     ::")
    email       = forms.CharField(max_length=256, widget=forms.EmailInput(), help_text="Email addr    ::")
    password    = forms.CharField(max_length=256, widget=forms.PasswordInput(), help_text="Password    ::")
    image       = forms.FileField(required=False)

    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'image')

class Signinform(forms.ModelForm):
    username   =   forms.CharField(max_length=256, widget=forms.EmailInput())
    password=   forms.CharField(max_length=256, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields= ('username','password' )

class UserEditForm(forms.ModelForm):
    username    = forms.CharField(max_length=256, widget=forms.TextInput(), help_text="UserName     ::", required=False)
    first_name  = forms.CharField(max_length=256, help_text="First name     ::", required=False)
    last_name   = forms.CharField(max_length=256, help_text="Last name     ::", required=False)
    email       = forms.CharField(max_length=256, widget=forms.EmailInput(), help_text="Email addr    ::", required=False)
    password    = forms.CharField(max_length=256, widget=forms.PasswordInput(), help_text="Password    ::", required=False)
    image       = forms.FileField(required=False)

    class Meta:
        model = UserAccount
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'image')

class MessageForm(forms.ModelForm):
    body    = forms.CharField(max_length=256,help_text="body     ::", widget=forms.TextInput(), required=False)
    
    

    class Meta:
        model = Message
        fields = ('body',)