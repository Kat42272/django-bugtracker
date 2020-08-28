# Generated by Django 3.1 on 2020-08-28 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bugs_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='bio',
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('current_ticket_process', models.CharField(choices=[('NEW', 'New'), ('IN PROGRESS', 'In Progress'), ('DONE', 'Done'), ('INVALID', 'Invalid')], default='NEW', max_length=50)),
                ('assigned_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user', to=settings.AUTH_USER_MODEL)),
                ('completed_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_user', to=settings.AUTH_USER_MODEL)),
                ('filed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]