from django.db import models


class Letter(models.Model):
    title       = models.CharField(max_length=255, verbose_name="Title")
    content     = models.TextField(verbose_name="Content")
    x           = models.FloatField(verbose_name="Longitude")
    y           = models.FloatField(verbose_name="Latitude")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    ip_address  = models.GenericIPAddressField(null=True, editable=False)

    class Meta:
        db_table = 'letter'
