# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Manufacturer(models.Model):
#     name = models.CharField(max_length=100)
#
#
# class Part(models.Model):
#     article = models.CharField(max_length=100, unique=True)
#
#     name = models.CharField(max_length=255)
#
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.PROTECT
#     )
#
#     manufacturer = models.ForeignKey(
#         Manufacturer,
#         on_delete=models.PROTECT
#     )
#
#     condition = models.CharField(
#         max_length=20,
#         choices=Condition.choices,
#         default=Condition.NEW
#     )
#
#     price = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )
#
#     in_stock = models.PositiveIntegerField(default=0)
#
#     image = models.ImageField(
#         upload_to='parts/',
#         blank=True,
#         null=True
#     )
#
#     engines = models.ManyToManyField(
#         Engine,
#         related_name='parts'
#     )
#
#
