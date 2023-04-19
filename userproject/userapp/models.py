from django.db import models

# Create your models here.
class postwork(models.Model):
    post_name = models.TextField(max_length=10)
    post_date = models.DateField(auto_created=True)
    post_disc = models.TextField(max_length=600)
    post_poster = models.FileField(upload_to="static/posters")

class carausel(models.Model):
    image= models.ImageField(upload_to="static/carausel")
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=600)

    def __str__(self):
        return self.title
