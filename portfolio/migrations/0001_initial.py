# Generated by Django 2.1.7 on 2019-05-02 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='static/img/portfolio')),
                ('lighting', models.CharField(choices=[('u', 'Under'), ('n', 'normal'), ('o', 'over')], max_length=1)),
                ('situation', models.CharField(choices=[('u', 'Under'), ('n', 'normal'), ('o', 'over')], max_length=1)),
                ('mood', models.CharField(choices=[('u', 'Under'), ('n', 'normal'), ('o', 'over')], max_length=1)),
                ('angle', models.CharField(choices=[('s', 'Wide'), ('n', 'normal'), ('t', 'tele')], max_length=1)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Album')),
            ],
        ),
    ]
