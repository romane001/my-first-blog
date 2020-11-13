from django import forms
from django.shortcuts import render, get_object_or_404


class PostForm(forms.ModelForm):

    class Meta:
        model = PostForm
        fields = ('title', 'text',)