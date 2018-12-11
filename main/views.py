from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Save
from django.shortcuts import get_object_or_404, render
from .forms import Algoritm, CheckForm
from django.utils import timezone
from .aesAlgoritm import encryp, decrypt
from .RSA import sign, ver

from .tbca import TBCA

"""def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render((request)))

"""
def index(request):
    return render(request, 'main/index.html')

def aes(request):	
	if request.method == "POST":
		form = Algoritm(request.POST)
		if form.is_valid():
			key = form.cleaned_data['key']
			text = form.cleaned_data['text']
			algoritm = form.cleaned_data['algoritm']
			modo = ''

			if(algoritm == 'cifrar'):
				men = encryp(text,key)
				modo = 'cifrado'
				firma = sign(text + key)
				f= open("firma.txt","w")
				f.write(firma)
				f.close()
			else:
				men = decrypt(text,key)
				modo = 'decifrado'

			result = {
					'key': key,
					'text': text,
					'algoritm': algoritm,
					'men': men,
					'modo': modo
			}

			
			s = Save(text_plain=text, cipher_text=men, algoritm=1, date=timezone.now())
			s.save()
			return render(request, 'main/result.html', result)

	form = Algoritm()
	return render(request, 'main/aes.html', {'form': form})

def eoa(request):	
	if request.method == "POST":
		form = Algoritm(request.POST)
		if form.is_valid():
			key = form.cleaned_data['key']
			text = form.cleaned_data['text']
			algoritm = form.cleaned_data['algoritm']
			modo = ''
			#implementar algoritmo
			#print(key, text, algoritm)
			men = "mensaje"

			
			tbca = TBCA()
			iv = '12345678'

			if(algoritm == 'cifrar'):
				men = tbca.cifrar(text,key,iv)
				modo = 'cifrado'
			else:
				men = tbca.descifrar(text, key,iv)
				modo = 'decifrado'



			result = {
				'key': key,
				'text': text,
				'algoritm': algoritm,
				'men': men,
				'modo': modo
			}
			s = Save(text_plain=text, cipher_text=men, algoritm=2, date=timezone.now())
			s.save()
			return render(request, 'main/result.html', result)

	form = Algoritm()
	return render(request, 'main/eoa.html', {'form': form})



def detail (request, save_id):
	return HttpResponse('estas viendo el registro numero %s' % save_id)
def firma(request):
	f= open("firma.txt","r")
	firma = f.read()
	f.close()
	return HttpResponse(firma, content_type="text/plain")

#!/usr/bin/python
# -*- coding: utf-8 -*-


def verification(request):
    
	if request.method == 'POST':
		form = CheckForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['text']
			ans = ver(text)
			if ans == 0:
				result = "Certificado no Valido"
			else:
				result = ans
			return render(request, 'main/verifier.html', {'text': result})
		else:
			print(form)
	form = CheckForm()
	return render(request, 'main/ver.html', {'form': form})