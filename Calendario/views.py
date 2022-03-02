from pyexpat import model
from urllib import request
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.views.generic import TemplateView
from django.http import HttpResponse, request
from Calendario.forms import CalendarioForm, AnuncioForm,SignUpForm
from django.views.generic.list import ListView
from .models import anuncio, calendario
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            
            user = authenticate(username=username, password=password)

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                print("si entro el usuario ")
                return redirect('dashboard')

    # Si llegamos al final renderizamos el formulario
    return render(request, "Calendario/auth-login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

class dasboardView(TemplateView):
    template_name = 'Calendario/index.html'
    #aqui ingresa en el caso de que se necesite traer datos 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        calForm=CalendarioForm()
        context["calendario"]=  calForm;
        return context
        
@login_required(login_url="/login/")
def guardarEvento(request):
    print(request.method)
    active=1
    data = {
        'calendario': CalendarioForm,
        'active':active}
    if request.method == "POST":
        form = CalendarioForm(request.POST)     
        if form.is_valid():
            form.save()
            dir = 'dashboard'
            return redirect(dir)
        else:
            print(form.errors)


    return render(request, 'Calendario/FormularioCalendar.html', data)

class CalendarioListView(ListView):
    model = calendario
    paginate_by = 100  # if pagination is desired
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active=1
        context['est'] = calendario.objects.all()
        context['active']=active
        return context

class CalendarioUpdateView(UpdateView):
    # specify the model you want to use
    model = calendario
    form_class = CalendarioForm
    success_url='/'


class AnuncioCreateView(CreateView):
    model=anuncio

    fields = ['fecha_publicacion','imagen','descripcion']

@login_required(login_url="/login/")
def guardarAnuncio(request):
    form = AnuncioForm(request.POST or None, request.FILES or None)
    active=2
    if form.is_valid():
        form.save()
        dir = 'list_anuncio'
        return redirect(dir)
    else:
        print(form.errors)

    return render(request, 'Calendario/FormularioAnuncio.html',  {'form':form,'active':active})

class AnuncioListView(ListView):
    model = anuncio
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active=2
        context['anuncio'] = anuncio.objects.all()
        context['active']=active
        return context


def image_delete(request, pk, template_name='gallery/confirm_delete.html'):
    image = get_object_or_404(anuncio, pk=pk)
    image.delete()
    return redirect('list_anuncio') 





def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'Usuario Creado- <a href="/login">Inicie Sesion</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Ocurrio un error revise los campos'    
    else:
        form = SignUpForm()

    return render(request, "Calendario/auth-register.html", {"form": form, "msg" : msg, "success" : success })