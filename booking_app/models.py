from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    size_room = models.PositiveIntegerField()
    availability_projector = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_reservation = models.DateField()
    description = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'date_reservation')
