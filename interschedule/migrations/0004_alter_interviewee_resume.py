# Generated by Django 4.0.3 on 2022-03-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interschedule', '0003_alter_interviewee_f_name_alter_interviewee_l_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewee',
            name='resume',
            field=models.URLField(null=True),
        ),
    ]
