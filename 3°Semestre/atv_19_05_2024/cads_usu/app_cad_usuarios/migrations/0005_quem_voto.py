# Generated by Django 5.0.3 on 2024-05-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0004_base_questoes_sub_questoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quem_voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=200)),
                ('voto', models.CharField(max_length=200)),
            ],
        ),
    ]
