from django.db import models
from django.urls import reverse

# Create your models here.
class Walls(models.Model):
    title = models.CharField('Название', max_length=55, blank=True)
    wall = models.ImageField("Обои", upload_to = 'walls/%Y/%m/%d/')
    date = models.DateField('Дата публикации', auto_now_add=True)
    is_published = models.BooleanField(default=True)
    cat = models.ManyToManyField("Category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content-id', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Обои"
        verbose_name_plural = 'Обои'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']