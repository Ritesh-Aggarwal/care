# Generated by Django 2.2.11 on 2022-06-22 13:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0297_auto_20220619_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, 'CT Scan Facility'), (2, 'Maternity Care'), (3, 'X-Ray facility'), (4, 'Neonatal care'), (5, 'Operation theater')], max_length=9, null=True),
        ),
    ]
