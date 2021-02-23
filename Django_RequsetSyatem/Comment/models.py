from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from Login.models import LoginUser
from RequstAnswer.models import RequestInfo
from ckeditor.fields import RichTextField

# Create your models here.

class Comment(MPTTModel):
    Project = models.ForeignKey(
        RequestInfo,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        LoginUser,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    reply_to = models.ForeignKey(
        LoginUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.body[:20]
