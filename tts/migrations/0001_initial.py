# Generated by Django 4.1.3 on 2022-11-14 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="페이지"
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="제목")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성시간"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="갱신시간"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Audio",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="오디오순서"
                    ),
                ),
                ("text", models.TextField(verbose_name="문장")),
                ("speed", models.FloatField(verbose_name="재생속도")),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="갱신시간"),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project_id",
                        to="tts.project",
                        verbose_name="페이지",
                    ),
                ),
            ],
        ),
    ]
