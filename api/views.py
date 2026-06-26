from django.shortcuts import render, redirect
from .models import Project, Contact
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Message sent successfully! I will reply soon 🚀')
        return redirect('home') 
    
    projects = Project.objects.all()
    return render(request, 'api/home.html', {'projects': projects})