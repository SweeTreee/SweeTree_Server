from django.db import models
from django.conf import settings


class Box(models.Model):
    user_id         = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    box_name        = models.CharField(max_length=20, null=False)
    box_type        = models.CharField(max_length=10, default='None')
    is_box_public   = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'box'
