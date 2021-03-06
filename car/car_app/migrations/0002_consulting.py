# Generated by Django 4.0 on 2022-01-05 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(db_column='car_name', max_length=20)),
                ('contact', models.CharField(db_column='contact', max_length=20)),
                ('location', models.CharField(db_column='location', max_length=20)),
                ('privacy_agreement', models.BooleanField(db_column='privacy_agreement', default=False)),
                ('status_consulting', models.CharField(db_column='status_consulting', default='상담중', max_length=20)),
                ('status_selling', models.CharField(db_column='status_selling', default='판매예약중', max_length=20)),
                ('created_at', models.DateTimeField(db_column='created_at', default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'consulting',
            },
        ),
    ]
