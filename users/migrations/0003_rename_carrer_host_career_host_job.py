# Generated by Django 4.0 on 2021-12-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='host',
            old_name='carrer',
            new_name='career',
        ),
        migrations.AddField(
            model_name='host',
            name='job',
            field=models.CharField(max_length=45, null=True),
        ),
    ]