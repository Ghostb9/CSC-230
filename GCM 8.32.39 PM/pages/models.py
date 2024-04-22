from django.db import models


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
    Description = models.CharField(max_length=500)

    class Meta:
        db_table = 'TypeOfPlay'

    def __str__(self):
        return self.TypeName
