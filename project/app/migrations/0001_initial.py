# Generated by Django 5.0.4 on 2024-04-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Contact', models.IntegerField()),
                ('Add', models.CharField(max_length=100)),
                ('Age', models.IntegerField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'stu',
                'ordering': ['Name'],
            },
        ),
    ]
