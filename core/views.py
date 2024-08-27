from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Sonho
from .forms import SonhoForm
from .serializers import SonhoSerializer
from django.shortcuts import get_object_or_404

# View para renderizar a página inicial e processar o formulário
def index(request):
    if request.method == "POST":
        form = SonhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SonhoForm()
    
    # Buscar todos os sonhos no banco de dados
    sonhos = Sonho.objects.all()
    
    return render(request, 'core/index.html', {'form': form, 'sonhos': sonhos})


# ViewSet para fornecer uma API RESTful para o modelo Sonho
class SonhoViewSet(viewsets.ModelViewSet):
    queryset = Sonho.objects.all()
    serializer_class = SonhoSerializer


def editar_sonho(request, pk):
    sonho = get_object_or_404(Sonho, pk=pk)
    if request.method == "POST":
        form = SonhoForm(request.POST, instance=sonho)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SonhoForm(instance=sonho)
    return render(request, 'core/editar_sonho.html', {'form': form})


def excluir_sonho(request, pk):
    sonho = get_object_or_404(Sonho, pk=pk)
    if request.method == "POST":
        sonho.delete()
        return redirect('index')
    return render(request, 'core/excluir_sonho.html', {'sonho': sonho})
