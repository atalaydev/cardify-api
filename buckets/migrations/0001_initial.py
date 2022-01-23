# Generated by Django 4.0 on 2022-01-23 11:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Archived'), (1, 'Active'), (2, 'Draft')], default=2)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_created_by', to='auth.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]