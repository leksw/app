# Generated by Django 2.2.5 on 2019-09-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founder',
            name='fio',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='uorecord',
            name='boss',
            field=models.CharField(max_length=455),
        ),
        migrations.AlterField(
            model_name='uorecord',
            name='founding_document_num',
            field=models.CharField(max_length=455),
        ),
    ]
