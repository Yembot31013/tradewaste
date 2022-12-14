# Generated by Django 4.0.4 on 2022-09-19 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=70, null=True)),
                ('last_name', models.CharField(blank=True, max_length=70, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=70, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True)),
                ('location_state', models.CharField(blank=True, max_length=20, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('nin', models.IntegerField(blank=True, max_length=11, null=True)),
                ('avatar', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='user_img/')),
                ('slug', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=9, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('done', models.BooleanField(blank=True, default=False, null=True)),
                ('period', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recycle.profile')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recycle.work')),
            ],
        ),
    ]
