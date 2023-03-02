from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def index(request):
    # voiture_list = Voiture.objects.all()
    # context = {'voiture_list': voiture_list}
    return render(request, 'index.html')