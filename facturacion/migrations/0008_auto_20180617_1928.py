# Generated by Django 2.0.6 on 2018-06-18 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0007_detallefacturaelectronica_idcomprobante'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoComprobante',
            fields=[
                ('idTipoComprobante', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='facturaelectronica',
            name='codComprobante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='facturacion.TipoComprobante'),
        ),
    ]