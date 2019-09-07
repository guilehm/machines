from django.db import models
from django.db.models import Sum


class Machine(models.Model):
    code = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    on_sale = models.BooleanField(default=True, db_index=True)
    variations = models.ManyToManyField(
        'product.Variation',
        related_name='machines',
        blank=True,
    )
    pictures = models.ManyToManyField('product.Picture', blank=True)
    picture_primary = models.ForeignKey(
        'product.Picture',
        null=True,
        blank=True,
        related_name='machines',
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.code}) {self.name}'

    @property
    def total(self):
        if not self.variations.exists():
            return self.price or 0
        return self.price or 0 + (self.variations.values(
            'price'
        ).aggregate(
            total_price=Sum('price')
        )['total_price'] or 0)


class Module(models.Model):
    code = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    pictures = models.ManyToManyField(
        'product.Picture',
        related_name='modules',
        blank=True,
    )
    picture_primary = models.ForeignKey(
        'product.Picture', null=True, blank=True, on_delete=models.CASCADE
    )

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def short_description(self):
        return '{}{}'.format(
            self.description[:50],
            '' if len(self.description) <= 50 else '...',
        )


class Variation(models.Model):
    module = models.ForeignKey(
        'product.Module',
        related_name='variations',
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=1024, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True,
        blank=True,
    )
    picture_primary = models.ForeignKey(
        'product.Picture',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    pictures = models.ManyToManyField(
        'product.Picture',
        related_name='variations',
        blank=True,
    )
    on_sale = models.BooleanField(default=True, db_index=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.code}) {self.name}'

    def picture(self):
        if not self.picture_primary:
            return self.module.picture_primary
        return self.picture_primary


class Picture(models.Model):
    title = models.CharField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to='core/picture/image')

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '#{id}{title}'.format(
            id=self.pk,
            title=f' ({self.title})' if self.title else '',
        )
