from django.shortcuts import redirect,render
from django.http import HttpResponse

from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from myApp.models import *
from django.db.models import Q 


def homePage(req):

    jobs = JobModel.objects.all()

    context = {
        'jobs':jobs,
    }

    return render(req, 'homepage.html',context)

def searchJob(req):

    query = req.GET.get('query')

    if query:
        jobs = JobModel.objects.filter(Q(title__icontains = query)
                                        |Q(skills__icontains = query))

    else:
        jobs = JobModel.objects.none()

    context = {
        'query': query,
        'jobs': jobs,
    }

    return render(req, 'search.html', context)


def skillMatchingPage(request):
    user = request.user

    if hasattr(user, 'JobSeeker') and user.JobSeeker:
        mySkill = user.JobSeeker.skills
        jobs = JobModel.objects.filter(skills=mySkill)
    

    context = {
        'jobs': jobs,
        'mySkill': mySkill
    }

    print(mySkill)  # Optional debugging print

    return render(request, "skill_match.html", context)


@login_required
def applyJob(req, job_id):

    job =  JobModel.objects.get(id=job_id)

    context = {
        'job':job,
    }

    if req.method == 'POST':
        cover = req.POST.get('cover')
        skills = req.POST.get('skills')
        resume = req.FILES.get('resume')

        apply = jobApplyModel(
            user = req.user,
            job = job,
            cover = cover,
            skills = skills,
            resume = resume
        )
        
        apply.save()
        return redirect('homePage')


    return render(req, 'apply_job.html',context)

def registerPage(req):

    if req.method == 'POST':
        user_name = req.POST.get('username')
        firstname = req.POST.get('firstname')
        lastname = req.POST.get('lastname')
        email = req.POST.get('email')
        user_type = req.POST.get('user_type')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')

        if password == confirm_password:

            user = Custom_User.objects.create_user(
            username = user_name,
            first_name = firstname,
            last_name = lastname,
            email = email,
            user_type = user_type,
            password = confirm_password 
            )

            if user_type == 'recruiter':
                RecruiterModel.objects.create(user=user)

            elif user_type == 'job_seeker':
                JobSeekerModel.objects.create(user=user)
            
            messages.success(req,'Registration successful!')
            return redirect('loginPage')

        else: 
            messages.warning(req,'Both password must be same!')


    return render(req, 'common/register.html')

def loginPage(req):

    if req.method == "POST":
        user_name = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username = user_name, password = password)
        
        if user is not None:
            login(req,user)
            messages.success(req,'Login successful!')

            return redirect('homePage')
        else:
            messages.warning(req, 'Username/Password is incorrect!')
            return redirect('loginPage')

    return render(req, 'common/login.html')


def logoutPage(req):
    logout(req)
    messages.success(req, 'Logout successful!')
    return redirect('loginPage')


@login_required
def profilePage(req):

    return render(req, 'profile.html')

@login_required
def createdJob(req):

    jobs = JobModel.objects.filter(user=req.user)

    context = {
        'jobs':jobs
    }

    return render(req, 'created_job.html', context)

@login_required
def addJob(req):

    if req.method == 'POST':
        jobTitle = req.POST.get('jobTitle')
        numberOfOpenings = req.POST.get('numberOfOpenings')
        category = req.POST.get('category')
        description = req.POST.get('description')
        skills = req.POST.get('skills')
        companyLogo = req.FILES.get('companyLogo')
        
        job = JobModel(
            user = req.user,
            title = jobTitle,
            num_of_openings = numberOfOpenings,
            category = category,
            description = description,
            skills = skills,
            company_logo = companyLogo

        )
        job.save()
        return redirect('createdJob')


    return render(req, 'add_job.html')

@login_required
def deleteJob(req,job_id):

    JobModel.objects.filter(id=job_id).delete()

    return redirect('createdJob')

@login_required
def editJob(req, job_id):


    jobs = JobModel.objects.get(id=job_id)

    context = {
        'jobs':jobs
    }

    if req.method == 'POST':
        jobId = req.POST.get('jobId')
        jobTitle = req.POST.get('jobTitle')
        numberOfOpenings = req.POST.get('numberOfOpenings')
        category = req.POST.get('category')
        description = req.POST.get('description')
        skills = req.POST.get('skills')

        if req.FILES.get('companyLogo'):
            company_logo = req.FILES.get('companyLogo')
        else:
            company_logo = jobs.company_logo

        
        job = JobModel(
            id = jobId,
            user = req.user,
            title = jobTitle,
            num_of_openings = numberOfOpenings,
            category = category,
            description = description,
            skills = skills,
            company_logo = company_logo

        )
        job.save()
        return redirect('createdJob')


    return render(req, 'edit_job.html', context)

@login_required
def viewJob(req, job_id):


    jobs = JobModel.objects.get(id=job_id)

    context = {
        'jobs':jobs
    }

    return render(req, 'view_job.html', context)