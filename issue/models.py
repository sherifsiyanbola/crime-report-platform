from django.db import models
from django.urls import reverse


# Create your models here.
class IssueCrime(models.Model):
    DUTSE = 'dutse'
    BIRNINKUDU = 'bkd'
    HADEJIA = 'hadejia'
    RINGIM = 'ringim'
    GUMEL = 'gumel'
    KAZAURE = 'kazaure'
    
    LGA = [
       (DUTSE, ('DUTSE')),
       (BIRNINKUDU, ('BIRNINKUDU')),
       (HADEJIA, ('HADEJIA')),
       (RINGIM, ('RINGIM')),
       (GUMEL, ('GUMEL')),
       (KAZAURE, ('KAZAURE')),
   ]
    
    crime_title = models.CharField(max_length = 255)
    crime_description = models.TextField()
    # date = models.DateTimeField(auto_now_add = True)
    crime_location = models.CharField(max_length = 255, default='Jigawa')
    lga = models.CharField(
       max_length=32,
       choices=LGA,
       default=DUTSE,
   )
    street_address = models.CharField(max_length = 255)
    date = models.DateTimeField()
    phone_number = models.CharField(max_length = 50)
    treated = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.crime_title