from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import userSignupPage
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Profile, Mail, SaveDatasM, CompanyCodeModel, CategoryGroupModel, UserOfCGM, CGChartModel
# for date and month
from datetime import datetime
# ctrl + sift + p
# reload windoe
from dateutil.relativedelta import relativedelta

# Create your views here.
def signUpPageFunction(request):
    users = userSignupPage()
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            CC = request.POST.get('Company_Code') ; C1 = 0 
            lstOfCompanyCodeOffice = ['AND1234567', 'BOR8976888', 'DR09009267', 'GHK98206468']
            for CCO in lstOfCompanyCodeOffice:
                if CC == CCO:
                    C1 += 1
                    break
                else:
                    continue

            if C1 == 1:
                users = userSignupPage(request.POST)

                if users.is_valid():
                    user = users.save()
                    
                    CCM_Obj = CompanyCodeModel(
                        CompanyId = request.POST.get('Company_Code'),
                        user_name = user,
                        user_pass = request.POST.get('password2'),
                    )

                    CCM_Obj.save()
                    
                    contact = request.POST.get('contact_no')

                    obj = Profile(
                        name = user,
                        contact_no = contact
                    )
                    obj.save()
                    return redirect('login')
            else:
                pass
        else:
            pass

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
    about_company = "We are a modern tech-driven organization focused on simplifying office management processes. Our goal is to enhance productivity, transparency, and security in day-to-day operations. With an experienced leadership team and dedicated staff, we ensure smooth workflow across all departments."

    inside_company = [
        'office.jpg', 'office.jpg', 'office.jpg',
    ]

    trusted_companies = [
        "AlphaSoft Pvt Ltd",
        "BrightEdge Tech",
        "CodeVerse Inc.",
        "NextGen Solutions",
        "VisionStack",
        "CloudEdge",
        "MindSpark",
        "DataNest"
    ]

    ourSystem = [
        {
            'headingPoint' : 'Fast Workflow',
            'icons' : 'bi bi-speedometer2 fs-1 mb-2',
            'text' : 'Streamline employee operations with minimal delay.',
        },
        {
            'headingPoint' : 'Secure Data',
            'icons' : 'bi bi-shield-lock fs-1 mb-2',
            'text' : 'our company’s information is encrypted and safe.',
        },
        {
            'headingPoint' : 'Team Friendly',
            'icons' : 'bi bi-people fs-1 mb-2',
            'text' : 'Collaborate, assign tasks, and manage users easily.',
        },
        {
            'headingPoint' : 'Growth Oriented',
            'icons' : 'bi bi-graph-up-arrow fs-1 mb-2',
            'text' : 'Analyze reports and improve overall productivity.',
        },

    ]
    
    tech_stacks = [
        {
            "techname": "Python",
            "techimages": "office.jpg"
        },
        {
            "techname": "Django",
            "techimages": "office.jpg"
        },
        {
            "techname": "MySQL / SQL",
            "techimages": "office.jpg"
        },
        {
            "techname": "Bootstrap",
            "techimages": "office.jpg"
        },
        {
            "techname": "Node.js",
            "techimages": "office.jpg"
        },
        {
            "techname": "HTML",
            "techimages": "office.jpg"
        },
        {
            "techname": "CSS",
            "techimages": "office.jpg"
        },
        {
            "techname": "JavaScript",
            "techimages": "office.jpg"
        }
    ]

    sections = [
        {
            "title": "🚀 Simple Registration Process",
            "description": "We make joining easy and transparent. Apply online, attend a short interview, and go through our smooth onboarding. Whether you're a fresher or experienced, there's an opportunity for you.",
            "image": "office.jpg",
            "alt": "Join Us",
            "reverse": False
        },
        {
            "title": "🎓 Internship Programs",
            "description": "Our internship programs offer real-world experience, mentorship from seniors, and project-based learning. Perform well, and you might secure a full-time position with us!",
            "image": "office.jpg",
            "alt": "Internship",
            "reverse": True
        },
        {
            "title": "👔 Managerial Roles",
            "description": "Managers lead our teams with vision. They track progress, assign roles, and boost productivity. We empower them with dashboards and autonomy to build results-driven teams.",
            "image": "office.jpg",
            "alt": "Manager Role",
            "reverse": False
        },
        {
            "title": "🏢 Modern Workplace Facilities",
            "description": "High-speed internet, chill zones, meeting rooms, and cafeterias — we care for our people. Our workspace is built to inspire, relax, and support your daily work-life balance.",
            "image": "office.jpg",
            "alt": "Facilities",
            "reverse": True
        },
        {
            "title": "📈 Career Growth & Learning",
            "description": "Employees receive training, rewards, and promotion opportunities. Our internal LMS and weekly sessions help you upgrade skills and climb the ladder with confidence.",
            "image": "office.jpg",
            "alt": "Growth Opportunities",
            "reverse": False
        },
    ]

    count_tc = len(trusted_companies)

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
        'about_company' : about_company,
        'inside_company' : inside_company,
        'trusted_companies' : trusted_companies,
        'count_tc' : count_tc,
        'ourSystem' : ourSystem,
        'tech_stacks' : tech_stacks,
        'sections' : sections,
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
    # print(checkUserDataForTable)
    # print()
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
        return redirect('sendUs')

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
        return redirect('sendUs')
        
    context = {
        'obj' : obj,
    }
    return render(request, 'profileEmail.html', context)

