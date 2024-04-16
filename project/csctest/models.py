

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class Exhibit(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='html_pages_images/', blank=True, null=True)

    def __str__(self):
        return self.title