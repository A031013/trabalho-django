# Generated by Django 2.0.10 on 2019-01-13 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reparacoes', '0005_auto_20190113_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='nome_peca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacoes.Peca'),
        ),
    ]
