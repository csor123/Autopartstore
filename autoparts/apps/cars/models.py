from django.db import models

class CarBrand(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
        related_name='models'
    )

    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('brand', 'name')

    def __str__(self):
        return f'{self.brand} {self.name}'


class CarGeneration(models.Model):
    model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
        related_name='generations'
    )

    generation_name = models.CharField(max_length=100)
    modification = models.CharField(max_length=100)
    # years_start = models.PositiveIntegerField()
    # years_end = models.PositiveIntegerField()
    # years_period = models.PositiveIntegerField()
    # photo = models.ImageField(upload_to='car_photos/')


class CarEngine(models.Model):
    generation = models.ForeignKey(
        CarGeneration,
        on_delete=models.CASCADE,
        related_name='engines'
    )

    code = models.CharField(max_length=50)

    volume = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True
    )

    fuel_type = models.CharField(
        max_length=30,
        blank=True
    )

    horse_power = models.IntegerField(
        blank=True,
        null=True
    )