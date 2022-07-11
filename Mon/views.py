from django.shortcuts import render
from Form.models import Formulaire
# Create your views here.



def index(request):

    if request.user.is_authenticated:

        user = request.user
        queryset = Formulaire.objects.all()

        context = {
            "object_list": queryset,
            "user": user
        }

        return render(request, "index.html", context)