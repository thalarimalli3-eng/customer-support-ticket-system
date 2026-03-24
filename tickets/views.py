
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm

def home(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request,'home.html',{'tickets':tickets})

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request,'create_ticket.html',{'form':form})
