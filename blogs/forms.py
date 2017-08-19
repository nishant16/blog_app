from django import forms
from .models import Blog
from django.forms import ModelForm

class BlogForm(forms.Form):
    title = forms.CharField(label ='title' , max_length = 50)
    content = forms.CharField(label = 'content', max_length = 100)
    category = forms.CharField(label = 'category', max_length = 50)

class CreateForm(ModelForm):
	class Meta:
		model = Blog
		fields = ['title','category','Content']

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 50)
	password = forms.CharField(max_length = 50)













 #title = models.CharField(max_length=120)
    #category = models.ForeignKey(Category)
   # Content = models.TextField()
   # posted = models.DateField()

