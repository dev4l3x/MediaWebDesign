# Generated by Django 3.0.8 on 2020-07-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200719_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ImageField(upload_to='')),
                ('include_portfolio', models.BooleanField(default=False)),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]