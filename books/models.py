from django.db import models

class Books(models.Model):
    name_book = models.CharField(max_length=50, verbose_name='укажите навание книги')
    description = models.TextField(verbose_name='укажите описание книги')
    imagiine = models.ImageField(upload_to='books/', verbose_name='загужите обложку')

    
    CATEGORY_BOOK = [
        ('фантакстика','фантастика'),
        ('хоррор','хоррор'),
        ('исторические','исторические')
    ]

    category_book = models.CharField(max_length=100 ,choices=CATEGORY_BOOK, verbose_name='выберите категорию')

    url_audio_book = models.URLField(verbose_name='укажите ссылку на аудиокнигу')

    views = models.PositiveIntegerField(default=0, null=True)

    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_book

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'книги'