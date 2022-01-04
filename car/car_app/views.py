from django.shortcuts import redirect, render
from .models import Consulting

def index(request):
    print (request.method)
    if request.method == 'POST':
        print("asdkfjsdaklfjl")
        print(request.POST)
        car_name = request.POST.get('car_name')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        if request.POST.get('privacy_agreement'):
            privacy_agreement = True
        print(privacy_agreement)
        consulting = Consulting(
            car_name = car_name,
            contact = contact,
            location = location
        )
        consulting.save()
        return redirect('/')
    else:
        consulting_list = Consulting.objects.order_by('-created_at')
        print(consulting_list)
        context = {
            'consulting_list' : consulting_list
        }
        return render(request, "index.html", context=context)

    