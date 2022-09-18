"""bookingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booking_app.views import AddRoomView, ShowAllRooms, ShowDetails, ModifyRoom, DeleteRoom, ReserveRoom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/new', AddRoomView.as_view(), name='add_room'),
    path('room/all', ShowAllRooms.as_view(), name='all_rooms'),
    path('room/<int:id>', ShowDetails.as_view(), name='details_rooms'),
    path('room/modify/<int:id>/', ModifyRoom.as_view(), name='modify_room'),
    path('room/delete/<int:id>/', DeleteRoom.as_view(), name='delete_room'),
    path('room/reserve/<int:id>/', ReserveRoom.as_view(), name='reserve_room'),
]
