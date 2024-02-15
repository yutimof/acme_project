from django import forms
from .models import Birthday
from .validators import real_age


class BirthdayForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(label='Фамилия', required=False)
    birthday = forms.DateField(label='День рождения', validators=(real_age,), widget=forms.DateInput(attrs={'type': 'date'})) 

    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__'

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам 
        # и возвращаем только первое имя.
        return first_name.split()[0] 
 