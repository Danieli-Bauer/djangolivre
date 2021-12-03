# Generated by Django 3.2.9 on 2021-12-02 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
        ('transferencia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacao',
            name='cadastro',
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='entrada_nome',
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='numero_conta_destino',
        ),
        migrations.RemoveField(
            model_name='transacao',
            name='valor_para_transferencia',
        ),
        migrations.AddField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transacao',
            name='destinatario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='destinatario', to='conta.conta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacao',
            name='remetente',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, related_name='remetente', to='conta.conta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacao',
            name='valor_transferido',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]