from django.shortcuts import redirect, render
from datetime import date, timedelta, datetime
from car_app.models import Admin, Consulting

def loged_in(request):
    return True
    try: 
        id = request.session['admin']
        admin = Admin.objects.get(id=id)
        return True
    except:
        return False


def login(request):
    if request.method=="POST":
        name=request.POST.get('name')
        password =request.POST.get('password')
        try:
            admin = Admin.objects.get(name=name, password=password)
            request.session['admin'] = admin.id
            return redirect('/admin')
        except:
            return render(request, "login.html")        
    else:
        return render(request, "login.html")        


def logout(request):
    del(request.session['admin'])
    return redirect('/admin')


def consulting(request):
    if loged_in(request):
        consulting_list = Consulting.objects.all()
        return render(request, "consulting.html", {'consulting_list':consulting_list})
    else:
        return redirect('/admin/login')

def consulting_detail(request, id):
    if loged_in(request):
        consulting = Consulting.objects.get(id=id)
        return render(request, "consulting_detail.html", {'consulting':consulting})
    else:
        return redirect('/admin/login') 

def location_detail(request, id):
    if loged_in(request):
        location = Location.objects.get(id=id)
        lotto_list = Lotto.objects.all().order_by('-car_name')
        context = {
            'location':location,
            'lotto_list':lotto_list
        }
        return render(request, "create_location.html", context=context)
    else:
        return redirect('/admin/login')


def delete(request):
    if loged_in(request):
        table = request.POST.get('table')
        id = request.POST.get('id')
        if table == 'consulting':
            consulting = Consulting.objects.get(id=id)
            consulting.delete()
        return redirect("/admin")
    else:
        return redirect('/admin/login')


def create(request):
    if loged_in(request):
        if request.method == "POST":

            action = request.POST.get('action')
            id = request.POST.get('id')
            
            car_name = request.POST.get('car_name')
            contact = request.POST.get('contact')
            location = request.POST.get('location')
            status_consulting = request.POST.get('status_consulting')
            status_selling = request.POST.get('status_selling')
            
            if action == "create":
                consulting = Consulting(
                    car_name=car_name,
                    contact = contact,
                    location=location,
                    status_consulting=status_consulting,
                    status_selling = status_selling
                )
                location.save()

            if action == "update":
                consulting = Consulting.objects.get(id=id)
                consulting.car_name = car_name
                consulting.contact = contact
                consulting.location = location
                consulting.status_consulting = status_consulting
                consulting.status_selling = status_selling
                consulting.save()

            return redirect("/admin/consulting/{}".format(consulting.id))
        else:
            return render(request, "consulting_detail.html")
    else:
        return redirect('/admin/login')