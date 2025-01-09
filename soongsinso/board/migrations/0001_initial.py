# Generated by Django 5.0.7 on 2024-09-04 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('chat_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('chat', models.CharField(blank=True, max_length=100, null=True)),
                ('sendtime', models.DateTimeField()),
                ('checker', models.IntegerField()),
            ],
            options={
                'db_table': 'chat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chatpa',
            fields=[
                ('chatpa_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'chatpa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('chatroom_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('chatname', models.CharField(blank=True, max_length=100, null=True)),
                ('chatstate', models.CharField(max_length=100)),
                ('entertime', models.DateTimeField()),
            ],
            options={
                'db_table': 'chatroom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('style_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'style',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=11)),
                ('major', models.CharField(max_length=100)),
                ('student_number', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
