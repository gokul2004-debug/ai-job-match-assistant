from django.db import models

class JobApplication(models.Model):
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    my_skills = models.TextField(help_text="Comma-separated skills")
    match_score = models.IntegerField(default=0)
    missing_skills = models.TextField(blank=True)
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"