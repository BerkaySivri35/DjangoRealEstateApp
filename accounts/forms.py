from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.contrib import messages


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username =="admin":
            messages.add_message(self.request, messages.SUCCESS,"Hoşgeldin Admin.")
        
        if username != "admin":
            messages.add_message(self.request, messages.SUCCESS, f"Hoşgeldin, {username}")
            #2 kere yazıyor.!!!
        return username

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required = True

        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email = email).exists():
            self.add_error("email","Bu mail adresi ile daha önce kayıt olunmuş.")

        return email
    
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username = username).exists():
            self.add_error("username","Bu kullanıcı adı daha önce alınmış.")

        return username