def ownMailSendPageFunction(request):
    mails = Mail.objects.filter(user_name = request.user.username)
    user_data = User.objects.get(username = request.user.username)

    first = user_data.first_name + ' ' + user_data.last_name

    for mail in mails:
        one_month_later = mail.text_time + relativedelta(months=1)
        print(mail.text_time + relativedelta(months=1))
        # print(mail.text_time)
        # print(bool(mail.text_time > one_month_later))
        if mail.text_time > one_month_later:
            mail.delete()
        
    context = {
        'check' : 2,
        'u_name' : first,
        'mail' : mails,
        'ct_mail' : mails.count()
    }
    return render(request, 'mail.html', context)

def MailOpenPageFunction(request, mail_id, Page_Check):
    if int(Page_Check) == 3:
        MailDatas = SaveDatasM.objects.get(savemail_data = mail_id)
        context = {
            'mailData' : MailDatas,
            'Check_Name' : 'savemail',
            'Page_Check' : int(Page_Check),
        }

    else:
        MailData = Mail.objects.get(id = mail_id)
        checkData = SaveDatasM.objects.all().values()
        c1 = 0
        for cd in checkData:
            # print(type(cd['savemail_data'])) # str
            # print(type(MailData.id)) # int
            if int(cd['savemail_data']) == int(MailData.id):
                c1 += 1
                # print('heloo')

        if c1 == 1:
            saveButton = 1
        else:
            saveButton = 0

        Check_Name = ''
        if Page_Check == 1:
            Check_Name = 'Sender'
        elif Page_Check == 2:
            Check_Name = 'Reciver'
        
        context = {
            'saveButton' : saveButton,
            'Check_Name' : Check_Name,
            'mailData' : MailData,
        }
    
    return render(request, 'MailOpenPage.html', context)

def DirectMessageFromMail(request, obj, choice):
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
        return redirect('sendUs')
    
    context = {
        'obj' : obj,
    }
    return render(request, 'profileEmail.html', context)

def DeleteMessagePageFunction(request, msg_id, Page):
    if int(Page) == 1:
        MailDelete = Mail.objects.get(id = msg_id)
        MailDelete.delete()
        return redirect('sendUs')
    elif int(Page) == 2:
        SaveMail = SaveDatasM.objects.filter(savemail_data = msg_id).first()
        SaveMail.delete()
        return redirect('SaveMail')
    else:
        return HttpResponse('Page Not Found')

def successfullSaveMailPageFunction(request, mail_id):
    mail = Mail.objects.get(id = mail_id)
    SM = SaveDatasM(
        savemail_data = mail.id,
        names = mail.names,
        user_name = mail.user_name,
        subject = mail.subject,
        text = mail.text,
        files = mail.files,
        text_time = mail.text_time,
    )
    SM.save()
    return render(request, 'successfullSaveMail.html')

def saveMailPageFunction(request):
    mails = SaveDatasM.objects.filter(names = request.user.id)
    context = {
        'mails' : mails,
        'Check' : '3',
    }
    return render(request, 'saveMail.html', context)

# create group 
def createGroupPageFunction(request):
    if request.method == 'POST':
        CGM_Image = request.POST.get('CGM_Image')
        CGM_Name = request.POST.get('CGM_Name')
        CGM_Category = request.POST.get('Category')
        CGM_Description = request.POST.get('CGM_Description')
        CGM_Slogon = request.POST.get('CGM_Slogon')

        CGM = CategoryGroupModel(
            CGM_Image = CGM_Image,
            CGM_Name = CGM_Name,
            CGM_Category = CGM_Category,
            CGM_Description = CGM_Description,
            CGM_Slogon = CGM_Slogon,
        )

        CGM.save()

        user_data = User.objects.get(id = request.user.id)
        user_profile_data = Profile.objects.get(id = user_data.id)
        
        UOC_connect = CategoryGroupModel.objects.get(id = CGM.id)
        UOC_Id = int(user_profile_data.id)
        UOC_username = user_data.username
        UOC_Category = 'Admin'

        GroupChatUserList = [
            {
                "UOC_connect" : UOC_connect,
                "UOC_Id" : UOC_Id,
                "UOC_username" : UOC_username,
                "UOC_Category" : UOC_Category,
            },
        ]

        Owner_Data = Profile.objects.filter(user_category = 'Owner')
        for UserLoop in range(len(Owner_Data)):
            dct = {}

            dct['UOC_connect'] = UOC_connect
            dct['UOC_Id'] = Owner_Data[UserLoop].id

            user_Model_Data = User.objects.get(id = Owner_Data[UserLoop].id)
            dct['UOC_username'] = user_Model_Data.username

            dct['UOC_Category'] = 'Admin'

            GroupChatUserList += [dct]

        for DataInList in GroupChatUserList:
            UC = UserOfCGM(
                UOC_connect = DataInList['UOC_connect'],
                UOC_Id = DataInList['UOC_Id'],
                UOC_username = DataInList['UOC_username'],
                UOC_Category = DataInList['UOC_Category'],
            )

            UC.save()
        
        return redirect('home')

    return render(request, 'createGroup.html')