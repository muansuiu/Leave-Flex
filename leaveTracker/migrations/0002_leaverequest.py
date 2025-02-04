# Generated by Django 5.1.5 on 2025-01-30 15:17

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('sick_leave', 'Sick Leave'), ('casual_leave', 'Casual Leave')], default='chose one', max_length=20)),
                ('leave_start_date', models.DateField()),
                ('leave_end_date', models.DateField()),
                ('leave_reason', models.TextField(max_length=250)),
                ('leave_applied_date', models.DateField(default=django.utils.timezone.now)),
                ('leave_status', models.CharField(max_length=50)),
                ('leave_approval_date', models.DateField(blank=True, null=True)),
                ('rejection_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
                ('hr_approval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hr_approval', to=settings.AUTH_USER_MODEL)),
                ('lead_approval', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lead_approval', to=settings.AUTH_USER_MODEL)),
                ('rejected_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Leave Requests',
                'ordering': ['leave_applied_date'],
            },
        ),
    ]
