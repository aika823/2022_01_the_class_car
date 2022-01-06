from django.shortcuts import redirect, render
from datetime import date, timedelta, datetime
from car_app.models import Admin, Buy, Installment, Sell

def loged_in(request):
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


def sell(request):
    if loged_in(request):
        sell_list = Sell.objects.all()
        return render(request, "sell.html", {'sell_list':sell_list})
    else:
        return redirect('/admin/login')

def buy(request):
    if loged_in(request):
        buy_list = Buy.objects.all()
        return render(request, "buy.html", {'buy_list':buy_list})
    else:
        return redirect('/admin/login')

def installment(request):
    if loged_in(request):
        installment_list = Installment.objects.all()
        return render(request, "installment.html", {'installment_list':installment_list})
    else:
        return redirect('/admin/login')

def sell_detail(request, id):
    if loged_in(request):
        sell = Sell.objects.get(id=id)
        return render(request, "sell_detail.html", {'sell':sell})
    else:
        return redirect('/admin/login') 

def buy_detail(request, id):
    if loged_in(request):
        buy = Buy.objects.get(id=id)
        return render(request, "buy_detail.html", {'buy':buy})
    else:
        return redirect('/admin/login') 

def installment_detail(request, id):
    if loged_in(request):
        installment = Installment.objects.get(id=id)
        return render(request, "installment_detail.html", {'installment':installment})
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
        
        if table == 'sell':
            consulting = Sell.objects.get(id=id)
            consulting.delete()
        elif table == 'buy':
            consulting = Buy.objects.get(id=id)
            consulting.delete()
        elif table == 'installment':
            consulting = Installment.objects.get(id=id)
            consulting.delete()

        return redirect("/admin")
    else:
        return redirect('/admin/login')


def create(request):
    if loged_in(request):
        if request.method == "POST":

            action = request.POST.get('action')
            table = request.POST.get('table')
            id = request.POST.get('id')
            
            car_name = request.POST.get('car_name')
            contact = request.POST.get('contact')
            location = request.POST.get('location')
            status_consulting = request.POST.get('status_consulting')
            status_selling = request.POST.get('status_selling')
            
            if action == "create":
                consulting = Sell(
                    car_name=car_name,
                    contact = contact,
                    location=location,
                    status_consulting=status_consulting,
                    status_selling = status_selling
                )
                location.save()

            if action == "update":
                print(table)
                if table == "sell":
                    consulting = Sell.objects.get(id=id)
                elif table == "buy":
                    consulting = Buy.objects.get(id=id)
                elif table == "installment":
                    consulting = Installment.objects.get(id=id)
                else:
                    consulting = None
                print(consulting)
                consulting.car_name = car_name
                consulting.contact = contact
                consulting.location = location
                consulting.status_consulting = status_consulting
                consulting.status_selling = status_selling
                consulting.save()

            return redirect("/admin/{}/{}".format(table, consulting.id))
        else:
            return render(request, "consulting_detail.html")
    else:
        return redirect('/admin/login')