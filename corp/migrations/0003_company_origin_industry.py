# Generated by Django 4.2.4 on 2024-06-27 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corp", "0002_originindustrycategory_originindustry"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="origin_industry",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="companies",
                to="corp.originindustry",
                verbose_name="オリジナル中分類",
            ),
            preserve_default=False,
        ),
    ]
