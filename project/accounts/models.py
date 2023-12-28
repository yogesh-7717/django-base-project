from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    note = models.TextField(max_length= 300)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title