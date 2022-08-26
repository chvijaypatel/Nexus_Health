from django import forms
from django.forms import ModelForm
from .models import Comment, Reply


class CommentForm(forms.ModelForm):
      name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), max_length=100)
      email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}), max_length=100)
      phoneno = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile No'}), max_length=10)
      message = forms.CharField(strip=False ,widget=forms.Textarea(attrs={'placeholder': 'Write your message here ...'}), max_length=1000)

      class Meta:
        model = Comment
        fields = ['name', 'email', 'phoneno', 'message']


class ReplyForm(forms.ModelForm):
      name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), max_length=100)
      email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}), max_length=100)
      phoneno = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Mobile No'}), max_length=10)
      message = forms.CharField(strip=False ,widget=forms.Textarea(attrs={'placeholder': 'Write your message here ...'}), max_length=1000)

      class Meta:
        model = Reply
        fields = ['name', 'email', 'phoneno', 'message']


# class CommentForm(forms.ModelForm):
#       class Meta:
#         model = Comment
#         fields = ('name', 'email', 'phoneno', 'message')
      
#       # overriding default form setting and adding bootstrap class
#       def __init__(self, *args, **kwargs):
#          super(CommentForm, self).__init__(*args, **kwargs)
#          self.fields['name'].widget.attrs = {'placeholder': 'Enter name','class':'form-control'}
#          self.fields['email'].widget.attrs = {'placeholder': 'Enter email', 'class':'form-control'}
#          self.fields['phoneno'].widget.attrs = {'placeholder': 'Enter phone no.','class':'form-control'}
#          self.fields['message'].widget.attrs = {'placeholder': 'Comment here...', 'class':'form-control', 'rows':'5'}
          

