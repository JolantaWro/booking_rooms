from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from booking_app.models import Room


class AddRoomView(View):

    def get(self, request):
        return render(request, template_name='add_room.html')

    def post(self, request):
        name = request.POST.get('name')
        size_room = request.POST.get('size')
        size_room = int(size_room) if size_room else 0
        availability_projector = request.POST.get('projector') == 'on'
        if not name:
            message = f"<h2> Name cannot be empty"
            return HttpResponse(message)
        if Room.objects.filter(name=name).first():
            message = f"<h2> The name already exists in the database"
            return HttpResponse(message)
        if size_room <= 0:
            message = f"<h2> An incorrect value has been entered"
            return HttpResponse(message)

        new_room = Room.objects.create(name=name, size_room=size_room, availability_projector=availability_projector)
        return redirect('all_rooms')


class ShowAllRooms(View):
    def get(self, request):
        rooms_all = Room.objects.all()
        return render(request, template_name='all_rooms.html', context={'rooms': rooms_all})


class ShowDetails(View):
    def get(self, request, id):
        rooms = Room.objects.get(pk=id)
        return render(request, template_name='room_details.html', context={'rooms': [rooms]})

class ModifyRoom(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        return render(request, template_name='modify_room.html', context={'room': room})

    def post(self, request, id):
        edit_room = Room.objects.get(pk=id)
        name = request.POST.get('name')
        size_room = request.POST.get('size')
        size_room = int(size_room) if size_room else 0
        availability_projector = request.POST.get('projector') == 'on'
        if not name:
            message = f"<h2> Name cannot be empty"
            return HttpResponse(message)
        if name != edit_room.name and Room.objects.filter(name=name).first():
            message = f"<h2> The name already exists in the database"
            return HttpResponse(message)
        if size_room <= 0:
            message = f"<h2> An incorrect value has been entered"
            return HttpResponse(message)

        edit_room.name = name
        edit_room.size_room = size_room
        edit_room.availability_projector = availability_projector
        edit_room.save()
        return redirect('all_rooms')

class DeleteRoom(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        room.delete()
        return redirect("all_rooms")

class ReserveRoom(View):
    pass




