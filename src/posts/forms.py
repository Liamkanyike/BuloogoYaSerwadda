from django import forms
from django.forms import ModelForm
from .models import Post, Comment



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'overview', 'content', 'thumbnail',
			'categories', 'featured', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment Here',
		'id': 'usercomment',
		'rows': '4'
	}))
	class Meta:
		model = Comment
		fields = ('content', )