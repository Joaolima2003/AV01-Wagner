from django.shortcuts import render
from django.http import HttpResponse

funcionarios = [
        {'id':1,'nome': 'João Silva', 'cpf': '12345678901', 'email': 'joao.silva@example.com', 'salario': 'R$ 3000,00', 'cargo': 'Analista'},
        {'id':2, 'nome': 'Maria Oliveira', 'cpf': '10987654321', 'email': 'maria.oliveira@example.com', 'salario': 'R$ 3500,00', 'cargo': 'Desenvolvedora'},
        {'id':3, 'nome': 'Pedro Santos', 'cpf': '32165498700', 'email': 'pedro.santos@example.com', 'salario': 'R$ 4000,00', 'cargo': 'Gerente'},
        {'id':4,'nome': 'Pedro Santos', 'cpf': '32165498700', 'email': 'pedro.santos@example.com', 'salario': 'R$ 4000,00', 'cargo': 'Gerente'},
        {'id':5,'nome': 'João Silva', 'cpf': '12345678901', 'email': 'joao.silva@example.com', 'salario': 'R$ 3000,00', 'cargo': 'Analista'},
        {'id':6,'nome': 'Maria Oliveira', 'cpf': '10987654321', 'email': 'maria.oliveira@example.com', 'salario': 'R$ 3500,00', 'cargo': 'Desenvolvedora'},
        {'id':7,'nome': 'Pedro Santos', 'cpf': '32165498700', 'email': 'pedro.santos@example.com', 'salario': 'R$ 4000,00', 'cargo': 'Gerente'},
        {'id':8,'nome': 'Pedro Santos', 'cpf': '32165498700', 'email': 'pedro.santos@example.com', 'salario': 'R$ 4000,00', 'cargo': 'Gerente'},

    ]


def listar_cadastros(request):
    return render(request, 'listar_cadastros.html', {'funcionarios':funcionarios})
    



def detalhar_cadastros(request, id):
    for funcionario in funcionarios:
        if funcionario['id'] == id:

            return render(request, 'detalhes_cadastros.html', {'funcionario': funcionario})

    return HttpResponse('Funcionário não encontrado')    

