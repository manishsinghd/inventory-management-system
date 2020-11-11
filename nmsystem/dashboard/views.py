from django.shortcuts import render, redirect, get_object_or_404
from .forms import Categorietypeform, Productform, Creatuserform, Customerform
from .models import Categorietype, Product, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    form = Creatuserform(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account is created for {username}')
        Customer.objects.create(user=user)
        return redirect('/login')
    context = {'form': form}
    return render(request, "register.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or password is incorrect')

    return render(request, "login.html", )


def logout_view(request):
    logout(request)
    return redirect("/login")


@login_required(login_url='login')
def home_view(request, *args, **kwargs):
    # queryset2 = request.user.customer
    # print('object_list2:', queryset2)

    # context = {

    # "object_list2": queryset2,
    # }

    return render(request, "home.html")


@login_required(login_url='login')
def categories_view(request):
    # queryset = Categorietype.objects.all()
    queryset = request.user.categorietype_set.all()

    context = {

        "object_list": queryset,
    }

    return render(request, "categories.html", context, )


@login_required(login_url='login')
def editcategories_view(request):
    form = Categorietypeform(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/categories')
    context = {
        'form': form,
    }

    return render(request, "ppp.html", context)


@login_required(login_url='login')
def updatecategories_view(request, pk):
    ins = Categorietype.objects.get(id=pk)
    form = Categorietypeform(instance=ins)
    if request.method == "POST":
        form = Categorietypeform(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            return redirect('/categories')
    context = {
        'form': form,
    }

    return render(request, "ppp.html", context)


@login_required(login_url='login')
def deletecategories_view(request, pk):
    ins = Categorietype.objects.get(id=pk)

    if ins.delete():
        return redirect('/categories')

    return render(request, "categories.html")


@login_required(login_url='login')
def poroducts_view(request, *args, **kwargs):
    queryset2 = request.user.product_set.all()
    print('object_list2:', queryset2)

    context = {

        "object_list2": queryset2,
    }
    return render(request, "products.html", context)


@login_required(login_url='login')
def accountsettings_view(request, *args, **kwargs):
    customer = request.user.customer
    form = Customerform(instance=customer)
    if request.method == 'POST':
        form = Customerform(request.POST, request.FILES, instance=customer)
        form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, "account_settings.html", context)


@login_required(login_url='login')
def editproduct_view(request):
    form2 = Productform(request.POST or None)
    if form2.is_valid():
        instance = form2.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/products')
    context = {
        'form2': form2,
    }

    return render(request, "2ppp.html", context)


@login_required(login_url='login')
def updateproduct_view(request, pk):
    ins1 = Product.objects.get(id=pk)
    form2 = Productform(instance=ins1)
    if request.method == "POST":
        form2 = Productform(request.POST, instance=ins1)
        if form2.is_valid():
            form2.save()
            return redirect('/products')
    context = {
        'form2': form2,
    }
    return render(request, "2ppp.html", context)


@login_required(login_url='login')
def deleteproducts_view(request, pk):
    ins1 = Product.objects.get(id=pk)

    if ins1.delete():
        return redirect('/products')

    return render(request, "add.html")


@login_required(login_url='login')
def bundle_view(request, pk):
    cus1 = Categorietype.objects.get(id=pk)
    queryset1 = cus1.product_set.all()

    context = {

        "object_list1": queryset1,
    }

    return render(request, "add.html", context, )
