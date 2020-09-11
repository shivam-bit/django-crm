from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.forms import inlineformset_factory 
from .forms import OrderForm

# Create your views here.
def home(request):
    # return HttpResponse('home')
    orders=order.objects.all()
    customers=Customer.objects.all()
    total_customers=customers.count()
    total_order=orders.count()
    total_order_delivered=orders.filter(status='delivered').count() 
    total_order_pending=orders.filter(status='pending').count()
    context={'orders':orders,'customers':customers,'total_customers':total_customers,'total_order':total_order,'total_order_delivered':total_order_delivered,'total_order_pending':total_order_pending}
    return render(request,'accounts/dashboard.html',context)
def products(request):
    all_tems=Products.objects.all()
    return render(request,'accounts/products.html',{'product_list':all_tems})
def customer(request,pk):
    customer_object=Customer.objects.get(id=pk)
    total_orders=customer_object.order_set.all()
    orders_count=total_orders.count()
    # return HttpResponse(total_orders.product)
    context={'customer':customer_object,'total_orders':total_orders,'orders_count':orders_count}
    return render(request,'accounts/customer.html',context)
def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,order,fields=('product','status'))
    customer_object=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=order.objects.none(),instance=customer_object )
    # form=OrderForm(initial={'customer':customer_object})
    if request.method=='POST':
        # print('printing POST:',request.POST)
        # form=OrderForm(request.POST)
        formset=OrderFormSet(request.POST,instance=customer_object)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request,'accounts/order_form.html',context)
def updateOrder(request,pk):
    order_details=order.objects.get(id=pk)
    form=OrderForm(instance=order_details)
    if request.method=='POST':
        # print('printing POST:',request.POST)
        form=OrderForm(request.POST,instance=order_details)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form }
    return render(request,'accounts/order_form.html',context)
def deleteOrder(request,pk):
    order_to_delete=order.objects.get(id=pk)
    if request.method=='POST':
        order_to_delete.delete()
        return redirect('/')
    context={'item':order_to_delete}
    return render(request,'accounts/delete.html',context)