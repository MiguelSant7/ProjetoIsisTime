from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Ponto
from django.contrib import messages

# Função para exibir a página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('senha')
        
        if username == 'usuario' and password == 'senha123':
            return redirect('/home/')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
    return render(request, 'usuarios/login.html')

# Função para registrar ponto
def registrar_ponto(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        data_hora = data.get('dataHora')

        ponto = Ponto(data_hora=data_hora)
        ponto.save()

        return JsonResponse({'success': True, 'data_hora': data_hora})
    return JsonResponse({'success': False}, status=400)

# Função para exibir o histórico
def listagem_historico(request):
    pontos = Ponto.objects.all()
    return render(request, 'usuarios/historico.html', {'pontos': pontos})

# Função para a home page
def home(request):
    return render(request, 'usuarios/home.html')

# Função para editar ponto
from django.utils import timezone
from datetime import datetime

def editar_ponto(request, id):
    ponto = get_object_or_404(Ponto, id=id)
    
    if request.method == 'POST':
        try:
            nova_data_hora = request.POST.get('data_hora')
            # Converte a string para datetime
            ponto.data_hora = datetime.strptime(nova_data_hora, '%Y-%m-%dT%H:%M:%S')
            ponto.save()
            messages.success(request, 'Ponto atualizado com sucesso!')
            return redirect('historico')
        except Exception as e:
            messages.error(request, f'Erro ao atualizar ponto: {str(e)}')
            return redirect('editar_ponto', id=id)
    
    return render(request, 'usuarios/editar_ponto.html', {'ponto': ponto})


# Função para apagar ponto
def apagar_ponto(request, id):
    ponto = get_object_or_404(Ponto, id=id)
    ponto.delete()
    return redirect('historico')
