from django.db import models
from django.utils import timezone
# Create your models here.
class Department(models.Model):
    name = models.CharField('部署名',max_length=20)
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField('部活名', max_length=20)
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return self.name


class Employ(models.Model):
    first_name = models.CharField('名',max_length=20)
    last_name = models.CharField('姓',max_length=20)
    email = models.EmailField('mailadress',blank=True)
    department = models.ForeignKey(
        Department, verbose_name = '部署', on_delete = models.PROTECT,
    )
    club = models.ManyToManyField(
        'Club', verbose_name = ('部活')
    )
    # address = models.CharField('住所', max_length=20,blank=True)

    created_at = models.DateTimeField('日付',default=timezone.now)

    # models.OneToOneField('', verbose_name=_(""), on_delete=models.CASCADE)

    def __str__(self):
        return '{0}{1}{2}'.format(self.last_name,self.first_name,self.department)