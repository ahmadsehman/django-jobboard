# Generated by Django 3.1.4 on 2020-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20201213_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
