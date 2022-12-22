from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.title=self.title.lower()
        super().save(*args,**kwargs)


class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.CharField(max_length=128)

    class Meta:
        unique_together=("job_id", "skill")

    def __str__(self) -> str:
        return f"{self.job.title} {self.skill}"

    def save(self, *args, **kwargs):
        self.skill= self.skill.lower()
        super().save(*args,**kwargs)



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

    class Meta:
        unique_together=("candidate_id", "skill")

    def __str__(self) -> str:
        return self.candidate.get_full_name

    def save(self, *args, **kwargs):
        self.skill=self.skill.lower()
        super().save(*args,**kwargs)
