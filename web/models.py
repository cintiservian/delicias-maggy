from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class tartas(models.Model):
    tartas_uuid= models.UUIDField() #del tipo UUIDField
    name= models.CharField (max_length=64)   #del tipo CharField (largo máximo 64 caracteres)
    description= models.TextField()
    image_url= models.URLField()   # del tipo URLField
    slug= models.SlugField()  # del tipo SlugField
    is_private= models.BooleanField()  # del tipo BooleanField
    precio = models.DecimalField(max_digits=10, decimal_places=2,default=10.00)
    def _str_(self):
        return self.name
    

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


class Favoritos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarta = models.ForeignKey(tartas, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tarta')
   
   
   