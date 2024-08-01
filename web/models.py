from django.db import models


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
    