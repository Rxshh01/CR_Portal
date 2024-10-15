import datetime as dt
import json
# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.

from . models import fnb_model ,pitch_submission

def google(request):
    return render(request,'google.html')

def smart_home(request):
    user=request.user
    is_register=False

    if user.is_authenticated:
        email_goggle=user.email
        is_register=len(fnb_model.objects.filter(email1=email_goggle))==1
    return render(request,'smart_pitch.html',{'is_register':is_register})

def register_view(request):

    return render(request,'form.html')


def pitch_view(request):
    
    return render(request,'pitch_form.html')


def pitch_submitted(request):



    if request.method=='POST':
        pitch_email=request.POST.get('pitch_email','')
        pitch_link=request.POST.get('pitch_link','')
        pitch_video=request.POST.get('pitch_video','')


        data=pitch_submission(pitch_email=pitch_email,pitch_link=pitch_link,pitch_video=pitch_video)
        data.save()





    return redirect('home_view')




#def registered(request):



#    if request.method=='POST':
#        email1=request.POST.get('email1','')
#        startup_name=request.POST.get('startup_name','')
#        web_link=request.POST.get('web_link','')
#        pvt_yn=request.POST.get('pvt_yn','')
#        details=request.POST.get('details','')
#        contact=request.POST.get('contact',0)
#        city=request.POST.get('city','')
#        theme=request.POST.get('theme','')
#        unique=request.POST.get('unique','')
#        stage=request.POST.get('stage','')
#        validation=request.POST.get('validation','')

#        patent=request.POST.get('patent','')
#        incubated=request.POST.get('incubuted','')
#        incubator_name=request.POST.get('incubutor_name','')
#        looking_for=request.POST.get('looking_for','')


#        data=fnb_model(email1=email1,startup_name=startup_name,web_link=web_link,pvt_yn=pvt_yn,details=details,contact=contact,city=city,theme=theme,unique=unique,stage=stage,validation=validation,patent=patent,incubated=incubated,incubator_name=incubator_name,looking_for=looking_for)
#        data.save()
        




#    return redirect('home_view')

def registered(request):
    
   

    if request.method=='POST':
        email1=request.POST.get('email1','')
        startup_name=request.POST.get('startup_name','')
        web_link=request.POST.get('web_link','')
        pvt_yn=request.POST.get('pvt_yn','')
        details=request.POST.get('details','')
        contact=request.POST.get('contact','')
        city=request.POST.get('city','')
        theme=request.POST.get('theme','')
        unique=request.POST.get('unique','')
        stage=request.POST.get('stage','')
        validation=request.POST.get('validation','')
        patent=request.POST.get('patent','')
        incubated=request.POST.get('incubated','')
        incubator_name=request.POST.get('incubator_name','')
        looking_for=request.POST.get('looking_for','')

            
        data=fnb_model(email1=email1,startup_name=startup_name,web_link=web_link,pvt_yn=pvt_yn,details=details,contact=contact,city=city,theme=theme,unique=unique,stage=stage,validation=validation,patent=patent,incubated=incubated,incubator_name=incubator_name,looking_for=looking_for)
        data.save()

        import boto3
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


        SENDER = "Divyansh Agarwal <divyansh@aakaariitbombay.org>"


        mail=[email1]

# name = ["Aditya Ola","shubahm","Avinash","Akshat","Dinesh","Vaishnavi","Manasi","Shreyanshi","Tanvii","Diyansh Agarwal","Nitin","Aditya Malhotra","Rohit","Ahish","Himanshi","Dhruvi","Dhananjay"]
        sent = 0
        num = -1

        for i in mail:
            num +=1
            RECIPIENT = i
            
            name='startapp1'
            






            AWS_REGION = "us-east-1"

# # The subject line for the email.
            SUBJECT = "Registration Confirmation | Smart Pitch, Aakaar IIT Bombay"
   
    #text = ("Dear " + "\033[1m" +name[0]+ "\033[0m" + ","+"\n\nThank you for registering for the Revit Architecture competition conducted by Aakaar,\nIIT Bombay in association with Bimlabs Global.\n\nParticipants will get a chance of winning prizes worth " + "\033[1m" + '₹ 20,000' + "\033[0m" + "\nAlong with Scholarships on courses worth " + "\033[1m" + '₹ 13L+!! ' + "\033[0m" + " \nAlso, get the opportunity to get  " + "\033[1m" + '3 Month Online training + 1-month Internship + Placement Training + Minimum 3 Interviews at BIM Companies in India,' + "\033[0m" + "\n\n" + "\033[1m" + 'Please find the problem statement below link: \n' + "\033[0m" + " https://bit.ly/Revit-Problem-Statement \nSubmission Link:  https://bit.ly/revit-submission \nSubmission Deadline: " + "\033[1m" + '25 November 2022 ' + "\033[0m" + " \nFor any queries,\nContact: competition@aakaariitbombay.org \n\nAll the best !!! \n\nRegards")
# The email body for recipients with non-HTML email clients.
#     BODY_TEXT = ( "dear"+name[num]
# #                 )
#     BODY_HTML=("""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
# </head>
# <body>
#     <img class="mx-auto rounded-circle" src="https://raw.githubusercontent.com/Himanshi62/AAKAAR/main/aakar-website/static/img/compi_revit.jpeg" width="240px" height="240px" alt="..." style="border-bottom: 5px solid #355681; object-fit: cover;" />
# </body>
# </html>""")
            BODY_HTML=("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="msapplication-TileColor" content="#da532c">
    <meta name="theme-color" content="#ffffff">

    <style>
        
    </style>
</head>

<body>
    <div class="text">
         

        <p>Hello {name},</p>
    <p>Thank you for registering for Smart Pitch, Aakaar IIT Bombay 2023.</p>
    <p>We’d like to confirm that your registration is completed successfully. After registering, you must complete the pitch submission form. </p>
    <p>For Detailed instruction go through - <a href="https://drive.google.com/file/d/1WpccVPd742a8ev64v5PPTt2pr7qO_Cok/view?usp=sharing">Drive Link</a> </p>
     <p>Link for Pitch submission - <a href="https://aakaariitbombay.org/smartpitch/pitch_submission">Pitch Submission Link</a> </p>
    <p>Reference Template for the Pitch presentation - <a href="https://docs.google.com/presentation/d/1Pl9DIK8ZnVMeFceC8NmduG9ZpHbGlslv/edit?usp=sharing&ouid=103419826893457841629&rtpof=true&sd=true">Reference Link</a> </p>  
  <p><strong>NOTE:</strong>  You may use your own template if you already have one</p>
  <p>If you experience any issues logging into your account, reach out to us at <a href="mailto:divyansh@aakaariitbombay.org">divyansh@aakaariitbombay.org</a> .</p>
  <p>
    Regards  <br>
<strong> Divyansh Agarwal</strong> <br>
Hospitality Head 2022-23 <br>
Aakaar IIT Bombay <br>
Department of Civil Engineering <br>
Indian Institute of Technology Bombay <br>
E: <a href="mailto:divyansh@aakaariitbombay.org">divyansh@aakaariitbombay.org</a>  <br>
M: <a href="tel:+917985654816">+917985654816</a>  <br>
  </p>
    </div>

</body>

</html>
""".format(name=startup_name))
    

# The character encoding for the email.
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
                        ]
        #                 ,
        #                 'CcAddresses': [
        #             'shubhamjadhavsss123@gmail.com'
        #         ],
        #         'BccAddresses': [
        #            '200040067@iitb.ac.in'
        #         ]
                
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

        
        
            

    return redirect('home_view')
