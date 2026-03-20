from django.db import models
from books.models import Books



class OrderBook(models.Model):
    name_order = models.CharField(max_length=100, default='Иван Иванов')
    choices_book = models.ForeignKey(Books, on_delete=models.CASCADE)
    number_card = models.PositiveIntegerField()
    STATUS_ORDER = (
        ("Уверен","Уверен"),
        ("Отказ","Отказ"),
        ("Подумаю","Подумаю")
    )

    status_order = models.CharField(max_length=100, choices=STATUS_ORDER)
    create_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f'{self.name_order}: {self.choices_book}'