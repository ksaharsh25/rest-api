# Generated by Django 4.1.6 on 2023-02-02 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_Number', models.IntegerField(unique=True)),
                ('Name', models.CharField(max_length=50, unique=True)),
                ('Email_Address', models.EmailField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SpamReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_count', models.IntegerField(default=0)),
                ('mobspam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spam.user', to_field='Phone_Number')),
            ],
        ),
    ]
