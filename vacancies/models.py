from django.db import models

class ITSpecialist(models.Model):
    STACK_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('devops', 'Devops'),
        ('design', 'UX/UI Desing'),

    ]

    full_name = models.CharField(max_length=100, verbose_name = "ФИО")
    email = models.EmailField(verbose_name = "Электронная почта")
    phone = models.CharField(max_length=20, verbose_name = "Номер телофона")
    specialization = models.CharField(max_length=20, choices=STACK_CHOICES, verbose_name="Специализация")
    experience_years = models.PositiveIntegerField(verbose_name="Стаж работы(лет)")
    github_url = models.URLField(verbose_name="Ссылка на GitHub")
    portfolio_url = models.URLField(verbose_name="Ссылка на портфолио", blank=True, null=True)
    bio = models.TextField(verbose_name="О себе ")
    resume = models.FileField(upload_to='resumes/', verbose_name="Файл резюме")
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ожидаемая ЗП")
    birth_date = models.DateField(verbose_name= "Дата рождения")
    is_ready_to_relocate = models.BooleanField(default=False, verbose_name="Готов к переезду")

    def __str__(self):
        return self.full_name

 