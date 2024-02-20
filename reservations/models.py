from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Reservation(models.Model):
    select_service = (
        ('Spa', 'Spa'),
        ('Aromatherapy', 'Aromatherapy'),
        ('Massage', 'Massage'),
        ('Yoga', 'Yoga'),
    )
    select_hour = (
        ('9:00', '9:00'),
        ('11:00', '11:00'),
        ('14:00', '14:00'),
        ('16:00', '16:00'),
    )


    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    service = models.CharField(max_length=15, choices=select_service)
    date = models.DateTimeField('XYZ DateTime')
    hour = models.CharField(max_length=15, choices=select_hour)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        string = str(self.date) + " " + self.hour  + " " + self.service  + " " + self.name + " " + self.surname
        return  string