from django.shortcuts import redirect, render
from .models import Buy, Installment, Sell

def index(request):
    if request.method == 'POST':
        table = request.POST.get('table')
        car_name = request.POST.get('car_name')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        if request.POST.get('privacy_agreement'):
            privacy_agreement = True

        if table == 'sell':
            consulting = Sell(
                car_name = car_name,
                contact = contact,
                location = location,
                privacy_agreement = privacy_agreement
            )
            consulting.save()

        elif table == 'buy':
            buy = Buy(
                car_name = car_name,
                contact = contact,
                location = location,
                privacy_agreement = privacy_agreement
            )
            buy.save()

        elif table == 'installment':
            installment = Installment(
                car_name = car_name,
                contact = contact,
                location = location,
                privacy_agreement = privacy_agreement
            )
            installment.save()

        return redirect('/')
    else:
        consulting_list = Sell.objects.order_by('?')
        context = {
            'consulting_list' : consulting_list
        }
        return render(request, "index.html", context=context)

    