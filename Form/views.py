from django.shortcuts import render
from Form.models import Formulaire
from Form.forms import TaskFormulaire
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def post_list(request):
    return render(request, 'Form/post_list.html', {})

def home_view(request):
    form = 0
    if request.method == 'POST':
        form = TaskFormulaire(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {}
    context['form'] = TaskFormulaire()
    return render(request, "Form/home.html", context)

