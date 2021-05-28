# Generated by Django 3.2.1 on 2021-05-12 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='timeStamp',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]