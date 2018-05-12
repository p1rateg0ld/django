# Generated by Django 2.0.4 on 2018-05-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
                ('work_phone', models.CharField(max_length=50)),
                ('direct', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('link_address', models.CharField(max_length=50)),
                ('website_link', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]