# Generated by Django 3.1.5 on 2021-02-03 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajador', '0003_auto_20210202_1906'),
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trabajador.trabajador'),
        ),
    ]
