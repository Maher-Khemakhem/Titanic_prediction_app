# Generated by Django 4.2.3 on 2023-09-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("titanic", "0004_alter_pred_parch_alter_pred_passengerid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pred",
            name="male",
            field=models.FloatField(default=0),
        ),
    ]
