from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import List, Client
from .forms import FormClient,FormList,FormRegister
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login ,logout
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='connexion')
def home(request):
    return render(request, 'home.html')
def est_Propriétaire(user):
    return user.groups.filter(name='Propriétaire').exists() or user.is_superuser

@login_required(login_url= 'connexion' )


@login_required(login_url='connexion')
def listerListe(request):
   
    if est_Propriétaire(request.user):
        listes = List.objects.all().order_by('-date')
    else:
       
        try:
            client_obj = Client.objects.get(email=request.user.email)
            listes = List.objects.filter(client=client_obj).order_by('-date')
        except Client.DoesNotExist:
            listes = []  # إلا ما لقيناش Client بهاد email
    
    return render(request, 'liste.html', {'listes': listes})
@login_required(login_url= 'connexion' )
def listerClient(request):
    clients=Client.objects.all()
    return render(request,'client.html',{'clients':clients})

@login_required(login_url= 'connexion' )
@user_passes_test(est_Propriétaire, login_url='connexion')

def AjouterListe(request):
    if request.method=="POST":
        form=FormList(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listerListe')
    else:
        form=FormList()
    return render(request,'forms.html',{'form':form , 'titre':"ajouter liste"})

@login_required(login_url= 'connexion' )
@user_passes_test(est_Propriétaire, login_url='connexion')
def AjouterClient(request):
    if request.method=="POST":
        form=FormClient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listerClient')
    else:
        form=FormClient()
    return render(request,'forms.html',{'form':form , 'titre':"ajouter aide"})

@login_required(login_url= 'connexion' )
@user_passes_test(est_Propriétaire, login_url='connexion')
def ModifierListe(request,pk):
    data=get_object_or_404(List, num=pk)
    if request.method=="POST":
        form=FormList(request.POST ,instance=data)
        if form.is_valid():
            form.save()
            return redirect('listerListe')
    
    else:
        form=FormList(instance=data)
    return render(request,'forms.html',{'form':form,'titre':"modofier liste"})

@login_required(login_url= 'connexion' )
@user_passes_test(est_Propriétaire, login_url='connexion')
def ModifierClient(request,pk):
    data=get_object_or_404(Client,num=pk) 
    if request.method=="POST":
        form=FormClient(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('listerClient')
    else:
        form=FormClient(instance=data)
    return render(request,'forms.html',{'form':form,'titre':"modifier  aide "})

@login_required(login_url= 'connexion' )
@user_passes_test(est_Propriétaire, login_url='connexion')
def SupprimerListe(request,pk):
    data=get_object_or_404(List,num=pk)
    if request.method=="POST":
        data.delete()
        return redirect('listerListe')
    return render(request,'confirm.html',{'data':data})

@login_required(login_url= 'connexion' )
@user_passes_test(est_Propriétaire, login_url='connexion')
def SupprimerClient(request,pk):
    data=get_object_or_404(Client,num=pk)
    if request.method=="POST":
        data.delete()
        return redirect('listerClient')
    return render(request,'confirm.html',{'data':data})

def register(request):
    if request.method=="POST":
        form=FormRegister(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html',{'form':form})
    else:
        form=FormRegister()
    return render(request,'register.html',{'form':form})

def connexion(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return render(request,'home.html',{'form':form})
    else:
        form=AuthenticationForm()
    return render(request,'connexion.html',{'form':form})

def deconnexion(request):
    logout(request)
    return redirect('connexion')

