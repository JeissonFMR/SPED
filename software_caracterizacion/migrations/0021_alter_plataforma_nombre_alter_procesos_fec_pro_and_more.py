# Generated by Django 4.1.1 on 2022-09-23 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('software_caracterizacion', '0020_rename_responsable_responsableunidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plataforma',
            name='nombre',
            field=models.CharField(max_length=150, null=True, unique=True, verbose_name='Plataforma a la cual va dirigida la solicitud:'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='fec_pro',
            field=models.CharField(default='2022/09/23', editable=False, max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='hor_pro',
            field=models.CharField(default='14:00:52', editable=False, max_length=50, verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='plataformaid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='software_caracterizacion.plataforma', verbose_name='Plataforma a la cual va dirigida la solicitud:'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='responsableid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='software_caracterizacion.responsableunidad', verbose_name='Responsable de la unidad que recibe la solicitud'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='tie_pro',
            field=models.CharField(max_length=100, verbose_name='Tiempo en resolver la solicitud del usuario'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='tie_sel',
            field=models.CharField(choices=[('Minutos', 'Minutos'), ('Horas', 'Horas'), ('Días', 'Días')], default='Horas', max_length=8, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='tipoprocesoid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='software_caracterizacion.tipoproceso', verbose_name='Tipo de unidad que recibe la solicitud'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='unidadesid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='software_caracterizacion.unidades', verbose_name='Unidad que recibe la solicitud'),
        ),
        migrations.AlterField(
            model_name='procesos',
            name='usuarioid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='software_caracterizacion.usuario', verbose_name='Usuario que realiza la solicitud'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=150, null=True, unique=True, verbose_name='Usuario que realiza la solicitud'),
        ),
    ]
