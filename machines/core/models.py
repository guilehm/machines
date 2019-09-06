from django.db import models


class Base(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Machine(Base):
    modules = models.ManyToManyField('core.Module')


class Module(Base):
    pass


class Picture(models.Model):
    original_file_name = models.CharField(max_length=1024, null=True, blank=True)
    title = models.CharField(max_length=512, null=True, blank=True)
    image = models.ImageField(upload_to='core/picture/image')

    date_added = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return '#{id}{title}'.format(
            id=self.id,
            title=f' ({self.title})' if self.title else '',
        )
