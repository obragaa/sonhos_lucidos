from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Sonho
from .forms import SonhoForm
from .serializers import SonhoSerializer

# View para renderizar a página inicial e processar o formulário
def index(request):
    if request.method == "POST":
        form = SonhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SonhoForm()
    return render(request, 'core/index.html', {'form': form})

# ViewSet para fornecer uma API RESTful para o modelo Sonho
class SonhoViewSet(viewsets.ModelViewSet):
    queryset = Sonho.objects.all()
    serializer_class = SonhoSerializer
