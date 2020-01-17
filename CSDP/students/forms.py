
from django import forms


class AddStudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    student_i = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    roll = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    Semester = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    section = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    registration=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    session_start= forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    session_end = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
