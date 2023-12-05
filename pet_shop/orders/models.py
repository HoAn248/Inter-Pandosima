from django.db import models
from users.models import User
from pets.models import Pet
class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    petid = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='orders')
    des = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.userid.fullname} - {self.petid.name}"
    class Meta:
        ordering = ['created']
    
        
