from django.db import models


class Project(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="페이지")
    title = models.CharField(max_length=200, verbose_name="제목")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="갱신시간")

    def __str__(self):
        return f"{self.title}"


class Audio(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="오디오순서")
    text = models.TextField(verbose_name="문장")
    speed = models.FloatField(verbose_name="재생속도")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="갱신시간")
    project = models.ForeignKey(
        Project,
        related_name="project_id",
        blank=False,
        on_delete=models.CASCADE,
        verbose_name="페이지",
    )
