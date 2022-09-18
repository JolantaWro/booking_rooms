from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    size_room = models.PositiveIntegerField()
    availability_projector = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
