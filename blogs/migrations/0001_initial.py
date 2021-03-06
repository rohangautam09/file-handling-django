# Generated by Django 3.0.4 on 2020-03-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('blog_body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('pic', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
