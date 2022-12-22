from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=128)


class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.job.title} {self.skill}"


class Candidate(models.Model):
    first_name = models.CharField(max_length=52)
    last_name = models.CharField(max_length=52)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class CandidateSkill(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    skill = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.candidate.get_full_name
