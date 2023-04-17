from django.shortcuts import redirect, render
from django.core.mail import send_mail
from random import randint
from django.conf import settings

from common.models import Customer, Seller

# Create your views here.

def c_signup(request):
    if request.method=='POST':
        f_name = request.POST['c_fname']
        l_name = request.POST['c_lname']
        e_mail = request.POST['c_email']
        m_number = request.POST['c_mnumber']
        add_ress = request.POST['c_address']
        pass_word = request.POST['c_pass']
        
# these are the fields to update the db details

        customer = Customer(
            first_name = f_name,
            last_name = l_name,
            email_id = e_mail,
            mobile_number = m_number,
            address = add_ress,
            password = pass_word,
        )

        customer.save()

    return render(request, 'common/c_signup.html')

def home(request):
    return render(request, 'common/homepage.html')

def c_login(request):
    msg=''
    if request.method == 'POST' :
        c_username = request.POST['c_username']
        c_password = request.POST['c_password']
        try:
            customer = Customer.objects.get(email_id = c_username,password = c_password)
            request.session['customer']= customer.id
            return redirect('customer:homepage')
        except:
            msg = 'invalid username or password'
    return render(request, 'common/c_login.html', {'message' : msg })

def s_login(request):
    return render(request, 'common/s_login.html')

def s_signup(request):
    msg=''
    if request.method =='POST':
        sname = request.POST['s_fname']
        companyname = request.POST['s_compname']
        accountnum = request.POST['s_bankacc']
        accountholder = request.POST['s_accname']
        ifsc = request.POST['s_ifsc']
        branch = request.POST['s_branch']
        semail = request.POST['s_email']
        s_mobnumber = request.POST['s_mnumber']
        saddress = request.POST['s_address']
        simage = request.FILES['s_image']
        spassword = randint(1111,9999)
        susername = 'sel-' + sname.lower()+str(spassword)

        seller = Seller(

            s_name = sname,
            s_account_number = accountnum,
            s_company_name = companyname,
            s_account_holder_name = accountholder, 
            s_ifsc_code = ifsc,
            s_branch_name = branch,
            s_email_id = semail,
            s_mobile_number = s_mobnumber,
            s_address = saddress,
            s_user_name = susername,
            s_password = spassword,
            s_image = simage,

        )

        seller.save()

        # msg = 'seller registerd successfully'

        # subject = 'login credentials'
        # message = 'Welcome Your Username is' + susername + ' and password is ' + str(spassword)
        # email_from = settings.EMAIL_HOST_USER 

        # send_mail(
        #     subject,
        #     message,
        #     email_from, 
        #     [semail],
        #     fail_silently=False
        # )
    
    return render(request, 'common/s_signup.html',{'message' : msg })

  