from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        # 연결시킬 model
        model = Todo
        # 입력받는 필드 값 
        fields = ('title', 'description', 'important')