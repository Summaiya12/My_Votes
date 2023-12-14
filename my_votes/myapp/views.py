from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Category, CategoryItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='register')
def About(request):
    return render(request, 'about.html')


@login_required(login_url='register')
def Contact(request):
    return render(request, 'contact.html')


@login_required(login_url='register')
def Index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'index.html', context)


def Login(request):
    if request.method == 'POST':
        users = request.POST.get("name")
        password = request.POST.get("pass")
        user = authenticate(request, username=users, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password in correct')
    return render(request, 'login.html')


def Register(request):
    if request.method == "POST":
        name = request.POST.get("fullname")
        mail = request.POST.get("email")
        password = request.POST.get("pass")

        if User.objects.filter(email=mail).exists():
            messages.error(request, "Email Already Registered!!")
            return render(request, 'register.html')

        else:
            my_user = User.objects.create_user(name, mail, password)
            my_user.save()
            messages.success(request, 'User Created Successfully..!')
            return redirect('login')

    return render(request, 'register.html')


@login_required(login_url='register')
def Results(request, slug):
    category = Category.objects.get(slug=slug)
    items = CategoryItem.objects.filter(category=category)
    data = CategoryItem.objects.all()
    context = {"category": category, "items": items, "data": data}
    return render(request, "results.html", context)


@login_required(login_url='register')
def Vote(request, slug):
    category = Category.objects.get(slug=slug)
    categories = CategoryItem.objects.filter(category=category)
    msg = None

    if request.user.is_authenticated:
        if category.voters.filter(id=request.user.id).exists():
            msg = "voted"
    if request.method == "POST":
        selected_id = request.POST.get("category_item")
        item = CategoryItem.objects.get(id=selected_id)
        item.total_vote += 1
        item_category = item.category
        item_category.total_vote += 1
        item.voters.add(request.user)
        item_category.voters.add(request.user)
        item.save()
        item_category.save()
        return redirect("results", slug=category.slug)

    context = {'categories': categories, 'category': category, 'msg': msg}

    return render(request, 'vote.html', context)


@login_required(login_url='register')
def Logs(request):
    logout(request)
    return redirect('register')
