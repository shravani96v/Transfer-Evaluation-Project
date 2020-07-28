# Generated by Django 3.0.3 on 2020-07-09 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_auto_20200709_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major_requirement',
            name='major_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.Major'),
        ),
        migrations.AlterField(
            model_name='transfercourse',
            name='school_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.School'),
        ),
        migrations.AlterField(
            model_name='transfercourse',
            name='subject_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transfercourse',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transferevaluation',
            name='major_req_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.Major_requirement'),
        ),
        migrations.AlterField(
            model_name='transferevaluation',
            name='transfer_course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.TransferCourse'),
        ),
        migrations.AlterUniqueTogether(
            name='major_requirement',
            unique_together={('description', 'major_id')},
        ),
        migrations.AlterUniqueTogether(
            name='transfercourse',
            unique_together={('school_id', 'subject_number', 'title')},
        ),
        migrations.AlterUniqueTogether(
            name='transferevaluation',
            unique_together={('transfer_course_id', 'major_req_id')},
        ),
    ]
