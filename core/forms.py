from django import forms
from .models import Question ,Answer


class PostQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets ={
            'title':forms.TextInput(attrs={'class':'form-control  '}),
            'content':forms.Textarea(attrs={'class':'form-control ', 'placeholder':'Optional ~ write question or topic elobrate.'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Your Question *"  
        self.fields['content'].label = "Description (Optional)"  
       
class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['content']
        widgets ={
            'content':forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Write your thought on this.'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ""  
       
