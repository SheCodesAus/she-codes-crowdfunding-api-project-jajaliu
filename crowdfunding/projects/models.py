from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200, blank=True, default='')
    cuisine = models.CharField(max_length=200, default='')
    goal = models.FloatField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'owner_projects'
    )


class Pledge(models.Model):
    amount = models.FloatField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete = models.CASCADE,
        related_name = 'pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'supporter_pledges'
    )

