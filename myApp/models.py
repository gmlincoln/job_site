from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Custom_User(AbstractUser):

    USER_TYPE = [
        ('recruiter','Recruiter'),
        ('job_seeker','Job Seeker')
    ]

    user_type = models.CharField(choices=USER_TYPE, null=True, max_length=30)

    def __str__(self) -> str:
        return f"{self.username}--{self.user_type}"
    
class JobSeekerModel(models.Model):

    SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),

    ]

    skills = models.CharField(choices=SKILLS, max_length=100, null=True)
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='JobSeeker')

    def __str__(self) -> str:
        return f"{self.user.username}--{self.user.first_name}"
    
class RecruiterModel(models.Model):
    user = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='Recruiter')

    def __str__(self) -> str:
        return f"{self.user.username}--{self.user.first_name}"
    


class JobModel(models.Model):

    SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),

    ]

    CATEGORY = [
        ('full_time','Full Time'), 
        ('part_time','Part Time') 
    ]

    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    num_of_openings = models.PositiveIntegerField(null=True)
    category = models.CharField(choices=CATEGORY, max_length=50)
    description = models.TextField(max_length=500, null=True)
    skills = models.CharField(choices=SKILLS, max_length=50, null=True)
    company_logo = models.ImageField(upload_to='Media/Company_Logo', null=True)


    def __str__(self) -> str:
        return f"{self.user.username}--{self.title}"
    

class jobApplyModel(models.Model):

    user = models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    job = models.ForeignKey(JobModel,on_delete=models.CASCADE)
    cover = models.CharField(max_length=500, null=True)
    skills = models.CharField(max_length=100, null=True)
    resume = models.ImageField(upload_to='Media/Resume', null=True)

    def __str__(self):
        return f"{self.user.username}--{self.job.title}"
