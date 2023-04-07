from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from u_auth.models import User
from Core.models import Lead,Students,Center,Coordinator,Lead_Updates,Section,Attandance
from Core.setup_functions import set_students
# Create your views here.

@login_required
def add_center(request):
    center = Center.objects.last()

    if center:
        refer = f'CENTER-00{center.id+1}'
    else:
        refer = 'CENTER-001'

    if request.method == 'POST':
        center = request.POST.get('center')
        new_center = Center(Reference=refer,Name=center)
        new_center.save()
        return redirect('list_center')

    context = {
        'refer' : refer,
    }
    return render(request,'add_center.html',context)

###########################################################################################################

@login_required
def list_center(request):
    set_students()
    centers = Center.objects.all().order_by('-id')
    context = {
        'centers':centers
    }
    return render(request,'list_center.html',context)

###########################################################################################################

@login_required
def add_coordinator(request):
    centers = Center.objects.all().order_by('-id')

    if request.method ==  'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        c1 = request.POST.get('center1')
        c2 = request.POST.get('center2')
        center1 = Center.objects.get(id=c1)
        center2 = Center.objects.get(id=c2)
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        place = request.POST.get('place')

        user = User.objects.create(first_name=f_name,last_name=l_name,email=email,
        username=username,is_coordinator=True)
        user.save()
        user.set_password(password)
        user.save()

        new_cordinator = Coordinator(User=user,Center1=center1,Center2=center2,Number1=number1,Number2=number2,Place=place)
        new_cordinator.save()

        return redirect('list_cordinator')
    
    context = {
        'centers':centers
    }

    return render(request,'add_cordinator.html',context)

###########################################################################################################

@login_required
def list_coordinators(request):
    coordinators = Coordinator.objects.all().order_by('-id')

    context = {
        'coordinators' : coordinators,
    }
    return render(request,'list_coordinators.html',context)

###########################################################################################################

@login_required
def add_lead(request):
    coordinators = Coordinator.objects.all().order_by('-id')
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
        coordinator = Coordinator.objects.get(id=c_id)
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
    leads = Lead.objects.all().order_by('-id')
    context = {
        'leads' : leads
    }
    return render(request,'list_leads.html',context)

###########################################################################################################

@login_required
def view_lead(request,id):
    lead = Lead.objects.get(id=id)
    updates = Lead_Updates.objects.filter(Lead=lead).order_by('-id')

    if request.method == 'POST':
        update = request.POST.get('update')
        new_update = Lead_Updates(Lead=lead,Description=update)
        new_update.save()
        return redirect('.')

    context = {
        'lead' : lead,
        'updates' : updates,
    }
    return render(request,'view_lead.html',context)

###########################################################################################################

@login_required
def accept(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.Status = 'accepted'
    lead.save()
    return redirect('add_student')

@login_required
def reject(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.Status = 'rejected'
    lead.save()
    return redirect('list_leads')

###########################################################################################################

@login_required
def add_student(request):
    student = Students.objects.last()
    centers = Center.objects.all().order_by('-id')

    if student:
        refer = f'STUDENT-00{student.id+1}'
    else:
        refer = 'STUDENT-001'

    if request.method == 'POST':
        c = request.POST.get('center')
        center = Center.objects.get(id=c)
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
                               Study_Standard=standard,Study_Devision=division,Center=center)
        new_student.save()
        return redirect('.')

    context = {
        'refer' : refer,
        'centers' : centers
    }
    return render(request,'add_student.html',context)

###########################################################################################################

@login_required
def list_students(request):
    students = Students.objects.all().order_by('-id')
    context = {
        'students' : students
    }
    return render(request,'list_students.html',context)

###########################################################################################################

@login_required
def center_attandance(request):
    set_students()
    centers = Center.objects.all().order_by('-id')
    context = {
        'centers' : centers
    }
    return render(request,'attandance_center.html',context)

###########################################################################################################

@login_required
def sections(request,cid):
    center = Center.objects.get(id=cid)
    sections = Section.objects.filter(Center=center).order_by('-id')
    section = Section.objects.last()

    if section:
        refer = f'SECTION-00{section.id+1}'
    else:
        refer = 'SECTION-001'

    if request.method == 'POST':
        from_time = request.POST.get('from')
        to_time = request.POST.get('to')

        new_section = Section(Reference=refer,Center=center,From_Time=from_time,To_Time=to_time)
        new_section.save()
        return redirect('.')

    context = {
        'sections' : sections,
    }
    return render(request,'classes.html',context)

###########################################################################################################

@login_required
def attandance(request,sid):
    section = Section.objects.get(id=sid)
    students = Students.objects.filter(Center=section.Center)

    if request.method == 'POST':
        attandance = request.POST.getlist('checks[]')
        
        for student in students:
            print (f'student id : {student.id}, attandence : {attandance}')
            if str(student.id) in attandance:
                data = Attandance(Section=section,Student=student,Attandance='Precent')
                data.save()
            else:
                data = Attandance(Section=section,Student=student,Attandance='Absent')
                data.save()

        section.Ended = True
        section.save()

        return redirect('.')

    context = {
        'students' : students
    }
    return render(request,'attandance.html',context)

###########################################################################################################

@login_required
def view_attandance(request,sid):
    section = Section.objects.get(id=sid)
    attandance = Attandance.objects.filter(Section=section)
    context = {
        'attandances' : attandance,
        'section' : section,
    }
    return render(request,'view_attandance.html',context)

###########################################################################################################