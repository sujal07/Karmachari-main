# Generated by Django 3.2.17 on 2023-02-24 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_schedule_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.FloatField(null=True)),
                ('status', models.CharField(choices=[('L', 'Late'), ('P', 'Present'), ('A', 'Absent'), ('LV', 'Leave')], max_length=2)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.calendar')),
            ],
        ),
    ]