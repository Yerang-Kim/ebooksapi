# Generated by Django 3.2.8 on 2021-10-16 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ebooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
