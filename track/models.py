from django.db import models


class Track(models.Model):
    processing_area = models.ForeignKey(
        "ProcessingArea",
        related_name="processing",
        on_delete=models.CASCADE,
        null=True
    )
    shortdesc = models.CharField(
        max_length=100
    )
    routes = models.ManyToManyField(
        "Route",
        blank=True,
        related_name="routing"
    )

    def __str__(self):
        return str(self.shortdesc)

    class Meta:
        verbose_name = 'Траектория'
        verbose_name_plural = 'Траектории'


class ProcessingArea(models.Model):
    shortdesc = models.CharField(
        max_length=25
    )
    shp = models.FileField(
        upload_to=f'geo/processing/'
    )
    shx = models.FileField(
        upload_to=f'geo/processing/'
    )
    dbf = models.FileField(
        upload_to=f'geo/processing/'
    )
    json = models.JSONField(
        null=True,
        blank=True
    )
    
    def __str__(self):
        return str(self.shortdesc)

    class Meta:
        verbose_name = 'Данные для заполнения'
        verbose_name_plural = 'Данные для заполнения'


class Route(models.Model):
    tractor = models.ForeignKey(
        "Tractor",
        related_name="executing",
        on_delete=models.CASCADE,
        null=True
    )
    aggregator = models.ForeignKey(
        "Aggregator",
        related_name="using",
        on_delete=models.CASCADE,
        null=True
    )
    shortdesc = models.CharField(
        max_length=25
    )
    shp = models.FileField(
        upload_to=f'geo/routing/'
    )
    shx = models.FileField(
        upload_to=f'geo/routing/'
    )
    dbf = models.FileField(
        upload_to=f'geo/routing/'
    )
    json = models.JSONField(
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.shortdesc)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Tractor(models.Model):
    name = models.CharField(
        max_length=100,
        default="МТЗ-1221"
    )
    length = models.FloatField(
        default=4.950
    )
    width = models.FloatField(
        default=2.250
    )
    wheels_base = models.FloatField(
        default=2.450
    )
    turning_radius = models.FloatField(
        default=5
    )
    available_aggregators = models.ManyToManyField(
        'Aggregator',
        related_name='compability',
        blank=True,
        )
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Трактор'
        verbose_name_plural = 'Тракторы'


class Aggregator(models.Model):
    target_choises = [
        ("plant", "planting"),
        ("water", "watering"),
        ("plant&water", "planting&watering")
    ]
    target = models.CharField(
        choices=target_choises,
        max_length=20
    )
    name = models.CharField(
        max_length=100,
        default="unnamed"
    )
    width = models.FloatField()
    aisle = models.FloatField(
        default=0.70
    )
    row_width = models.FloatField(
        default=0.0
    )
    num_of_sections = models.IntegerField(
        null=True
    )
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Агрегатор'
        verbose_name_plural = 'Агрегаторы'
