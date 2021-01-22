# Generated by Django 3.1.1 on 2020-09-27 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('sdt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('bomon', models.CharField(max_length=80)),
                ('khoa_gd', models.CharField(max_length=80)),
                ('ngaysinh', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=255)),
                ('quequan', models.CharField(max_length=30)),
                ('sdt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('lop', models.CharField(max_length=80)),
                ('khoa', models.CharField(max_length=80)),
                ('ngaysinh', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=255)),
                ('quequan', models.CharField(max_length=30)),
                ('sdt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationStaff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBackStaff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.staff')),
            ],
        ),
    ]
