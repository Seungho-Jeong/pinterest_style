from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=256, null=True)
    image = models.ImageField(upload_to='project/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.pk, self.title)