# Generated by Django 3.0.8 on 2020-07-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elabodeal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256)),
                ('code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
