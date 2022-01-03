from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from .forms import *
def index(request):
    context = {"order": Qrcode.objects.all(),}
    return render(request, 'dashboard.html', context)


def insert(request):
    return render(request, 'index.html', {'form': CustomerForm()})

def CreateUser(request):
    tableno = request.POST.get('tableno')
    cust = Customer.objects.create(tableno= tableno)
    if cust:
        request.session['customer_id']=cust.id
        return redirect('/menu')


def menu(request):
    if 'customer_id' in request.session:
        context = {"category": Category.objects.all(),
                   'custom': Customer.objects.get(id =request.session['customer_id'])}
        return render(request, "menu.html", context)
    return redirect('/')

def AddToFood(request,id):
    customer = Customer.objects.get(id = request.session['customer_id'])
    quantity = request.POST['quantity']
    food = Meal.objects.get(id=id)
    succssess = Food_Pick.objects.create(quantity= quantity,customer=customer,meal=food)
    return redirect('/menu')


def food(request):
    context = { 'custom': Customer.objects.get(id =request.session['customer_id']) }
    return render(request,'food.html',context)


def food2(request):
    context = { 'custom': Customer.objects.get(id =request.session['customer_id']),
                'date': Order.objects.get(customer = request.session['customer_id'])}
    return render(request,'food2.html',context)


def makeorder(request):
    customer = Customer.objects.get(id = request.session['customer_id'])
    total = 0
    for sum in customer.my_food.all():
        total += sum.meal.price * sum.quantity
    ord = Order.objects.create(customer=customer, table_number=customer.tableno, total=total)
    for meals in customer.my_food.all():
        ord.foodlist.add(meals.meal)
    ord.save()



    return redirect('/yourorder')


# def order(request):
#     context = {"order": Customer.objects.all()}
#     return render(request, "orders.html", context)
class order(ListView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders.html'
    def get_queryset(self):
        query = self.request.GET.get('created_at')
        if query:
            order = self.model.objects.filter(created_at=query)
        else:
            order = self.model.objects.all()
        return order


def kitchen(request):
    context = {"order": Customer.objects.all(),}
    return render(request, "kitchen.html", context)


def add_order(request):
    table_number = request.POST["table_number"]
    quantity = request.POST["quantity"]
    number_of_invoice = request.POST["number_of_invoice"]
    order = Order.objects.create(table_number=table_number, quantity=quantity, number_of_invoice=number_of_invoice)
    return redirect('/')


def orderdetails(request, id):
    context = {
        'order': Order.objects.get(id=id)
    }
    return render(request, 'orders.html', context)


def orderdetail(request,id):
    to = Customer.objects.get(id = id)
    price = Order.objects.get(customer = to)
    context = {"custom": Customer.objects.get(id=id) ,
               'price' :price.total}
    return render(request, "orderdetails.html", context)


def kitchendetail(request,id):
    to = Customer.objects.get(id = id)
    price = Order.objects.get(customer = to)
    context = {"custom": Customer.objects.get(id=id) ,
               'price' :price}
    return render(request, "kitchendetail.html", context)


class Login(LoginView):
    template_name = 'login_page.html'


class Logout(LogoutView):
    success_url = 'home'

class orders(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orderslist.html'


class orderdetails(UpdateView):
    model = Order
    context_object_name = 'order'
    template_name = 'kitchen.html'


class invoice(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'invoice.html'

def choose(request):
    return render(request, 'choose.html')

def preparing(request, id, coid):
    ord = Order.objects.get(id = id)
    cust = Customer.objects.get(id=coid)
    ord.order_status = OrderStatus.PREPARING
    cust.table_status = OrderStatus.PREPARING
    ord.save()
    cust.save()
    return redirect('/kitchen')


def done(request, id, coid):
    ord = Order.objects.get(id = id)
    cust = Customer.objects.get(id=coid)
    ord.order_status = OrderStatus.WAITING
    cust.table_status = OrderStatus.WAITING
    ord.save()
    cust.save()
    return redirect('/kitchen')


def deliver(request, id, coid):
    ord = Order.objects.get(id = id)
    cust = Customer.objects.get(id=coid)
    ord.order_status = OrderStatus.DONE
    cust.table_status = OrderStatus.DONE
    ord.save()
    cust.save()
    return redirect('/kitchen')