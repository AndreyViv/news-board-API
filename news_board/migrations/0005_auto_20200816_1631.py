# Generated by Django 3.1 on 2020-08-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_board', '0004_auto_20200816_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount_of_upvotes',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
