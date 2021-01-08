from django.db import models

from .validators import MinMaxValueValidator


class Bb(models.Model):
    KINDS = (
        ('b', 'Куплю'),
        ('s', 'Продам'),
        ('c', 'Обменяю'),
    )
    title = models.CharField(max_length=50, verbose_name='Товар')
    # текстовое поле неограниченной длины, или memo-поле. Присвоив
    # параметрам null и blank конструктора значения True , мы укажем, что это поле
    # можно не заполнять (по умолчанию любое поле обязательно к заполнению);
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена',
                              validators=[MinMaxValueValidator(1000, 6000000)])
    # DateTimeField — поле для хранения временнóй отметки. Присвоив параметру
    # конструктора значение True , мы предпишем Django при создании
    # новой записи заносить в это поле текущие дату и время. А параметр db_index
    # при присваивании ему значения True укажет создать для этого поля индекс (при
    # выводе объявлений мы будем сортировать их по убыванию даты публикации,
    # и индекс здесь очень пригодится).
    kind = models.CharField(max_length=1, choices=KINDS, default='s',
                            verbose_name='Тип')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')

    def __str__(self):
        return self.title

    def get_type(self):
        for kind in self.KINDS:
            if kind[0] == self.kind:
                return kind[1]

    class Meta:
        # название модели во множественном числе;
        verbose_name_plural = 'Объявления'
        # название модели в единственном числе;
        verbose_name = 'Объявление'
        # последовательность полей, по которым по умолчанию будет
        # выполняться сортировка записей
        ordering = ['published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
