# Generated by Django 3.1 on 2020-08-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_board', '0002_auto_20200816_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount_of_upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
