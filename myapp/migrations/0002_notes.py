# Generated by Django 4.0.5 on 2022-08-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('cate', models.CharField(max_length=100)),
                ('myfile', models.FileField(upload_to='MyFiles')),
                ('comments', models.TextField()),
            ],
        ),
    ]