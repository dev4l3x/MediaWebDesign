# Generated by Django 3.1 on 2020-08-18 14:32

from django.db import migrations
import fontawesome_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_service_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialnetwork',
            name='icon',
            field=fontawesome_5.fields.IconField(blank=True, max_length=60),
        ),
    ]