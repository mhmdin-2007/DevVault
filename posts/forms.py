from django import forms
from .models import Post
from taggit.models import Tag
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    """
    Form for creating and editing posts.
    Dynamically updates fields based on post type.
    """

    # new_tags = forms.CharField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Add new tags',
    #         'id': 'id_new_tags'
    #     }),
    #     label='New tags (manual)',
    #     help_text='Enter new tags seprated by comma (e.g. Python, Django, API)'
    # )

    class Meta:
        model = Post
        fields = [
            'post_type', 'title', 'content', 'image', 'video', 'summary',
            'category', 'difficulty', 'company', 'tags'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here...'
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief summary of your post...'
            }),
            'post_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-select'
            }),
            'company': forms.Select(attrs={'class': 'form-select'}),
            'tags': TagWidget(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'post_type': 'Post Type',
            'title': 'Title',
            'content': 'Content',
            'image': 'Image (optional)',
            'video': "Video (optional)",
            'summary': 'Summary (optional)',
            'category': 'Category (for interview posts)',
            'difficulty': "Difficulty (for interview posts)",
            'company': 'Company (optional)',
            'tags': 'Tags (optional)',
        }

        help_texts = {
            'image': 'Upload a cover image for your post',
            'video': 'Upload a video file (mp4, webm, etc.)',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # make interview fields optional by default
            instance = kwargs.get('instance')
            if instance and instance.post_type == Post.PostType.INTERVIEW:
                self.fields['difficulty'].required = True
                self.fields['category'].required = True
            else:
                self.fields['difficulty'].required = False
                self.fields['category'].required = False

            self.fields['company'].required = False
            self.fields['tags'].required = False
            self.fields['image'].required = False
            self.fields['video'].required = False
            self.fields['summary'].required = False
