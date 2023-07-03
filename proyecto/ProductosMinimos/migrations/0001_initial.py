# Generated by Django 4.2.2 on 2023-07-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductosMinimos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        default="Sin nombrar", max_length=300, verbose_name="Nombre"
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        default="Sin especificar",
                        max_length=300,
                        verbose_name="Descripción",
                    ),
                ),
                ("precio", models.FloatField(default=0, verbose_name="Precio")),
                ("registro", models.DateField(verbose_name="Fecha de registro")),
                (
                    "estatus",
                    models.CharField(
                        default="Sin estatus", max_length=300, verbose_name="Estatus"
                    ),
                ),
            ],
            options={
                "verbose_name": "Productos_Minimos",
                "verbose_name_plural": "Productos_Minimos",
            },
        ),
    ]