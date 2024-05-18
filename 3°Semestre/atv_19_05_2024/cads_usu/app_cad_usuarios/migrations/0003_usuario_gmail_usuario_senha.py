# Generated by Django 5.0.3 on 2024-04-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='gmail',
            field=models.EmailField(default='example@gmail.com', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.CharField(default='123456789', max_length=100),
            preserve_default=False,
        ),
    ]
