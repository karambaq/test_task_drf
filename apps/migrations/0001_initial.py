# Generated by Django 2.2.12 on 2020-04-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('api_key', models.CharField(editable=False, max_length=100)),
            ],
        ),
    ]
