from django.shortcuts import render
from Form.models import Formulaire
from Form.forms import TaskFormulaire
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from Form.pdf2 import sendMail3

# Create your views here.
def post_list(request):
    if request.method == 'POST':
        form = TaskFormulaire(request.POST, request.FILES)
        if form.is_valid():
            sendMail3(request)
            form.save()
            print('réussi')
            return HttpResponseRedirect('/')

    context = {}
    context['form'] = TaskFormulaire()
    return render(request, 'Form/post_list.html',context)

def accueil_view(request):
    return render(request, "Form/accueil.html",{})

