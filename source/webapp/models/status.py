from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = "New", "новый"
    IN_PROGRESS = "In Progress", "в процессе"
    DONE = 'Done', 'выполнено'


class Status(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        choices=StatusChoice.choices,
        default=StatusChoice.NEW,
        verbose_name="Статус"
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
