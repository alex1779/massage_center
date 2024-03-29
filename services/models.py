from django.db import models

# Create your models here.


class Service(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=400)
    image=models.ImageField(upload_to='services')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Service'
        verbose_name_plural='Services'

    def __str__(self):
        return self.title