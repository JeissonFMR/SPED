# Generated by Django 4.1.1 on 2022-09-14 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software_caracterizacion', '0015_alter_procesos_hor_pro_alter_procesos_tipoprocesoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procesos',
            name='hor_pro',
            field=models.CharField(default='12:22:16', editable=False, max_length=50, verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='tipoprocesoid',
            field=models.ForeignKey(error_messages={'invalid': 'Enter a valid value', 'required': 'This field is required'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='software_caracterizacion.tipoproceso', verbose_name='Tipo de unidad'),
        ),
    ]
