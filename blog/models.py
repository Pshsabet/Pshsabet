from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
# Create your models here.

class post(models.Model):
    CHOICES = (
        ("d", "Draft"),
        ("p", "Published"),
        ("n", "None"),
    )
    title = models.CharField(max_length= 200, unique=True)
    slug = models.SlugField(max_length= 100, unique= True)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length= 1, choices= CHOICES)
    def __str__(self):
        return self.title
    