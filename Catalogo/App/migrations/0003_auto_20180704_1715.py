# Generated by Django 2.0.6 on 2018-07-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20180704_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='texto',
            field=models.CharField(max_length=30),
        ),
    ]