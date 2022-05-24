from email import message
from pyexpat.errors import messages
from django.shortcuts import render
from .models import Message

def chat(request):
  return render(request, '/home/aditya/Desktop/Django/LawyerScheduler_guptaV2/templates/chat/index.html')

def room(request, room_name):
  username = request.GET.get('username', 'Anonymous')
  messages = Message.objects.filter(room=room_name)[0:25]

  return render(request, '/home/aditya/Desktop/Django/LawyerScheduler_guptaV2/templates/chat/room.html', {'room_name': room_name, 'username': username , 'messages': messages })
