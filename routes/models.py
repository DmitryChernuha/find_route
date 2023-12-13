from django.db import models
from django.urls import reverse
from cities.models import City


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  related_name='route_to_city_set', verbose_name='В какой город')
    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE,
                                related_name='route_from_city_set', verbose_name='Из какого города')
    trains = models.ManyToManyField()

    def __str__(self):
        return f'Поезд № {self.name} из города {self.from_city}'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']

    def get_absolute_url(self):
        return reverse('trains:detail', kwargs={'pk': self.pk})
