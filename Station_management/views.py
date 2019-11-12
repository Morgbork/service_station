from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponse, redirect
from .models import Clients, Cars, Orders
from .forms import SearchClientForm, RegistrationForm
from django.db.models import Q

def main_page(request):
    form = SearchClientForm()
    return render(request, 'Station_management/base.html', {'form':form})

def clients_search(request):
    form = SearchClientForm(request.POST)
    if form.is_valid():
        full_name = form.cleaned_data['search_field']
    full_name_list=full_name.split(' ')
    search_result = get_list_or_404(Clients, Q(first_name=full_name_list[0]) & Q(last_name=full_name_list[1]))
    return render(request, 'Station_management/clients.html', {
         'search_result': search_result
    })

def registration_view(request):
    form = RegistrationForm()
    return render(request, 'Station_management/registration.html', {'form':form})

def registration_procedure(request):
    form = RegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse(content=b'Fine!')
    
        return render(request, 'Station_management/registration.html', {'form':form})

def client_card(request, first_name, id):
    client = get_object_or_404(Clients, id=id, first_name=first_name)
    client_cars = Cars.objects.filter(owner = client.id)
    return render(request, 'Station_management/client_card.html', {'client':client, 'client_cars':client_cars})