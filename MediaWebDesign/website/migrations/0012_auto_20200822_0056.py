# Generated by Django 3.1 on 2020-08-21 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200822_0029'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='servicetranslate',
            unique_together={('service', 'language')},
        ),
    ]