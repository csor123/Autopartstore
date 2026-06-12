from django.db import models
from apps.parts.models import Part

class Compatibility(models.Model):
    part = models.ForeignKey(
        'Part',
        on_delete=models.CASCADE,
        related_name='compatibilities'
    )

    engine = models.ForeignKey(
        CarEngine,
        on_delete=models.CASCADE,
        related_name='parts'
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('part', 'engine')
# class PartCross(models.Model):
# class Attributes(models.Model):