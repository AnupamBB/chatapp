from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib.auth.forms import UserCreationForm

def rooms(request):
    rooms = Room.objects.all()
    return render(request, "rooms.html", {"rooms": rooms})

def room(request, slug):
    room_name = Room.objects.get(slug=slug).name
    messages = Message.objects.filter(room=Room.objects.get(slug=slug))
    return render(request, "room.html", {"room_name": room_name, "slug": slug, "messages": messages})

def register(request):
    form = UserCreationForm()  # Initialize the form outside the if statement

    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Pass request.POST to the form
        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, "registration/register.html", {'form': form})
