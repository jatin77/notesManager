from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    #  Choices of priority
    CRITICAL = 0
    MAJOR = 1
    MODERATE = 2
    LOW = 3
    STATUS = (
        (CRITICAL, ('Urgent')),
        (MAJOR, ('Major')),
        (MODERATE, ('Moderate')),
        (LOW, ('Low'))
    )
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    priority = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=MODERATE,
    )
    owner = models.ForeignKey(User, related_name='posts',
                              on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
