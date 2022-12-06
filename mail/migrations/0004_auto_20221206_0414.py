# Generated by Django 3.2.16 on 2022-12-06 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_remove_resident_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mail.resident'),
        ),
        migrations.AddField(
            model_name='package',
            name='status',
            field=models.CharField(choices=[('DELIVERED', 'delivered'), ('PENDING', 'pending'), ('UNKNOWN', 'unknown')], max_length=50, null=True),
        ),
    ]
