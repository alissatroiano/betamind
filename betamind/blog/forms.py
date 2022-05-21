from django import forms
from .models import Mood, Post, Comment


class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
        label="How are you doing?",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "I need a hand."
        })
    )

    content = forms.CharField(
        required=False,
        label="What's on your mind?",
        widget=forms.Textarea(attrs={
            'rows':5,
            'width':'100%',
            'class': 'form-control',
            'placeholder': 'Please let us know.'}))
    
    mood = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-select"}),
        initial="Happy",
        queryset=Mood.objects.all(),
        label="Select Your Mood"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'mood']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'mood': 'Select your Mood'
        }
        widgets = {
            'mood': forms.Select(attrs={'class': 'form-control'}),
        }

