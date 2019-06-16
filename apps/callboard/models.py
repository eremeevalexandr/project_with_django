from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    """Модель категорий обьявлений"""
    name = models.CharField(verbose_name = "Название категории", max_length=100, unique=True)
    slug = models.SlugField(verbose_name = "Алиас", max_length=100, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by=['name']
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Adverts(models.Model):
    """Модель объявлений"""
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Имя объявления", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"