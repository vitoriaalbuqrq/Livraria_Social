# Generated by Django 4.2.5 on 2023-11-25 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios_Resenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('data', models.DateField(null=True)),
            ],
            options={
                'db_table': 'Comentarios_Resenha',
            },
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('isbn', models.TextField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField()),
                ('autor', models.CharField()),
                ('capa_url', models.URLField()),
                ('descricao', models.TextField(max_length=100)),
                ('genero', models.CharField(default='Outros', max_length=100)),
                ('avaliacao', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
            ],
            options={
                'db_table': 'livro',
            },
        ),
        migrations.CreateModel(
            name='Resenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('texto', models.TextField()),
                ('avaliacao', models.IntegerField()),
                ('curtidas', models.PositiveIntegerField(default=0)),
                ('data', models.DateField(null=True)),
                ('melhor_resenha', models.IntegerField(default=0)),
                ('data_atual', models.DateField(null=True)),
                ('data_final', models.DateField(null=True)),
                ('comentarios', models.ManyToManyField(related_name='comentario_resenha', to='livro.comentarios_resenha')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.livros')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'db_table': 'Resenha',
            },
        ),
        migrations.CreateModel(
            name='Lista_livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_lista', models.CharField(max_length=100)),
                ('livros', models.ManyToManyField(related_name='livros_salvos', to='livro.livros')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'db_table': 'Lista_livros',
            },
        ),
        migrations.CreateModel(
            name='CurtidaResenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curtida', models.BooleanField(default=True)),
                ('resenha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.resenha')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'db_table': 'CurtidaResenha',
            },
        ),
        migrations.AddField(
            model_name='comentarios_resenha',
            name='resenha_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.resenha'),
        ),
        migrations.AddField(
            model_name='comentarios_resenha',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario'),
        ),
    ]