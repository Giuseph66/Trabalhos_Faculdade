from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import os
from .models import *
import matplotlib.pyplot as plt
import numpy as np

def home(request):
    return render(request,'usuarios/login.html')

def usuarios(request):
    global Nome_usu
    if request.method == 'POST':
        gmail = request.POST.get('email')
        senha = request.POST.get('senha')
    
        if Usuario.objects.filter(gmail=gmail,senha=senha).exists():
            obg=Usuario.objects.get(gmail=gmail)
            Nome_usu= obg.nome
            questions = Base_questoes.objects.order_by('Pergunta')
            return render(request, 'usuarios/tela1.html', {'nome': Nome_usu, 'questions': questions})
        else:
            return render(request, 'usuarios/mensagem.html', {'messagem': 'Usuario nao cadastrado'})
def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ida = 0
        gmail = request.POST.get('email')
        senha = request.POST.get('senha')
        if Usuario.objects.filter(nome=nome).exists() or Usuario.objects.filter(gmail=gmail).exists():
            return render(request, 'usuarios/mensagem.html', {'messagem': f'Usuario ja existe!'})
        else:
            novo_usuario = Usuario(nome=nome, idade=ida, gmail=gmail, senha=senha)
            novo_usuario.save()
            return render(request,'usuarios/login.html')
def exibir(request):
    usuarios={
        'usuarios':Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuarios)
def cadastro(request):
    return render(request,'usuarios/cadastro.html')
def results(request, question_id):
    global Nome_usu,pergunta
    selected_option = Sub_questoes.objects.filter(id=question_id)
    for op in pergunta:
        if Quem_voto.objects.filter(Nome=Nome_usu,voto=op).exists():
            return render(request, 'usuarios/mensagem.html', {'messagem': f'{Nome_usu} já votou em "{op}"'})
        else:
            for option in selected_option:
                option.voto += 1
                option.save()
            voto_usu = Quem_voto(Nome=Nome_usu,voto=op)
            voto_usu.save()
            perguntas = Base_questoes.objects.order_by('id')
            ids=[]
            for pergunta in perguntas:
                opcoes=[]
                votus=[]
                tudo = Sub_questoes.objects.filter(questao_id=pergunta)
                for dnv in tudo:
                    opcoes.append(dnv.ops)
                    votus.append(dnv.voto)
                print(opcoes)
                if opcoes:
                    ids.append(f"img/grafico_{pergunta.id}.png")
                    plt.bar(opcoes, votus)
                    plt.xlabel('Perguntas')
                    plt.ylabel('votos')
                    plt.title(pergunta)
                    plt.xticks(rotation=45, ha='right')

                    save_path = os.path.join('app_cad_usuarios/static/img', f'grafico_{pergunta.id}.png')
                    plt.tight_layout() 
                    plt.savefig(save_path)
                    plt.close()

            return render(request, 'usuarios/results.html',{'n':ids})

def vote(request, question_id):
    global Nome_usu,pergunta
    pergunta=Base_questoes.objects.filter(id=question_id)
    selected_option = Sub_questoes.objects.filter(questao_id=question_id)
    return render(request, 'usuarios/vote.html', {'nome': Nome_usu,'alternativas': selected_option,'perguntas':pergunta})

def grafico(request):
    perguntas = Base_questoes.objects.order_by('id')
    ids=[]
    for pergunta in perguntas:
        opcoes=[]
        votus=[]
        tudo = Sub_questoes.objects.filter(questao_id=pergunta)
        for dnv in tudo:
            opcoes.append(dnv.ops)
            votus.append(dnv.voto)
        print(opcoes)
        if opcoes:
            ids.append(f"img/grafico_{pergunta.id}.png")
            plt.bar(opcoes, votus)
            plt.xlabel('Perguntas')
            plt.ylabel('votos')
            plt.title(pergunta)
            plt.xticks(rotation=45, ha='right')

            save_path = os.path.join('app_cad_usuarios/static/img', f'grafico_{pergunta.id}.png')
            plt.tight_layout() 
            plt.savefig(save_path)
            plt.close()

    return render(request, 'usuarios/results.html',{'n':ids})