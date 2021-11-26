# Generated by Django 3.2.9 on 2021-11-26 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=9)),
                ('endereço', models.CharField(max_length=100)),
                ('telefone_de_contato', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
            ],
        ),
    ]