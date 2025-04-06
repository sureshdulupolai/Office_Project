from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import userSignupPage
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Profile, Mail

# Create your views here.
def signUpPageFunction(request):
    users = userSignupPage()
    if request.method == 'POST':
        users = userSignupPage(request.POST)

        if users.is_valid():
            user = users.save()

            contact = request.POST.get('contact_no')

            obj = Profile(
                name = user,
                contact_no = contact
            )
            obj.save()
            return redirect('home')

    context = {
        'form' : users
    }

    return render(request, 'signup.html', context)

def LoginPageFunction(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def logoutPageFunction(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect('home')
        else:
            return render(request, 'logout.html')
    else:
        pass


def homePageFunction(request):
    profile_count = Profile.objects.all().values().count()
    profiles = list(Profile.objects.all().values())
    # for ss in list(Profile.objects.all().values()):
    #     print(ss)

    a1 = 0; a2 = 0
    for i in profiles:
        if i['user_category'] == 'Owner':
            a1 += 1
        elif i['user_category'] == 'Manager':
            a2 += 1
    a3 = (profile_count - (a1 + a2))

    context = {
        'pf_count' : a3,
        'manager' : a2,
        'owner' : a1,
    }
    return render(request, 'home.html', context)

def tablePageFunction(request):
    profile = list(Profile.objects.all().values())

    for a1 in range(len(profile)):
        for a2 in range(len(profile)):
            if profile[a1]['user_category'][:1] > profile[a2]['user_category'][:1]:
                profile[a1], profile[a2] = profile[a2], profile[a1]

    lst = []; lst_data = []
    for i in profile:
        lst += [i['name_id']]
        
    for j in range(len(lst)):
        lst_data += [User.objects.get(id=lst[j])]

    zipped_data = zip(profile, lst_data)

    checkUserDataForTable = request.GET.get('search_user')
    print(checkUserDataForTable)
    print()
    if checkUserDataForTable:
        filtered_zipped_data = []
        for zipData1, zipData2 in zipped_data:
            CheckUser = User.objects.get(id = zipData1['name_id'])
            if (checkUserDataForTable in CheckUser.username) or (checkUserDataForTable in CheckUser.first_name) or (checkUserDataForTable in CheckUser.last_name):
                filtered_zipped_data += [(zipData1, zipData2)]
        zipped_data = filtered_zipped_data

    context = {
        'zipped_data' : zipped_data
    }

    return render(request, 'table.html', context)

def profilePageFunction(request, id = None, names = None, check = 0):
    obj = Profile.objects.get(name = id)
    no1 = obj.contact_no[:5]
    no2 = obj.contact_no[5:]
    if obj.desc:
        desc = obj.desc
    else:
        desc = ' "The user hasn`t shared any information yet. 📝" '
    # print(type(check))
    context = {'obj' : obj, 'no1' : no1, 'no2' : no2, 'desc' : desc, 'check' : check}
    return render(request, 'profile.html', context)

def editProfilePageFunction(request):
    if request.method == 'POST':
        user = request.user
        if request.POST.get('first_name'):
            user.first_name = request.POST['first_name']
        if request.POST.get('last_name'):
            user.last_name = request.POST['last_name']
        user.save()

        obj = Profile.objects.get(name=request.user)

        if request.FILES.get('user_image'):
            obj.user_image = request.FILES['user_image']

        if request.POST.get('desc'):
            obj.desc = request.POST['desc']

        if request.POST.get('contact_no'):
            obj.contact_no = request.POST['contact_no']

        obj.save()

        return redirect('home')

    return render(request, 'edit.html')

def mailPageFunction(request):
    user_data = User.objects.get(username = request.user.username)
    mails = Mail.objects.filter(names = request.user.id)

    count_mail = mails.count()

    first = user_data.first_name + ' ' + user_data.last_name

    context = {
        'check' : 1,
        'u_name' : first,
        'mail' : mails,
        'ct_mail' : count_mail,
    }
    
    return render(request, 'mail.html', context)

def mailSendPageFunction(request):
    if request.method == 'GET':
        if request.GET.get('query'):
            data = User.objects.filter(username__icontains=request.GET.get('query'))
            if not data:
                data = User.objects.filter(username__icontains=request.GET.get('query')[:1])
        else:
            data = None

    elif request.method == 'POST':
        selected_user_id = request.POST.get('user_names')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        files = request.FILES.get('files')
        username = str(request.user.username)

        # Get the User object
        # print(selected_user_id)
        selected_user = User.objects.get(username=selected_user_id)
        # print(selected_user)

        obj = Mail(
            names=selected_user,
            user_name=username,
            subject=subject,
            text=text,
            files=files
        )
        obj.save()
        return redirect('home')

    context = {
        'users': data,
    }
    return render(request, 'mailsend.html', context)

def profileEmailPageFunction(request, obj):
    if request.method == 'POST':
        selected_user_id = obj
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        files = request.FILES.get('files')
        username = str(request.user.username)

        # Get the User object
        # print(selected_user_id)
        selected_user = User.objects.get(username=selected_user_id)
        # print(selected_user)

        obj = Mail(
            names=selected_user,
            user_name=username,
            subject=subject,
            text=text,
            files=files
        )
        obj.save()
        return redirect('home')
    
    context = {
        'obj' : obj,
    }
    return render(request, 'profileEmail.html', context)

def ownMailSendPageFunction(request):
    mails = Mail.objects.filter(user_name = request.user.username)
    user_data = User.objects.get(username = request.user.username)

    first = user_data.first_name + ' ' + user_data.last_name

    context = {
        'check' : 2,
        'u_name' : first,
        'mail' : mails,
        'ct_mail' : mails.count()
    }
    return render(request, 'mail.html', context)

def MailOpenPageFunction(request, mail_id, Page_Check):
    MailData = Mail.objects.get(id = mail_id)
    Check_Name = ''
    if Page_Check == 1:
        Check_Name = 'Sender'
    elif Page_Check == 2:
        Check_Name = 'Reciver'

    context = {
        'Check_Name' : Check_Name,
        'mailData' : MailData,
    }
    
    return render(request, 'MailOpenPage.html', context)