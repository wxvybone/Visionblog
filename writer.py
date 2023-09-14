import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser

writer = input("Your Name: ")
sender_email = input('What is your email address? ')
recipient = input("Recipient(s) ")
receiver_email = input('What is their email address(es)? ')
subject = input('What is the subject? ')

tone = input("Select a tone: Acceptance, Apology,Congratulations, Create, Request, Rejection: ")
def email_writer():
    global body
    
    if tone.lower() == "apology":
        action = input("what are you sorry for? ")
        tone2 = input('Formal or Informal? ')
        if tone2.lower() == 'formal':
            body = f"Dear " + str(recipient) + ","
            body+= f'''I would like to formally apologize for ''' + str(action) + '''. 
I understand that it was a poor choice of mine and I would stop at 
nothing to correct this issue in your eyes.I hope you can forgive me 
for what I have done. We deserve to move past this and excel with other
aspects of our lives.

'''
            body += f'''Thank you for reading this, and I hope you are well.
Yours Sincerely, 
{writer}'''
        else:
            body = f"Dear " + str(recipient) + ","
            body += f'I am sorry for ' + str(action) + '''. I did not know it would 
become as much of a deal as it did, but i apologize nonetheless. 
I do feel like this is a rather petty issue we can look past if you feel 
so too. I hope we can stay in touch after this rough patch in our relationship.


I hope you're doing well so we can hang out some time.
{writer}'''

    elif tone.lower() == "congratulations":
        action = input("What did they do? ")
        tone2 = input('Formal or Informal? ')

        if tone2.lower() == 'informal':
            body = f"Hey {recipient},"
            body+= f'''I hope this email finds you well. I just wanted to drop you a 
quick note to offer my heartfelt congratulations on your recent achievement! 

I heard the fantastic news and couldn't be happier for you. Your hard work, dedication, 
and perseverance have truly paid off, and it's inspiring to see you reach this milestone. 
Your ability to {action} shows that your determination knows no bounds.

I have always believed in your abilities, and I'm thrilled to see you succeed. This 
achievement is a testament to your skills and the incredible person you are. Keep aiming 
high and chasing after your dreams. This is just the beginning of many more great things 
to come.

If you ever want to celebrate or share more about your experience, Feel free to 
reach out anytime.

Once again, congratulations!

Take care and talk soon,
{writer}'''
        else:
            body = f'Dear {recipient},'
            body += f'''I trust this email finds you in the best of health and spirits. 
It is with great pleasure and immense admiration that I extend my warmest congratulations 
to you on your exceptional achievement.
Your dedication, perseverance, and unwavering commitment have led you to this remarkable 
milestone, and it is truly an honor to witness your success. Your {action} speaks 
volumes about your dedication to excellence.
Your accomplishment is a testament to your outstanding capabilities, and I have every 
confidence that this achievement marks only the beginning of a journey filled with even 
greater accomplishments. Should you wish to share your insights or experiences surrounding 
this achievement, I am genuinely eager to engage in conversation. Your journey undoubtedly 
holds valuable lessons for all of us who have the privilege of working alongside you.

Once again, congratulations on this momentous achievement. May your path be ever luminous 
and your aspirations continue to soar.
Wishing you continued success and fulfillment.

Warmest regards,
{writer}'''

    elif tone.lower() == 'request':
        action = input("What are you asking? ")
        tone2 = input('Formal or Informal? ')

        if tone2.lower() == 'informal':
            body = f"Hey  {recipient},"
            body += f'''I hope you're doing well. I wanted to reach out and ask if you could {action}.
I know you have a busy schedule, and I genuinely appreciate your time and consideration. If it's convenient for you, 
I would love to discuss this further and provide more context. I look forward to hearing from you whenever you get a chance. 
Thanks in advance for your help!

Take care,
{writer}'''

        else:
            body = f'Dear ' + str(recipient) + ','
            body += f'''I trust this email finds you well. I am writing to respectfully request 
that you ''' + str(action) + '''. I am aware of the demands on your time and expertise, and 
I sincerely appreciate any consideration you can give to my request. If it aligns with your 
schedule, I would be grateful for the opportunity to discuss this matter in more detail at 
your convenience.
Your insights and assistance would be invaluable, and I truly thank you for considering my 
request.

Wishing you a productive and fulfilling day ahead.

Warm regards,
{writer}'''

    elif tone.lower() == 'rejection':
        job = input('Organization Name? ')
        interest = input("what is the position of interest? ")
        action = input("what stood out about the person? ")
        tone2 = input('Formal or Informal? ')

        if tone2.lower() == 'informal':
            body = f'Dear' + str(recipient) + ','
            body += f'''I hope this email finds you well. I want to express my appreciation 
for your interest in''' + str(interest) + '''at ''' + str(job) + '''.

After careful consideration, we regret to inform you that we have chosen to move forward with 
other candidates/applicants at this time. This decision was not made lightly, as we recognize 
the effort and enthusiasm you put into your application.

Please understand that our decision is in no way a reflection of your qualifications or potential. 
We received a number of outstanding applications, and the selection process was challenging.

We encourage you to continue pursuing your goals and aspirations. Your ''' + str(action) + '''are 
noteworthy, and we believe you have much to offer. Keep honing your strengths and seeking opportunities 
that align with your passion.

Thank you once again for considering''' + str(job) + '''. We wish you all the best 
in your future endeavors.

Take care and stay encouraged.
Warm regards,
{writer}'''
        else:
            body = f'Dear' + str(recipient) + ','
            body += f'''I trust this message finds you in good health. I wish to extend my sincere 
gratitude for your application for ''' + str(interest) + ''' at ''' + str(job) + '''.

After a thorough review and evaluation of all applications, it is with regret that I must inform you 
that we have chosen to proceed with other candidates who closely align with the specific requirements 
and qualifications we are seeking. The decision-making process was meticulous and challenging due to 
the exceptional pool of applicants.

Please be assured that our decision is based on the current needs and circumstances of our organization,
and it should not be interpreted as a reflection of your skills, qualifications, or potential. 
Your application demonstrated your ''' + str(action) + ''' which we genuinely appreciate.
I encourage you to maintain your pursuit of excellence and to explore other opportunities that resonate 
with your aspirations. Your background and capabilities are commendable, and I have no doubt that you will 
find success in your endeavors.

Once again, I extend my sincere thanks for considering ''' + str(interest) + ''' for your professional journey. 
We wish you continued success and fulfillment in all your future undertakings.

Should you have any questions or require further clarification, please do not hesitate to reach out.

Warm Regards,
{writer}'''

    elif tone.lower() == 'acceptance':
        job = input("Organization Name?")
        interest = input("what is the position of interest?")
        department = input('Department: ')
        action = input("what stood out about the person? ")
        tone2 = input('Formal or Informal? ')

        if tone2.lower() == 'formal':
            body = f"Dear " + str(recipient) + ","
            body += f'''I hope this email finds you well. It is with great pleasure that I convey our decision to accept your application for {interest} at {job}.

After a comprehensive review of all applications, your qualifications, experiences, and achievements stood out prominently.We were particularly impressed by your {action}.
Your application reflects a strong alignment with our values and goals, and we believe that your contributions will enrich our team and further our objectives. We are excited to welcome you to the {department} department.

Should you have any questions or need additional information, please do not hesitate to contact us.

Once again, congratulations on your successful application. We are enthusiastic about the opportunity to collaborate with you and look forward to the contributions you will bring to the {department} department.

Warm regards,
{writer}'''
        else:
            body = f"Hey " + str(recipient) + ","
            body += f'''Hope you're doing well! I'm thrilled to let you know that your application for {interest}
with us at {job} has been accepted!

Your background, skills, and enthusiasm truly impressed us. We're excited about the potential you bring to our team and 
how you'll contribute to {job}.

If you have any questions or need anything in the meantime, feel free to drop us a line.
Congratulations once again! We can't wait to have you on board and to see the awesome things we'll achieve together.

Best regards,
{writer}'''

    elif tone.lower() == 'create':
        url = 'mailto:' + receiver_email + '?subject=&body='
        webbrowser.open_new_tab(url)

email_writer()

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = sender_email
smtp_password = 'jmxgsqsujequnnfk'
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('"EMAIL SENT"')
