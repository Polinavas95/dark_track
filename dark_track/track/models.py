from django.db import models


class

class TractorTrack(models.Model):
    self_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.pk)
