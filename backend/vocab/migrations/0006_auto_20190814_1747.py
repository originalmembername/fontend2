# Generated by Django 2.1.2 on 2019-08-14 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0005_vocabs_pitctureurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vocabs',
            old_name='pitctureUrl',
            new_name='pictureUrl',
        ),
    ]
