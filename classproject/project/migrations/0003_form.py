# Generated by Django 3.0.3 on 2020-02-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=55)),
                ('Phone_no', models.IntegerField()),
                ('Email', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
    ]
