# Generated by Django 4.2.5 on 2023-10-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_resenha'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='avaliacao',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
    ]
