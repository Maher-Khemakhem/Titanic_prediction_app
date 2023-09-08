# Generated by Django 4.2.3 on 2023-09-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("titanic", "0002_pred_parch_pred_passengerid_pred_female_pred_male_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pred",
            name="Age",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="C",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="Fare",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="Pclass",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="Q",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="S",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="SibSp",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="pred",
            name="classification",
            field=models.IntegerField(default=0),
        ),
    ]