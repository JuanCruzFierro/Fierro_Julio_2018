# Generated by Django 2.0.6 on 2018-07-04 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20180704_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='texto',
            new_name='puntaje',
        ),
    ]