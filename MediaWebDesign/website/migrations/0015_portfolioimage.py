# Generated by Django 3.1 on 2020-09-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_remove_image_include_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ImageField(upload_to='portfolioimages/')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
