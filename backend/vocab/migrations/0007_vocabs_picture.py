# Generated by Django 3.0 on 2020-02-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0006_auto_20190814_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabs',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
