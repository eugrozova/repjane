from django.shortcuts import render
from .models import Dataentries

def index(request):
    dataentries = Dataentries.objects.all()
    context = {
        'dataentries': dataentries
    }
    return render(request, 'index.html', context)
# Create your views here.
