# Generated by Django 4.2.3 on 2024-10-06 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_url', '0005_login_urlinfo_user_alter_urlinfo_short_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlinfo',
            name='user',
        ),
    ]
