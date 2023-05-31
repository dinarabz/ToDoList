from django.db import models
from django.db.models import TextChoices


class TypeChoice(TextChoices):
    TASK = "Task", "задача"
    BUG = "Bug", "ошибка"
    ENHANCEMENT = 'Enhancement', 'улучшение'


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Тип"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return self.name

