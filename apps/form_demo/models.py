from django.db import models
from django.contrib.auth.models import User

class FormDemo(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
