# Generated by Django 4.2.3 on 2023-09-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("titanic", "0005_alter_pred_male"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pred",
            name="C",
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="pred",
            name="Q",
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name="pred",
            name="S",
            field=models.FloatField(default=1),
        ),
    ]
