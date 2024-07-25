# Generated by Django 5.0.7 on 2024-07-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='date_posted',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='story',
            name='img_title',
        ),
        migrations.RemoveField(
            model_name='story',
            name='snip',
        ),
        migrations.AddField(
            model_name='story',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='excerpt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='story',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
