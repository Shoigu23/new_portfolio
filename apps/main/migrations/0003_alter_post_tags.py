# Generated by Django 4.2 on 2023-04-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_post_active_alter_post_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="main.tag", verbose_name="Направление"),
        ),
    ]
