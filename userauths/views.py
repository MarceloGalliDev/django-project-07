from django.shortcuts import redirect, render
from userauths.forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def RegisterView(request):
    if request.method == 'POST':
        # se eu nao passar o request.POST ele nao vai capturar os valores do formulario
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            new_user = form.save()
            username = form.cleaned_data.get('username')
            # username = request.POST.get('username') isso aqui é a mesma coisa que a linha acima
            messages.success(request, f"Hey {username} was account is successfully!")
            new_user = authenticate(
                username=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password1')
            )
            login(request, new_user)
            return redirect('core:index')
        
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in!")
        return redirect('core:login')
    else:
        form = UserRegistrationForm()

    context = {
        # passamos o formulario aqui no context, isso faz com que gere o formulario de usuario renderizado na pagina
        "form": form,
    }
    return render(request, 'userauths/sign-up.html', context)
