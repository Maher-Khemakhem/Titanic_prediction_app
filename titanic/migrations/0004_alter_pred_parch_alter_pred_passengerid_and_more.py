# Generated by Django 4.2.3 on 2023-09-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("titanic", "0003_alter_pred_age_alter_pred_c_alter_pred_fare_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pred",
            name="Parch",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="PassengerId",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="Pclass",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="SibSp",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="classification",
            field=models.FloatField(default=0),
        ),
    ]
