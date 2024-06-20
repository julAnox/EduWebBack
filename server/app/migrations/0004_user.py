# Generated by Django 4.2.13 on 2024-06-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img_path', models.ImageField(upload_to='users/')),
                ('password', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
    ]