from django.shortcuts import render, redirect
from .forms import TaskList, Delivery, Payment, Amount

# Create your views here.

def home(request):
    context = {'form': TaskList , "Del" : Delivery , "Pay" : Payment, "Amo":Amount}
    return render (request, 'ht.html',context)


# def dataPost(request):
#     form=TaskList(request.POST)
#     if form.is_valid():
#         name= form.cleaned_data['name']
#         email=form.cleaned_data['email']
#         phone=form.cleaned_data['phone']
#         form.save()
#     else:
#         form=TaskList
#     return redirect("/")
    
def dataPost(request):
    if request.method == 'POST':
        form = TaskList(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            form.save()
            
        else:
            form = TaskList()

        form = Delivery(request.POST)
        if form.is_valid():
            local_drop_off = form.cleaned_data["local_drop_off"]
            local_pick_up = form.cleaned_data["local_pick_up"]
            shopping = form.cleaned_data["shopping"]
            ship_N = form.cleaned_data["ship_N"]
            ship_date = form.cleaned_data["ship_date"]
            form.save()

        else:
            form = Delivery()

        form = Payment(request.POST)
        if form.is_valid():
            cash = form.cleaned_data["cash"]
            card = form.cleaned_data["card"]
            checks = form.cleaned_data["checks"]
            paypal = form.cleaned_data["paypal"]
            other = form.cleaned_data["other"]
            form.save()
        else:
            form = Payment()

        form = Amount(request.POST)
        if form.is_valid():
            Subtotal = form.cleaned_data["Subtotal"]
            Taxes = form.cleaned_data["Taxes"]
            Shipping = form.cleaned_data["Shipping"]
            Total = form.cleaned_data["Total"]
            form.save()   
        return redirect("/")
    return redirect("/")



