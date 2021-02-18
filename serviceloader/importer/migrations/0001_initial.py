# Generated by Django 3.1.5 on 2021-02-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dimresgenforecastmodel',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('desc', models.TextField(blank=True, db_column='Desc', null=True)),
                ('productiontypeemieid', models.IntegerField(blank=True, db_column='ProductionTypeEmieID', null=True)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
            ],
            options={
                'db_table': 'DimRESGenForecastModel',
                'managed': True,
            },
        ),
    ]
