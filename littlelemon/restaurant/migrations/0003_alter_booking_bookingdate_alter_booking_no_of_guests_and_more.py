# Generated by Django 4.2.20 on 2025-03-13 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "restaurant",
            "0002_rename_price_menu_price_alter_booking_no_of_guests_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking", name="BookingDate", field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="booking",
            name="No_of_guests",
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name="menu", name="Inventory", field=models.IntegerField(default=5),
        ),
    ]
