# Generated by Django 4.2 on 2023-04-04 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modeloQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_status', models.IntegerField(max_length=300, null=True)),
                ('data_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]