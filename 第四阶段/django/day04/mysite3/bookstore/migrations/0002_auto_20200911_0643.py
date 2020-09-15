# Generated by Django 2.2.12 on 2020-09-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='maker_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='市场价'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(default='', max_length=50, verbose_name='出版社'),
        ),
    ]
