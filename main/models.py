from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    icon = models.ImageField(upload_to="icons/")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self) -> str:
        return f"{self.title}"
