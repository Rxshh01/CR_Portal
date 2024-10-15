from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
import pandas as pd
import numpy as np
#from ranklist import df


## import data tables from database
from .models import TaskZero
from .models import taskOne , taskTwo , taskThree , taskFour , taskFive,taskSix,taskSeven ,taskEight

# print(f"df from views : {df} ")

def time_view(request):
    return render(request, "time.html")
def tally_view(request):
    return render(request, "tally.html")
def team_view(request):
    return render(request, "team.html")

def scorecard_view(request):
    return render(request, "cr_marks.html")
# Create your views here.


from .models import email_auto

def email_in(request):
    return render(request,"email_in.html")
def email_submission(request):
    if request.method == "POST":
        name = request.POST.get('name_form', '')
        email = request.POST.get('email_form', '')
        data=email_auto(name=name,email=email)
        data.save()

    params={'name_html':data.name,
             'email_html':data.email
    }
    print("mailing start")
    import boto3
    import datetime as dt
    def publish_message(message):
        arn = ''
        sns = boto3.resource('sns', aws_access_key_id="AKIA3TGK5AWKEZFOA2NH", 
                            aws_secret_access_key="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",
                            region_name='ap-south-1')
        topic = sns.Topic(arn)
        x = dt.datetime.now()
        message = {
            "default": "Sample fallback message",
            "email": message
        
        }
        response = topic.publish(Message=str(json.dumps(message)), Subject="Alert", MessageStructure='json')
        return response
    from botocore.exceptions import ClientError

    SENDER = "Symposium <symposium@aakaariitbombay.org>"
    mail=[data.email]

    sent = 0
    num = -1

    for i in mail:
        num +=1
        RECIPIENT = i
        name = data.name
    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = "us-east-1"

    # # The subject line for the email.
        SUBJECT = "Automated Mail Successful !"

        BODY_HTML=("Hi " + data.name +"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        
        <style>
            .text {
                font-size: 15px;
                font-family: " Arial, Helvetica, sans-serif; ";
            }
        </style>
    </head>

    <body>
        <div class="text">
            <p></p>
            <p>automated mail is working !<br> GREAT! <br>
            Aakaar 2023, <br>
            IIT Bombay.</p>
        </div>

    </body>

    </html>
    """)
        
        CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
        try:
        #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
    #                     'Text': {
    #                         'Charset': CHARSET,
    #                         'Data': BODY_TEXT,
    #                     },
                        'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
    #         ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            sent +=1
            print("Email",sent,"sent! Message ID:" ),
            print(response['MessageId'])


        return render(request,'email_submission.html',params)



def home(request):
    return render(request, "home.html")
def compi_home(request):
    return render(request,"compi_home.html")
def aakaar_new(request):
    return render(request,"aakaar_new.html")


def dashboard(request):
    user = request.user
    data = SocialAccount.objects.get(user=user).extra_data
    email = data.get('email')
    name = data.get('name')
    name = name.split(" ")
    picture = data.get('picture')
    # print(rank_list)
    #for i in range(len(rank_list)):
     #   if rank_list[i]:
      #      rank = i+1
       #     break
    
    is_filled = False
    objects = TaskZero.objects.all()
    current_obj = ''
    for obj in objects:
        if obj.crid == crid:
            is_filled=True
            current_obj = obj
            break
    is_filled_taskone = len(taskOne.objects.filter(crid=crid))==1
    is_filled_tasktwo = len(taskTwo.objects.filter(crid=crid))==1
    is_filled_taskthree = len(taskThree.objects.filter(crid=crid))==1
    is_filled_taskfour = len(taskFour.objects.filter(crid=crid))==1
    is_filled_taskfive= len(taskFive.objects.filter(crid=crid))==1
    is_filled_tasksix= len(taskSix.objects.filter(crid=crid))==1
    is_filled_taskseven= len(taskSeven.objects.filter(crid=crid))==1
    is_filled_taskeight= len(taskEight.objects.filter(crid=crid))==1


    return render(request, "dashboard.html", 
    {'email': email,
     "name":name[0], 
     "picture": picture, 
     "CRID":"AK"+str(current_user_id),
     "rank":rank, 
     "objects":objects,
     "is_filled": is_filled,
     "is_filled_taskone": is_filled_taskone,
     "is_filled_tasktwo": is_filled_tasktwo,
     "is_filled_taskthree": is_filled_taskthree,
    "is_filled_taskfour":is_filled_taskfour,
   "is_filled_taskfive":is_filled_taskfive,
 "is_filled_tasksix":is_filled_tasksix,
 "is_filled_taskseven":is_filled_taskseven,
 "is_filled_taskeight":is_filled_taskeight,
     "current_obj": current_obj
    })

def redirect_view(request):
    response = redirect('/home')
    return response

def updateProfile(request):
    if request.method == "POST":
        user = request.user
        username = user.username
        
        current_user_id = 230000 + user.id
        crid = "AK"+str(current_user_id)
        email = user.email
        colgName = request.POST.get('colName', '')
        names = request.POST.get('names', "")
        emails = request.POST.get("emails", "")
        state = request.POST.get('state', '')
        mobileNo = request.POST.get('phoneNo','')
        dept = request.POST.get('dept', '')
        whatsappNo = request.POST.get('whatsNo','')
        pincode = request.POST.get('pin', '')
        address = request.POST.get('address', '')
        print(crid, username, colgName, state, mobileNo, whatsappNo, dept, pincode, address)
        is_filled = False
        objects = TaskZero.objects.all()
        current_obj = ''
        for obj in objects:
            if obj.crid == crid:
                is_filled = True
                current_obj = obj
                break
        if not is_filled:
            response = TaskZero(crid=crid, username=username, colgName=colgName, state=state, mobileNo=mobileNo,
                                whatsappNo=whatsappNo, dept=dept, pincode=pincode, address=address, names=names, email=email, emails = emails)
            response.save()
        else:
            objects = TaskZero.objects.get(crid=crid)
            objects.delete()
            response = TaskZero(crid=crid, username=username, colgName=colgName, state=state, mobileNo=mobileNo,
                                whatsappNo=whatsappNo, dept=dept, pincode=pincode, address=address, names=names, email=email, emails = emails)
            response.save()

    return  redirect('dashboard')


def task1(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link','')

        is_filled_taskone = len(taskOne.objects.filter(crid=crid)) == 1

        if is_filled_taskone:
            objects = taskOne.objects.get(crid=crid)
            objects.delete()
            response = taskOne(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskOne(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')

def task2(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link','')

        is_filled_tasktwo = len(taskTwo.objects.filter(crid=crid)) == 1

        if is_filled_tasktwo:
            objects = taskTwo.objects.get(crid=crid)
            objects.delete()
            response = taskTwo(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskTwo(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')


def task3(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link','')

        is_filled_taskthree = len(taskThree.objects.filter(crid=crid)) == 1

        if is_filled_taskthree:
            objects = taskThree.objects.get(crid=crid)
            objects.delete()
            response = taskThree(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskThree(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')


def task4(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link4','')

        is_filled_taskfour = len(taskFour.objects.filter(crid=crid)) == 1

        if is_filled_taskfour:
            objects = taskFour.objects.get(crid=crid)
            objects.delete()
            response = taskFour(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskFour(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')



def task5(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link5','')

        is_filled_taskfive = len(taskFour.objects.filter(crid=crid)) == 1

        if is_filled_taskfive:
            objects = taskFive.objects.get(crid=crid)
            objects.delete()
            response = taskFive(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskFive(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')


def task6(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link','')

        is_filled_tasksix = len(taskSix.objects.filter(crid=crid)) == 1

        if is_filled_tasksix:
            objects = taskSix.objects.get(crid=crid)
            objects.delete()
            response = taskSix(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskSix(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')


def task7(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link7','')

        is_filled_taskseven = len(taskSeven.objects.filter(crid=crid)) == 1

        if is_filled_taskseven:
            objects = taskSeven.objects.get(crid=crid)
            objects.delete()
            response = taskSeven(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskSeven(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')


def task8(request):
    if request.method == "POST":
        user = request.user
        username = user.first_name
        id = 230000 + user.id
        crid = "AK"+str(id)
        email = user.email
        link = request.POST.get('link8','')

        is_filled_taskeight = len(taskEight.objects.filter(crid=crid)) == 1

        if is_filled_taskeight:
            objects = taskEight.objects.get(crid=crid)
            objects.delete()
            response = taskEight(crid=crid, email=email, username=username, link=link, marks=0)
            response.save()
        else:
            response = taskEight(crid=crid, email=email,
                               username=username, link=link, marks=0)
            response.save()

    return  redirect('dashboard')

def logiq(request):
    return render(request, "logiq.html")

def leaderboard(request):
    task1 = taskThree.objects.all()
    task2 = taskTwo.objects.all()
    task3 = taskOne.objects.all()
    task4 = taskFour.objects.all()
    task5 = taskFive.objects.all()
    task6 = taskSix.objects.all()
    task7 = taskSeven.objects.all()
    task8 = taskEight.objects.all()
    leaderboard  = {}
    for obj in task1:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)
    for obj in task2:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)
    for obj in task3:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)
    for obj in task4:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)
    for obj in task5:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)
    for obj in task6:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)
    for obj in task7:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)
    for obj in task8:
        if leaderboard.get(obj.crid):
            leaderboard[obj.crid] += int(obj.marks)
        else:
            leaderboard[obj.crid] = int(obj.marks)   
    sorted_leaderboard = {k: v for k, v in sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)}
    top_five_crids = list(sorted_leaderboard.items())[:5]
    return render(request, "leaderboard.html", {"top_crids": top_five_crids})