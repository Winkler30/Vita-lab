from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def solicitar_exames(request):
    if request.method == "GET":
        return render(request, 'solicitar_exames.html')