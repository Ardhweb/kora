from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_questions')
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(null=True,blank=True, max_length=560)


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField(null=True,blank=True, max_length=960)
    likes = models.PositiveIntegerField(null=True, blank=True)



