# Generated by Django 2.0.10 on 2019-01-13 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reparacoes', '0009_auto_20190113_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('localidade', models.CharField(max_length=200)),
                ('morada', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='encomenda',
            name='numero',
        ),
        migrations.AddField(
            model_name='encomenda',
            name='entregue',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='encomenda',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacoes.Fornecedor'),
        ),
    ]
