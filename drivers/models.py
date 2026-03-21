from django.db import models


class DriverModel(models.Model):
    CAR_CHOICES = (
        ('sedan', 'Седан'),
        ('suv', 'Внедорожник'),
        ('truck', 'Грузовой'),
    )

    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    photo = models.ImageField(upload_to='drivers_photos/', verbose_name="ФОТО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    car_choice = models.CharField(max_length=20, choices=CAR_CHOICES, verbose_name="Выбор машины")
    experience = models.PositiveIntegerField(verbose_name="Водительский стаж (лет)")
    has_license = models.BooleanField(default=False, verbose_name="Наличие прав (Да/Нет)")

    def __str__(self):
        return self.full_name