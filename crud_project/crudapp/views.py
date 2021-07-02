from django.contrib.auth import logout, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CardForm, createuserform
from .models import dbb
from django.contrib.auth.decorators import login_required


# Create your views here.

# def home(request):
#     cards = dbb.objects.all()
#     return render(request, 'index.html', { 'cards': cards })
# @login_required
def home(request):
    cards = reversed(dbb.objects.all())
    return render(request, 'index.html', {'cards': cards})



# def home(request):
#     cards = dbb.objects.order_by('description')
#     return render(request, 'index.html', { 'cards': cards })


def view(request):
    cards = dbb.objects.all()
    return render(request, 'showbooks.html', {'cards': cards})


def create(request):
    form = CardForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('index')
    context = {
        "form": form
    }
    return render(request, 'forms.html', context)


def update(request, id=None):
    instance = get_object_or_404(dbb, id=id)
    form = CardForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('index')
    context = {
        "form": form,
    }
    return render(request, 'forms.html', context)


def delete(request, id=None):
    instance = get_object_or_404(dbb, id=id)
    instance.delete()
    return redirect('index')


def userreg(request):
    form = createuserform()
    # cust_form = createcustomerform()
    if request.method == 'POST':
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            # cust_form = createcustomerform(request.POST)
            # if form.is_valid() and cust_form.is_valid():
            #     user = form.save()
            # customer = cust_form.save(commit=False)
            # customer.user = user
            # customer.save()
            return redirect('login')
    context = {
        'form': form,
        # 'cust_form': cust_form,
    }
    return render(request, 'userreg.html', context)


def login(request):
    if request.user.is_authenticated:
        print("Hello world")
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    return redirect('index')
            # if user == 'admin':
            #     return redirect('index')
            # else:
            #     # login(request)
            #     return redirect('index')

        # context = {}
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')

# def start(request):
#     form=UserRegFrom
#     context={}
#     context["form"]=form
#     if request.method=='POST':
#
#         form=UserRegFrom(request.POST)
#         if form.is_valid():
#             print(form)
#             form.save()
#             return HttpResponseRedirect('login')
#         else:
#             form=UserRegFrom(request.POST)
#             context["form"]=form
#             return HttpResponse("sorry")
#             return HttpResponseRedirect('start')
#
#     return render(request,'userregistration.html',context)

# def login(request):
#     context={}
#     form=Loginform
#     context={'form':form}
#     if request.method=='POST':
#         form=Loginform(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get("username")
#             password=form.cleaned_data.get("password")
#             user=authenticate(username=username,password=password)
#             if user:
#                 if username=='admin':
#                     return redirect('index')
#                 else:
#                     return HttpResponse("user")
#                 # messages.info(request, 'Login Successfull!')
#                 # login(request, user)
#             else:
#                 form=Loginform()
#     return render(request,'loginpage.html',context)
