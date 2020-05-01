# Generated by Django 3.0.5 on 2020-05-01 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_auto_20200428_1253'),
        ('studies', '0064_auto_20200429_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='studies', related_query_name='study', to='accounts.Organization'),
        ),
    ]