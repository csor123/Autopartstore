from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class PartCondition(models.Model):
    name = models.CharField(max_length=100)

class PartCategory(models.Model):
    name = models.CharField(max_length=100)

class PartSubCategory(models.Model):
    name = models.CharField(max_length=100)
    part_category = models.ForeignKey(
        PartCategory,
        on_delete=models.CASCADE,
        related_name='sub_categories'
    )

class PartPhoto(models.Model):
    part = models.ForeignKey(
        'Part',
        on_delete=models.CASCADE,
        related_name='photos'
    )
    image = models.ImageField(upload_to='part_photos/')
    is_main = models.BooleanField(default=False)


class Part(models.Model):
    name = models.CharField(
        max_length=255
    )

    article = models.CharField(
        max_length=100,
        unique=True
    )

    part_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        related_name='parts'
    )

    subcategory = models.ForeignKey(
        PartSubCategory,
        on_delete=models.PROTECT,
        related_name='parts'
    )

    condition = models.ForeignKey(
        PartCondition,
        on_delete=models.PROTECT,
        related_name='parts'
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.article} {self.name}'

class PartCross(models.Model):
    part = models.ForeignKey(
        Part,
        on_delete=models.CASCADE,
        related_name='crosses'
    )

    analog_part = models.ForeignKey(
        Part,
        on_delete=models.CASCADE,
        related_name='crossed_by'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['part', 'analog_part'],
                name='unique_cross'
            )
        ]

