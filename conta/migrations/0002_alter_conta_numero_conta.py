# Generated by Django 3.2.9 on 2021-11-29 21:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='numero_conta',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]