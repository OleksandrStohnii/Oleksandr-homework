from django.db import models


class Category(models.Model):
    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField("Название работы", max_length=200)
    description = models.TextField("Описание", blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="works",
        verbose_name="Категория",
    )
    image = models.ImageField("Фото", upload_to="works/", blank=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title