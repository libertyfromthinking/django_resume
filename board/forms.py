from django import forms
from .models import *

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content', 'image',)
        labels = {'title':(''), 'content':(''), 'image':('이미지첨부'),}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder':'제목을 입력해 주세요'})
        self.fields['content'].widget.attrs.update({'placeholder':'내용을 입력해 주세요'})
        self.fields['image'].widget.attrs.update({'class':'btn btn-outline-secondary btn-sm'})
        
class SearchForm(forms.Form):
        search_word = forms.CharField(label='')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['search_word'].widget.attrs.update({'placeholder':'검색어를 입력해 주세요'})

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = { 'text': (''), }
        help_texts = {'text':(''),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'placeholder':'댓글을 입력해 주세요'})