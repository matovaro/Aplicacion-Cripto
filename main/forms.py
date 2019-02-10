from django import forms

class Algoritm(forms.Form):
	user = forms.CharField(max_length=100) 
	key = forms.CharField(max_length=16)
	text = forms.CharField( widget=forms.Textarea(), max_length=1000)
	algoritm = forms.ChoiceField(choices=[('cifrar', 'cifrar'), ('descifrar', 'descifrar')], widget=forms.RadioSelect())

class CheckForm(forms.Form):
	text = forms.CharField( widget=forms.Textarea())