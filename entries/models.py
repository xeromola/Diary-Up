from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date_created = models.DateField()
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"
