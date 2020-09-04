from django.db import models
from django.urls import reverse

from clubcard.func import generate_club_card_number, add_time, add_balance


class Sex(models.Model):
    """ Модель половой принадлежности человека """
    gender = models.CharField(verbose_name='Пол', max_length=10)

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class User(models.Model):
    """Модель для хранения информации о клиенте"""
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, )
    name = models.CharField(verbose_name='Имя', max_length=50, )
    fathers_name = models.CharField(verbose_name='Отчество', max_length=50, )
    passport_number = models.CharField(verbose_name='Номер паспорта', max_length=20)
    phone = models.IntegerField(verbose_name='Контактный телефон', blank=False, )
    sex = models.ForeignKey(Sex, verbose_name='Пол', on_delete=models.PROTECT)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class CardStatus(models.Model):
    """Статусы карты"""
    title = models.CharField(verbose_name='Статус карты', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статусы карт'
        verbose_name_plural = 'Статусы карт'


class CardCategory(models.Model):
    """Категории карт"""
    name = models.CharField(verbose_name='Категория карты', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории карт'
        verbose_name_plural = 'Категории карт'


class ActiveDate(models.Model):
    """Варианты пополнения карты"""
    title = models.CharField(verbose_name='Услуга продления карты', max_length=50)
    value = models.IntegerField(verbose_name='Срок продления в месяцах')
    price = models.IntegerField(verbose_name='Стоимость')

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Пополнение карт'
        verbose_name_plural = 'Пополнение карт'


class ClubCard(models.Model):
    """Модель карты клуба"""
    card_number = models.IntegerField(verbose_name='Номер клубной карты', unique=True, default=0)
    user = models.ForeignKey(User, verbose_name='Клиент', on_delete=models.PROTECT)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    end_date = models.DateTimeField(verbose_name='Дата окончания абонемента', blank=False, editable=True, null=True)
    balance = models.IntegerField(verbose_name='Суммарный баланс карты', default=0)
    status = models.ForeignKey(CardStatus, verbose_name='Статус карты', on_delete=models.PROTECT)
    category = models.ForeignKey(CardCategory, verbose_name='Категория карты', on_delete=models.PROTECT)
    active_date = models.ForeignKey(ActiveDate, verbose_name='Продление краты', on_delete=models.PROTECT, default=5)
    freeze_time = models.CharField(verbose_name='Замороженое время', max_length=255, default=0)

    def save(self, *args, **kwargs):
        if len(str(self.card_number)) < 16:
            self.card_number = generate_club_card_number()
        self.end_date = add_time(self.active_date, self.end_date)
        self.balance = add_balance(self.balance, self.active_date)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('clubcard', kwargs={"clubcard_id": self.pk})

    class Meta:
        verbose_name = 'Карты'
        verbose_name_plural = 'Карты'
