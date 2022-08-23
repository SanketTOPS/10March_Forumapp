# Generated by Django 4.0.5 on 2022-08-13 13:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_signup',
            name='username',
        ),
        migrations.AddField(
            model_name='user_signup',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
