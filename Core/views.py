from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from u_auth.models import User
from Core.models import Lead,Students
# Create your views here.

@login_required
def add_coordinator(request):
    if request.method ==  'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        center1 = request.POST.get('center1')
        center2 = request.POST.get('center2')
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        email = request.POST.get('email')
        place = request.POST.get('place')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create(first_name=f_name,last_name=l_name,Center1=center1,Center2=center2,email=email,
        Mobile=number1,Mobile2=number2,Address=place,username=username,is_coordinator=True)
        user.save()
        user.set_password(password)
        user.save()
        return redirect('list_cordinator')
    return render(request,'add_cordinator.html')

###########################################################################################################

@login_required
def list_coordinators(request):
    coordinators = User.objects.filter(is_coordinator=True)

    context = {
        'coordinators' : coordinators,
    }
    return render(request,'list_coordinators.html',context)

###########################################################################################################

@login_required
def add_lead(request):
    coordinators = User.objects.filter(is_coordinator=True)
    lead = Lead.objects.last()
    
    if lead:
        refer = f'LEAD-00{lead.id+1}'
    else:
        refer = 'LEAD-001'

    if request.method == 'POST':
        student = request.POST.get('name')
        gardian = request.POST.get('gardian')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        c_id = request.POST.get('coordinator')
        coordinator = User.objects.get(id=c_id)
        mode = request.POST.get('mode')
        mode_text = request.POST.get('mode_text')

        new_lead = Lead(Reference=refer,Student_Name=student,Gardian_Name=gardian,Contact_Number=contact,
                        Location=location,Lead_Mode=mode,Lead_Mode_Text=mode_text,Coordinator=coordinator)
        new_lead.save()
        return redirect('list_leads')

    context = {
        'coordinators' : coordinators,
        'refer' : refer
    }
    return render(request,'add_lead.html',context)

###########################################################################################################

@login_required
def list_leads(request):
    leads = Lead.objects.all()
    context = {
        'leads' : leads
    }
    return render(request,'list_leads.html',context)

###########################################################################################################

@login_required
def view_lead(request,id):
    lead = Lead.objects.get(id=id)
    context = {
        'lead' : lead
    }
    return render(request,'view_lead.html',context)

###########################################################################################################

@login_required
def add_student(request):
    student = Students.objects.last()
    if student:
        refer = f'STUDENT-00{student.id+1}'
    else:
        refer = 'STUDENT-001'

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        guardian_name = request.POST.get('guardian_name')
        guardian_mobile = request.POST.get('guardian_mobile')
        attached_proof = request.POST.get('attached_proof')
        date_of_birth = request.POST.get('date_of_birth')
        age_group = request.POST.get('age_group')
        preferd_location = request.POST.get('preferd_location')
        mode_of_travel = request.POST.get('mode_of_travel')
        playing_position = request.POST.get('playing_position')
        school_name = request.POST.get('school_name')
        school_address = request.POST.get('school_address')
        standard = request.POST.get('standard')
        division = request.POST.get('division')

        new_student = Students(Reference=refer,Full_Name=full_name,Street_Address=street_address,
                               City=city,State=state,Zip_Code=zipcode,Phone=phone,Email=email,
                               Guardian_Name=guardian_name,Guardian_Mobile=guardian_mobile,
                               ID_Proof=attached_proof,Date_Of_Birth=date_of_birth,Age_Group=age_group,
                               Preferred_Location=preferd_location,Travel_Mode=mode_of_travel,
                               Playing_Position=playing_position,School_Name=school_name,School_Address=school_address,
                               Study_Standard=standard,Study_Devision=division)
        new_student.save()
        return redirect('.')

    context = {
        'refer' : refer
    }
    return render(request,'add_student.html',context)

###########################################################################################################

@login_required
def list_students(request):
    students = Students.objects.all()
    context = {
        'students' : students
    }
    return render(request,'list_students.html',context)

###########################################################################################################

@login_required
def add_center(request):
    return render(request,'add_center.html')

###########################################################################################################

@login_required
def list_center(request):
    return render(request,'list_center.html')