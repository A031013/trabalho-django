# Generated by Django 2.0.10 on 2019-01-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reparacoes', '0008_auto_20190113_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reparacao',
            name='estado',
            field=models.CharField(choices=[('Por Analisar', 'Por Analisar'), ('Aguardar Encomenda', 'Aguardar Encomenda'), ('Arranjado', 'Arranjado')], max_length=20),
        ),
    ]
