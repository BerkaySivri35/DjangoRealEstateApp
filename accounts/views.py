from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.forms import NewUserForm, LoginUserForm,AuthenticationForm
from django.contrib.auth import logout, authenticate, login,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from contacts.models import Contact

# Create your views here.
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request, data = request.POST)

#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')

#             #Match with user
#             user = authenticate(request, username = username, password = password)

#             #user is available?
#             if user is not None:
#                 login(request,user)
#                 messages.add_message(request, messages.SUCCESS, 'Giriş Başarılı')
            
#             else:
#                 return render(request,"accounts/login.html", {"form":form})
#         else:
#             return render(request,"accounts/login.html", {"form":form})
#     else:   
#             form = LoginUserForm()
#             return render(request,"accounts/login.html", {"form":form})


#     return render(request, 'accounts/login.html')
def user_login(request):
    if request.user.is_authenticated and "next" in request.GET:
        return render(request, "accounts/login.html", messages.add_message(request, messages.ERROR, "Yetkiniz YOK!"))

    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            #user ile eşleştirme
            user = authenticate(request, username = username, password = password)
            
            #user bilgisi varsa
            if user is not None:
                login(request,user)
                messages.add_message(request, messages.SUCCESS, "Giriş Başarılı.")
                nextUrl = request.GET.get("next", None)
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                return render(request, "accounts/login.html", {"form":form})
        else:
            return render(request, "accounts/login.html", {"form":form})
    else:
        form = LoginUserForm()
        return render (request, "accounts/login.html",{"form":form})
    
def user_register(request):
    if request.method == 'POST':
        #GET FORM VALUES
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            
            user = authenticate(request, username = username, password = password)

            login(request, user)
            messages.info(request,"Hesap başarıyla oluşturuldu.")
            return redirect("index")
        else:
            return render(request,"accounts/register.html", {"form":form})
    else:
        form = NewUserForm()
        return render(request, "accounts/register.html", {"form":form})
    

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Çıkış Başarılı.")
    return redirect("index")

@login_required
def user_dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context ={
        'user_contacts':user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)