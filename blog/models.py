from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    creation_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def summary(self):
        return self.body[:100] + "..."

    def pretty_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def pretty_create_date(self):
        return self.creation_date.strftime('%b %e %Y')