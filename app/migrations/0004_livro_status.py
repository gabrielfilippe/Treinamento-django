# Generated by Django 5.0.4 on 2024-04-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_livro_livro_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]