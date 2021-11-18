# -*- coding: utf-8 -*-
"""
Create Time: 11/17/2021 8:03 PM
Author: Zhou
"""

from django import forms
from App_Blog.models import Blog, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)