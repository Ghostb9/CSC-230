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
    ExhibitName = models.ForeignKey(Exhibit, on_delete=models.CASCADE, db_column='ExhibitName')

    class Meta:
        db_table = 'Activities'  # The name of your table

    def __str__(self):
        return self.activityName


from django.db import models

"""""""""""
class TimeStamp(models.Model):
    # Assuming "UserID" is a foreign key to a user model
    UserID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Assuming "CurrentTime" is a timestamp field with date and time
    CurrentTime = models.DateTimeField()
    # Assuming "ChildID" is a foreign key to another model representing a child
    ChildID = models.ForeignKey('ChildID', on_delete=models.CASCADE)
    # Assuming "ExhibitID" is a foreign key to another model representing an exhibit
    ExhibitID = models.ForeignKey('ExhibitID', on_delete=models.CASCADE)

    class Meta:
        db_table = 'TimeStamp'  # Ensure the table name matches the one in MySQL

    def __str__(self):
        return f"TimeStamp({self.user}, {self.current_time}, {self.child}, {self.exhibit})"
"""""""""""""""""