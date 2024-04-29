# Generated by Django 4.2.6 on 2024-04-28 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("spam_mailing", "0005_mailinglog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="send_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Время отправки"
            ),
        ),
    ]