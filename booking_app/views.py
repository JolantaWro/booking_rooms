from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from booking_app.models import Room, Reservation
import datetime


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
        date_view = datetime.date.today()
        for room in rooms_all:
            reserve_date = [r.date_reservation for r in room.reservation_set.all()]
            room.booking = False
            if date_view in reserve_date:
                room.booking = True
        return render(request, template_name='all_rooms.html', context={'rooms': rooms_all})


class ShowDetails(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        reservations = room.reservation_set.filter(date_reservation__gte=str(datetime.date.today()))
        reservations.order_by('date_reservation')
        return render(request, template_name='room_details.html', context={'room': room, 'reservations': reservations})

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
    def get(self, request, id):
        room = Room.objects.get(pk=id)

        return render(request, template_name='add_reserve.html', context={'room': room})

    def post(self, request, id):
        room_id = Room.objects.get(pk=id)
        description = request.POST.get("description")
        date_reserve = request.POST.get("date_reserve")
        if Reservation.objects.filter(room_id=room_id, date_reservation=date_reserve):
            message = f"<h2> The room is unavailable"
            return HttpResponse(message)
        if date_reserve < str(datetime.date.today()):
            message = f"<h2> Booking date error"
            return HttpResponse(message)

        reserve_room = Reservation.objects.create(room_id=room_id, date_reservation=date_reserve, description=description)
        reserve_room.save()
        return redirect("all_rooms")






