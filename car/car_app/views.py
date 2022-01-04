from django.shortcuts import redirect, render
from .models import Consulting

def index(request):
    if request.method == 'POST':
        car_name = request.POST.get('car_name')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        if request.POST.get('privacy_agreement'):
            privacy_agreement = True
        consulting = Consulting(
            car_name = car_name,
            contact = contact,
            location = location,
            privacy_agreement = privacy_agreement
        )
        consulting.save()
        return redirect('/')
    else:
        consulting_list = Consulting.objects.order_by('-created_at')
        context = {
            'consulting_list' : consulting_list
        }
        return render(request, "index.html", context=context)

    