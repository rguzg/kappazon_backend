
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    total_items = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    products = models.ManyToManyField('')
