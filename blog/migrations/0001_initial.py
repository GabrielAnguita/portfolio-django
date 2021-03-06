# Generated by Django 2.2.17 on 2020-11-05 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
