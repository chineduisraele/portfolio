# Generated by Django 4.0.2 on 2022-04-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_alter_message_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
