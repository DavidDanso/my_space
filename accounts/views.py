from django.shortcuts import redirect, render
from datetime import datetime
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
from .decorators import *

############################# USER AUTHENTICATION ################################
@unauthenticated_user
def registerUser(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, f'Account was created successfully for {username}')
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # change to admin name to be redirect to the admin page
            if username == "the_desiinger":
                return redirect('/')
            else:
                return redirect('user')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

############################# USER PAGES ################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def user_feed(request):
    # get projects, meetings & deals of user with the total counts
    projects = request.user.person.project_set.all()
    total_projects = projects.count()
    meetings = request.user.person.meeting_set.all()
    total_meetings = meetings.count()
    deals = request.user.person.deal_set.all()
    total_deals = deals.count()

    # show current projects, meetings or deals created
    reverse_project = projects[::-1]
    reverse_meeting = meetings[::-1]
    reverse_deal = deals[::-1]

    # condition statement to create project
    p_form = ProjectForm()
    if request.method == 'POST':
        p_form = ProjectForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            return redirect('user')

    # condition statement to create meeting
    m_form = MeetingForm()
    if request.method == 'POST':
        m_form = MeetingForm(request.POST)
        if m_form.is_valid():
            m_form.save()
            return redirect('user')

    # condition statement to create deal
    d_form = DealForm()
    if request.method == 'POST':
        d_form = DealForm(request.POST)
        if d_form.is_valid():
            d_form.save()
            return redirect('user')
    context = {'projects': projects, 'total_projects': total_projects, 'meetings': meetings, 'total_meetings': total_meetings, 'deals': deals, 'total_deals': total_deals, 'reverse_project': reverse_project, 'reverse_meeting': reverse_meeting, 'reverse_deal': reverse_deal, 'p_form': p_form, 'm_form': m_form, 'd_form': d_form}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def project_update(request, pk):
    user = request.user
    project = Project.objects.get(id=pk)
    formset = ProjectForm(instance=project)
    if request.method == 'POST':
        formset = ProjectForm(request.POST, instance=project)
        if formset.is_valid():
            formset.save()
            return redirect('user')

    context = {'user': user, 'project': project, 'formset': formset}
    return render(request, 'accounts/update_project-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def meeting_update(request, pk):
    user = request.user
    meeting = Meeting.objects.get(id=pk)
    formset = MeetingForm(instance=meeting)
    if request.method == 'POST':
        formset = MeetingForm(request.POST, instance=meeting)
        if formset.is_valid():
            formset.save()
            return redirect('user')

    context = {'user': user, 'meeting': meeting, 'formset': formset}
    return render(request, 'accounts/update_meeting-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def deal_update(request, pk):
    user = request.user
    deal = Deal.objects.get(id=pk)
    formset = DealForm(instance=deal)
    if request.method == 'POST':
        formset = DealForm(request.POST, instance=deal)
        if formset.is_valid():
            formset.save()
            return redirect('user')

    context = {'user': user, 'deal': deal, 'formset': formset}
    return render(request, 'accounts/update_deal-form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def deleteCurrentProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('user')

    context = {'project': project}
    return render(request, 'accounts/delete_info.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def deleteCurrentMeeting(request, pk):
    meeting = Meeting.objects.get(id=pk)
    if request.method == 'POST':
        meeting.delete()
        return redirect('user')

    context = {'meeting': meeting}
    return render(request, 'accounts/delete_info.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def deleteCurrentDeal(request, pk):
    deal = Deal.objects.get(id=pk)
    if request.method == 'POST':
        deal.delete()
        return redirect('user')

    context = {'deal': deal}
    return render(request, 'accounts/delete_info.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def accountSettingsUpdate(request):
    user_profile = request.user.person
    form = SettingsForm(instance=user_profile)
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()

    context = {'user_profile': user_profile, 'form': form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def deleteUser(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        return redirect('login')

    context = {'user': user}
    return render(request, 'accounts/delete.html', context)


############################# ADMIN PAGES ################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def adminPage(request):
    users = Person.objects.all()
    user_count = users.count()
    target_users = 1000
    user_num = user_count / target_users
    user_percentage = user_num * 100
    show_new_user = users[::-1]
    date = datetime.now()
    today = date.strftime("%a %d %b, %Y")  
    current_year =  date.strftime("%Y")
    # get projects, meetings & deals of user with the total counts
    projects = Project.objects.all()
    total_projects = projects.count()
    meetings = Meeting.objects.all()
    total_meetings = meetings.count()
    deals = Deal.objects.all()
    total_deals = deals.count()

    context = {'users': users, 'user_count': user_count, 'target_users': target_users, 'user_percentage': user_percentage, 'show_new_user': show_new_user, 'today': today, 'current_year': current_year, 'projects': projects, 'total_projects': total_projects, 'meetings': meetings, 'total_meetings': total_meetings, 'deals': deals, 'total_deals': total_deals}
    return render(request, 'accounts/home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def userProfile(request, pk): 
    user = Person.objects.get(id=pk)
    projects = user.project_set.all() 
    project_count = projects.count()  
    meetings = user.meeting_set.all() 
    meeting_count = meetings.count()
    deals = user.deal_set.all() 
    deal_count = deals.count()  

    context = {'user': user, 'projects': projects, 'project_count': project_count, 'meetings': meetings, 'meeting_count': meeting_count, 'deals': deals, 'deal_count': deal_count}
    return render(request, 'accounts/user_profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteUserProfile(request, pk):
    print(request.user)
    user = Person.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('/')

    context = {'user': user}
    return render(request, 'accounts/admin-delete_user.html', context)