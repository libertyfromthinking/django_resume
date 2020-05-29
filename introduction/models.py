from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from board.fields import *

# Create your models here.
class Resume(models.Model):
    name = models.CharField('Name', max_length=10)
    age = models.IntegerField('Age')
    email = models.TextField('Email', blank=True)
    git_addr = models.TextField('GitAddr', blank=True)
    phone = models.TextField('Phone', blank=True)
    job_objective = models.CharField('Job Objective', max_length=10)
    military_service = models.TextField('Military Service', blank=True)
    hobby = models.TextField('Hobby', blank=True)
    image = ThumbnailImageField(upload_to='img/', null=True, blank=True)

    def __str__(self):
        return self.name


class Coverletter(models.Model):
    question = models.TextField('Question')
    answer = models.TextField('Answer')

    def __str__(self):
        return self.question


class Project(models.Model):
    name = models.CharField('Name', max_length=20)
    slug = models.SlugField('Slug', unique=True, allow_unicode=True,
                            help_text='자동으로 기입되니 입력하지 않으셔도 됩니다.', blank=True, null=True)
    description = models.TextField('Description')
    link = models.TextField('link', null=True, blank=True)
    techs = models.ManyToManyField('Tech', related_name='projects')
    git_addr = models.TextField('GitAddr', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("intro:project_detail", args=(self.slug,))


class Tech(models.Model):
    name = models.CharField('Name', max_length=30)
    level = models.IntegerField('Level')

    def __str__(self):
        return self.name


class Qualification(models.Model):
    name = models.CharField('Name', max_length=20)
    issuer = models.CharField('Issuer', max_length=20)
    issue_date = models.TextField('Issue Date')
    resume = models.ForeignKey(Resume, related_name='qualifications',
                               on_delete=models.CASCADE)


class Work_experience(models.Model):
    name = models.CharField('Name', max_length=20)
    department = models.CharField('Department', max_length=10)
    position = models.CharField('Position', max_length=10)
    responsibilities = models.TextField('responsibilities', null=True)
    employment_period = models.TextField('Employment Period')
    resume = models.ForeignKey(Resume, related_name='work_experiences',
                               on_delete=models.CASCADE)


class Education(models.Model):
    name = models.CharField('Name', max_length=20)
    study_period = models.TextField('Study Period')
    resume = models.ForeignKey(Resume, related_name='educations',
                               on_delete=models.CASCADE)
