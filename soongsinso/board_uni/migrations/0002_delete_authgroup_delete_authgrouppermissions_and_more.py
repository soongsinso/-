# Generated by Django 5.0.7 on 2024-09-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("board_uni", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AuthGroup",
        ),
        migrations.DeleteModel(
            name="AuthGroupPermissions",
        ),
        migrations.DeleteModel(
            name="AuthPermission",
        ),
        migrations.DeleteModel(
            name="AuthUser",
        ),
        migrations.DeleteModel(
            name="AuthUserGroups",
        ),
        migrations.DeleteModel(
            name="AuthUserUserPermissions",
        ),
        migrations.DeleteModel(
            name="DjangoAdminLog",
        ),
        migrations.DeleteModel(
            name="DjangoContentType",
        ),
        migrations.DeleteModel(
            name="DjangoMigrations",
        ),
        migrations.DeleteModel(
            name="DjangoSession",
        ),
    ]
