# Generated by Django 5.0.7 on 2024-09-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_authgroup_delete_authgrouppermissions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('postname', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
    ]