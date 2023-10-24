from django.db import models

class WorkpieceEvent(models.Model):
    WORKSTATIONS = [
        ('CUT', 'Cutting'),
        ('ASM', 'Assembling'),
        ('PKG', 'Packing'),
    ]

    workpiece_id = models.CharField(max_length=100)
    workstation = models.CharField(choices=WORKSTATIONS, max_length=3)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
