from django.db import models
from django.db.models import Q
from model_utils.models import TimeStampedModel


# Create your models here.
class Person (TimeStampedModel):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateField()
    birth_city = models.CharField(max_length=200, blank=True, null=True)
    birth_country = models.CharField(max_length=200, blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='pictures', blank=True, null=True)
    parents = models.ForeignKey('Couple', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    @property
    def full_name(self):
        return '{0} {1} {2}'.format(self.first_name, self.middle_name or '', self.last_name)

    @property
    def siblings(self):
        if self.parents:
            return self.parents.children.exclude(pk=self.pk)

    @property
    def children(self):
        return Person.objects.filter(Q(parents__father=self) | Q(parents__mother=self))

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return self.full_name


class Couple(TimeStampedModel):
    father = models.ForeignKey(Person, related_name='father')
    mother = models.ForeignKey(Person, related_name='mother')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.father.full_name, self.mother.full_name)
