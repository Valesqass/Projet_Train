# Generated by Django 5.0.3 on 2024-04-06 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0004_rename_plan_train_adresse_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='adresse_plan',
            new_name='plan',
        ),
    ]
