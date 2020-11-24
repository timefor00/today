from django.shortcuts import render
from .forms import RegisterForm


def register(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html',{'form':user_form})


def userinfo(request):
    conn_user = request.user
    context = {
        'username' : conn_user.username,
        'first_name' : conn_user.first_name,
        'last_name' : conn_user.last_name,
        'email' : conn_user.email,
    }

    return render(request, 'registration/mypage.html', context=context)