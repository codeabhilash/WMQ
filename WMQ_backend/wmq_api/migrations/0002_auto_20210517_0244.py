# Generated by Django 3.1.2 on 2021-05-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wmq_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='id',
        ),
        migrations.AddField(
            model_name='project',
            name='task_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]