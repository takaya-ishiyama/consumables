from django.db import models
from django.utils import timezone

# Create your models here.

class Items(models.Model):
    id=models.AutoField(primary_key=True, unique=True, null=False, blank=False)
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media/' ,null=True, blank=True)
    status=models.IntegerField(null=True, blank=True)
    text=models.TextField(max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name