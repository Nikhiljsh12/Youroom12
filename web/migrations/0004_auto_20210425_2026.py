# Generated by Django 3.1 on 2021-04-25 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('web', '0003_auto_20210425_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='doc_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount'),
        ),
    ]