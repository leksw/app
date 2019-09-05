from django.db import models
from django.contrib.postgres.fields import JSONField


class Fop(models.Model):
    updated = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField()

    class Meta:
        verbose_name = 'fop'
        verbose_name_plural = 'fops'

    def __str__(self):
        return f'Fop data - {self.update_date}'


class FopRecord(models.Model):
    fio = models.CharField(max_length=455)
    address = models.CharField(max_length=455)
    kved = models.CharField(max_length=455)
    stan = models.CharField(max_length=455)
    records = models.ForeignKey(
        Fop,
        on_delete=models.CASCADE,
        related_name="records",
    )

    class Meta:
        verbose_name = 'fop record'
        verbose_name_plural = 'Fop records'

    def __str__(self):
        return self.fio


class Uo(models.Model):
    updated = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField()

    class Meta:
        verbose_name = 'uo'
        verbose_name_plural = 'uos'

    def __str__(self):
        return f'Uo data - {self.update_date}'


class UoRecord(models.Model):
    name = models.CharField(max_length=755)
    short_name = models.CharField(max_length=755)
    edrpou = models.CharField(max_length=55)
    address = models.CharField(max_length=755)
    boss = models.CharField(max_length=255)
    kved = models.CharField(max_length=455)
    stan = models.CharField(max_length=455)
    founding_document_num = models.CharField(max_length=255)
    records = models.ForeignKey(
        Uo,
        on_delete=models.CASCADE,
        related_name="records",
    )

    class Meta:
        verbose_name = 'uo record'
        verbose_name_plural = 'uo records'

    def __str__(self):
        return self.name


class Founder(models.Model):
    fio = models.CharField(max_length=255)
    share = models.TextField()
    founders = models.ForeignKey(
        UoRecord,
        on_delete=models.CASCADE,
        related_name="founders",
    )

    class Meta:
        verbose_name = 'founder'
        verbose_name_plural = 'founders'

    def __str__(self):
        return self.fio
