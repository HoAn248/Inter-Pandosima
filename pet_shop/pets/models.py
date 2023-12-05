from django.db import models

class Pet(models.Model):
    petid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.FloatField()
    title = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created']
