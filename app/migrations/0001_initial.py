# Generated by Django 2.0.6 on 2020-06-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=4)),
                ('age', models.IntegerField()),
                ('fputs', models.IntegerField()),
            ],
            options={
                'db_table': 'clases',
            },
        ),
    ]