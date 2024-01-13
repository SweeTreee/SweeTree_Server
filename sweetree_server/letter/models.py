from django.db import models


class Letter(models.Model):
    box_id      = models.ForeignKey('box.Box', on_delete=models.CASCADE, verbose_name="Box id")
    choco_type  = models.CharField(max_length=4, verbose_name="Choco type")
    nickname    = models.CharField(max_length=20, verbose_name="Nickname")
    contents    = models.TextField(verbose_name="Contents")
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    ip_address  = models.GenericIPAddressField(null=True, editable=False)

    class Meta:
        db_table = 'letter'
