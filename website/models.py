from django.db import models
from datetime import datetime 

# Create your models here.
class Service(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True )
    description_1 = models.CharField(null=True, blank=True, max_length=300)
    date_1 = models.DateTimeField(default=datetime.now, blank=True)

    description_2 = models.CharField(null=True, blank=True, max_length=300)
    date_2 = models.DateTimeField(default=datetime.now, blank=True)

    description_3 = models.CharField(null=True, blank=True, max_length=300)
    date_3 = models.DateTimeField(default=datetime.now, blank=True)

    description_4 = models.CharField(null=True, blank=True, max_length=300)
    date_4 = models.DateTimeField(default=datetime.now, blank=True)

    description_5 = models.CharField(null=True, blank=True, max_length=300)
    date_5 = models.DateTimeField(default=datetime.now, blank=True) 





    def __str__(self):
        return self.title
