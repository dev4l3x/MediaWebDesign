# Generated by Django 3.1 on 2020-08-21 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_socialnetwork_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='language',
        ),
        migrations.CreateModel(
            name='ServiceTranslate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.language')),
                ('service', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.service')),
            ],
        ),
    ]