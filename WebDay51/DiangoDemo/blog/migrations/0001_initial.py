# Generated by Django 2.0.1 on 2018-01-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('mobile', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
            ],
        ),
    ]