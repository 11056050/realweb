# Generated by Django 4.2.4 on 2023-10-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('put_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-put_date',),
            },
        ),
    ]
