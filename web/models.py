from django.db import models
import uuid

# Create your models here.
class tartas(models.Model):
    tartas_uuid= models.UUIDField() #del tipo UUIDField
    name= models.CharField (max_length=64)   #del tipo CharField (largo máximo 64 caracteres)
    description= models.TextField()
    image_url= models.URLField()   # del tipo URLField
    slug= models.SlugField()  # del tipo SlugField
    is_private= models.BooleanField()  # del tipo BooleanField

    def _str_(self):
        return self.name
    

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_name} ({self.customer_email})"  
    