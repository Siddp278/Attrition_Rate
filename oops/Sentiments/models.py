from django.db import models

# Create your models here.
class sentiment(models.Model):
    table_id = models.AutoField(primary_key=True)
    sentiment1 = models.CharField(max_length=500, default='not filled', blank=True, null=True)
    sentiment2 = models.CharField(max_length=500, default='not filled', blank=True, null=True)
    sentiment3 = models.CharField(max_length=500, default='not filled', blank=True, null=True)
    sentiment4 = models.CharField(max_length=500, default='not filled', blank=True, null=True)
    sentiment5 = models.CharField(max_length=500, default='not filled', blank=True, null=True)

    objects = models.Manager()
    def __int__(self):
        return self.table_id


class attrition_upload(models.Model):
    tables_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, default='example') # take the username of the uploader
    file_name = models.CharField(max_length=100)
    date_of_upload = models.DateField(auto_now_add=True)
    file_upload = models.FileField(upload_to='HR')

    def __int__(self):
        return self.tables_id

    def delete(self, *args, **kwargs):
        self.file_upload.delete()
        super().delete(*args, **kwargs)
