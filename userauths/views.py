from django.shortcuts import render
from userauths.forms import UserRegistrationForm


def RegisterView(request):
    if request.method == 'POST':
        # se eu nao passar o request.POST ele nao vai capturar os valores do formulario
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegistrationForm()

    context = {
        # passamos o formulario aqui no context, isso faz com que gere o formulario de usuario renderizado na pagina
        "form": form,
    }
    return render(request, 'userauths/sign-up.html', context)
