from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify
from core.models import BaseModel

class Topic(BaseModel):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True, max_length=250)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class InterestedTopic(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username