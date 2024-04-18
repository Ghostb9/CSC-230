from django.db import models
from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Exhibit(models.Model):
    ExhibitID = models.IntegerField(primary_key=True)  # Assuming ExhibitID is your primary key
    ExhibitName = models.CharField(max_length=100)
    Location = models.CharField(max_length=50)

    class Meta:
        db_table = 'Exhibit'

    def __str__(self):
        return self.ExhibitName


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

# This model is for storing time spent on different pages by the user
class PageTimeSpent(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.CharField(max_length=2048)
    time_spent = models.IntegerField(help_text="Time spent in milliseconds")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} spent {self.time_spent} on {self.url}"
