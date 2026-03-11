from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Car(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название машины")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='cars/', verbose_name="Фото")
    price = models.PositiveIntegerField(verbose_name="Цена")
    year = models.IntegerField(validators=[MinValueValidator(1886), MaxValueValidator(2026)])
    engine_volume = models.FloatField(verbose_name="Оъем двигателя")
    color = models.CharField(max_length=50, blank=True, null=True)
    is_electric = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=50, default="Unknown")

    def __str__(self):
        return self.title