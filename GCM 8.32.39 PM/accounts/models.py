from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"


class Child(models.Model):
    GENDER_CHOICES = (
        ('boy', 'Boy'),
        ('girl', 'Girl'),
        ('not_say', 'Prefer not to say'),
    )

    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='children')
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='not_say')

    def __str__(self):
        return self.name
