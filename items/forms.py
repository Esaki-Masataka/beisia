from django import forms

class ListForm(forms.Form):
    name = forms.CharField(label='name')
    number = forms.IntegerField(label='number')
    lists = forms.CharField(label='lists', widget=forms.Textarea)

