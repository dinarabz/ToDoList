from django.db import models
from django.utils import timezone
from django.db.models import TextChoices


# Create your models here.
class Article(models.Model):
    summary = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Текст"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True, default=None
    )
    type = models.ForeignKey(
        to='webapp.Tag',
        related_name='type',
        verbose_name='Тип'
    )
    status = models.ForeignKey(
        'webapp.Status',
        related_name='status',
        on_delete=models.RESTRICT,
        verbose_name='Статус'
    )

    def __str__(self):
        return f"{self.summary} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
