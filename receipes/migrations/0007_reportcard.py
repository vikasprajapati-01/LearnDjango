# Generated by Django 4.2.9 on 2024-02-28 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipes', '0006_subject_subjectmarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtae_of_report', models.DateField(auto_created=True)),
                ('student_rank', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreportcard', to='receipes.student')),
            ],
        ),
    ]
