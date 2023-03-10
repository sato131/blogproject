# Generated by Django 4.1.3 on 2022-12-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_samplemodel_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('postdate', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
