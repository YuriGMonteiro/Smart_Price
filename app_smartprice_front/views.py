from django.shortcuts import render
from .forms import RegisterForm

def home(request):
    cadastro = RegisterForm()
    context = {}
    context['cadastro_usuario'] = cadastro
    
    if request.method == "POST":
        registro_usuario = RegisterForm(request.POST)
        if registro_usuario.is_valid():
            registro_usuario.save()
    
    return render(request, "pages/home.html", context=context)
