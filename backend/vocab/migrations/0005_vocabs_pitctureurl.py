# Generated by Django 2.1.2 on 2019-08-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0004_auto_20190602_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabs',
            name='pitctureUrl',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
