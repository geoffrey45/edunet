# Generated by Django 2.2 on 2021-03-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20210307_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.CharField(default='http://africa-me.com/wp-content/uploads/2020/07/africa-women-tech-africa-me.jpg', max_length=6000),
        ),
    ]
