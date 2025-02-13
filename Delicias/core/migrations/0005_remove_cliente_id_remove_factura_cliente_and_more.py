# Generated by Django 4.0.4 on 2024-07-04 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_factura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='direccion_entrega',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='foto_entrega',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='motivo_rechazo',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='rut_receptor',
        ),
        migrations.AddField(
            model_name='cliente',
            name='estadoFactura',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.factura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='idFactura',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.CharField(max_length=50),
        ),
    ]
