# Generated by Django 2.2.16 on 2022-09-12 18:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220911_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название жанра'),
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Genre', verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reviews.Title', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название произведения'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.SmallIntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(2022, 'Год выпуска произведения не может быть больше нынешнего.')], verbose_name='Год выпуска'),
        ),
    ]