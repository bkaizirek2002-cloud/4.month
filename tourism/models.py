from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name

class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название тура")
    description = models.TextField(verbose_name="Описание")
    categories = models.ManyToManyField(Category, related_name='tours', verbose_name="Категории")

    def __str__(self):
        return self.title

class Tourist(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя туриста")
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE, verbose_name="Тур")

    def __str__(self):
        return self.name

class Review(models.Model):
    text = models.TextField(verbose_name="Отзыв")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews', verbose_name="Тур")

    def __str__(self):
        return f"Отзыв к {self.tour.title}"