from Core.models import Center,Students


def set_students():
    centers = Center.objects.all()
    students = Students.objects.all()

    for center in centers:
        count = students.filter(Center=center).count()
        center.Students = count
        center.save()