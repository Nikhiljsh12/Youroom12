# Generated by Django 3.1 on 2021-04-25 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_mypost_head'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='background',
            field=models.CharField(choices=[('#0a4b94', 'Blu'), ('#DAA520', 'Yel'), ('#95001b', 'Red'), ('#463f85', 'Pur'), ('#009342', 'Gre'), ('#930051', 'Pin'), ('', 'Non')], default='', max_length=20),
        ),
        migrations.CreateModel(
            name='MyPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('page', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.mypost')),
            ],
        ),
    ]
