# Generated by Django 4.2.3 on 2023-09-02 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("titanic", "0006_alter_pred_c_alter_pred_q_alter_pred_s"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pred",
            name="classification",
            field=models.CharField(max_length=30),
        ),
    ]
