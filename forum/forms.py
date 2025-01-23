from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "input-field",
                    "placeholder": "Enter your question title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "input-field",
                    "rows": 6,
                    "placeholder": "Describe your question in detail...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Question Title"
        self.fields["content"].label = "Question Content"
