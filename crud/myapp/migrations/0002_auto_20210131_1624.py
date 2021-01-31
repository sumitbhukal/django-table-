# Generated by Django 3.1.5 on 2021-01-31 10:54

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='data',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='email_id',
            field=models.CharField(default='email@g.com', max_length=60, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='data',
            name='emp_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=60, verbose_name='name'),
        ),
    ]