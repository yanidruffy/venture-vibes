from django.db import models

# Create your models here.


class About(models.Model):
    """
    Represents the About page content.
    """
    title = models.CharField(max_length=250)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
