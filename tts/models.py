from django.db import models


class Title(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")

    def __str__(self):
        return f"{self.title}"


class Project(models.Model):
    page = models.IntegerField(verbose_name="페이지")
    title = models.ForeignKey(Title, on_delete=models.CASCADE, verbose_name="제목")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="갱신시간")

    def __str__(self):
        return f"project title: {self.title} - page: {self.page}"


class Audio(models.Model):
    sequence = models.IntegerField(verbose_name="오디오순서")
    text = models.TextField(verbose_name="문장")
    speed = models.FloatField(verbose_name="재생속도")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="갱신시간")
    # 프로젝트 제목 pk
    project = models.ForeignKey(Title, on_delete=models.CASCADE, verbose_name="프로젝트")
    project_page = models.IntegerField(verbose_name="페이지")

    def __str__(self):
        return f"project title: {self.project.title} - page: {self.project_page} - {self.sequence}번째 audio"
