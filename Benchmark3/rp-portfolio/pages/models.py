#########################
#####
##### MODELS FOR ADMIN PAGE
#####
#########################


from django.db import models

#test model for edit site
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
