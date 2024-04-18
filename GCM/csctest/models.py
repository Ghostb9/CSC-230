# Create your models here.
from django.db import models


class Exhibit(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='html_pages_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class TypeofPlay(models.Model):
    TypeID = models.IntegerField(primary_key=True)
    TypeName = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        db_table = 'TypeOfPlay'

    def __str__(self):
        return self.TypeName


class Activity(models.Model):
    ActivityID = models.AutoField(primary_key=True)
    activityName = models.CharField(max_length=255)
    category = models.ForeignKey(TypeofPlay, on_delete=models.CASCADE, db_column='Category')
    subcategory = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = 'Activities'  # The name of your table

    def __str__(self):
        return self.activityName
