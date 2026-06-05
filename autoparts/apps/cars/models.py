# from django.db import models
#
#
# class Brand(models.Model):
#     name = models.CharField(
#         max_length=100,
#         unique=True
#     )
#
#     def __str__(self):
#         return self.name
#
#
# class CarModel(models.Model):
#     brand = models.ForeignKey(
#         Brand,
#         on_delete=models.CASCADE,
#         related_name='models'
#     )
#
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         unique_together = ('brand', 'name')
#
#     def __str__(self):
#         return f'{self.brand} {self.name}'
#
#
# class Generation(models.Model):
#     model = models.ForeignKey(
#         CarModel,
#         on_delete=models.CASCADE,
#         related_name='generations'
#     )
#
#     name = models.CharField(max_length=100)
#
#
# class Engine(models.Model):
#     generation = models.ForeignKey(
#         Generation,
#         on_delete=models.CASCADE,
#         related_name='engines'
#     )
#
#     code = models.CharField(max_length=50)
#
#     volume = models.DecimalField(
#         max_digits=3,
#         decimal_places=1,
#         blank=True,
#         null=True
#     )
#
#     fuel_type = models.CharField(
#         max_length=30,
#         blank=True
#     )