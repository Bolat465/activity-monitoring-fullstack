# Generated by Django 5.0.3 on 2024-05-03 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_activity_show_editing'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tr_document',
            field=models.FileField(blank=True, null=True, upload_to='project_translate_documents/'),
        ),
    ]
