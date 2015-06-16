from django.db import models
from django.utils import timezone
from django.conf import settings


class Tag(models.Model):
    word = models.CharField(max_length=50)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.slug


class Movement(models.Model):
    CURRENCY_CHOICES = (
        ('EUR', 'EUR'),
        ('USD', 'USD')
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    tag = models.ManyToManyField(Tag)  # , related_name='movements')
    date_pub = models.DateField(default=timezone.now, verbose_name='Data inserimento')
    text = models.CharField(max_length=200, verbose_name='Descrizione')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, null=False, blank=False, choices=CURRENCY_CHOICES)
    # amount = MoneyField(decimal_places=2, max_digits=12, currency='EUR')

    def __str__(self):
        return self.text
