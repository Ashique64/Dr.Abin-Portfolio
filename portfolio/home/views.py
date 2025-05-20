from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')




def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        form_subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message')


        subject = f"New Inquiry from {name}"


        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Subject: {form_subject}
        Message: {message}
        """


        html_message = f"""
        <html>
            <body>
                <h2>New Inquiry Details</h2>
                <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
                    <tr><th align="left">Name</th><td>{name}</td></tr>
                    <tr><th align="left">Email</th><td>{email}</td></tr>
                    <tr><th align="left">Phone</th><td>{phone}</td></tr>
                    <tr><th align="left">Subject</th><td>{form_subject}</td></tr>
                    <tr><th align="left">Message</th><td>{message}</td></tr>
                </table>
            </body>
        </html>
        """

        send_mail(
            subject,
            body,
            'hp@digitalroomz.com',
            ['hp@digitalroomz.com', 'ma@digitalroomz.com'],
            fail_silently=False,
            html_message=html_message
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    return render(request, 'index.html')