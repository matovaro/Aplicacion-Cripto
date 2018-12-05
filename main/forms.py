from django import forms

class Algoritm(forms.Form):
	key = forms.CharField(max_length=16)
	text = forms.CharField( widget=forms.Textarea())
	algoritm = forms.ChoiceField(choices=[('cifrar', 'cifrar'), ('descifrar', 'descifrar')], widget=forms.RadioSelect())