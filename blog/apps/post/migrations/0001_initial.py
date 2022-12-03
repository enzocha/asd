# Generated by Django 4.0 on 2022-12-01 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('activado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=40, null=True)),
                ('resumen', models.CharField(max_length=70, null=True)),
                ('texto', models.TextField(max_length=500, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='post')),
                ('publicado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'posteos',
            },
        ),
    ]
