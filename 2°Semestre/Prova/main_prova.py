import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

class Prova():
    def __init__(self) :
        self.tela=tk.Tk()
        self.tela.geometry("800x500+500+50")
        self.tela.title("Prova...")
        try:self.tela.iconbitmap(os.path.join(os.path.dirname(__file__), "prova.ico"))
        except:pass
        self.tela.resizable(0,0)
        self.total=0
        self.qnt_gente=0
        self.geral=[]
        self.tela_fun()
        self.tela.mainloop()

    def tela_fun(self):
        self.fundo=LabelFrame(self.tela,width=800,height=500,bg="green")
        self.fundo.place(x=0,y=0)
        self.texto=LabelFrame(self.fundo,bg="green",text="Entrevista para saber o estado civil da população da cidade de Sinop...",font="Arial 12 bold",width=800,height=400,bd=0,fg="black")
        self.texto.place(x=0,y=5)
        self.texto_t=Label(self.texto,bg="green",text="Nome:",font="Arial 12 bold",width=20,bd=0,fg="black")
        self.texto_t.place(x=25,y=60)
        self.texto_t=Label(self.texto,bg="green",text="Idade:",font="Arial 12 bold",width=5,bd=0,fg="black")
        self.texto_t.place(x=300,y=60)
        self.nome=Entry(self.texto,font="Arial 12 bold",bd=1,fg="black")
        self.nome.bind("<Return>",lambda event:self.idade.focus())
        self.nome.place(x=25,y=80,height=25,width=200)
        self.idade=Entry(self.texto,font="Arial 12 bold",bd=1,fg="black")
        self.idade.place(x=300,y=80,height=25,width=75)
        self.texto_t=Label(self.texto,bg="green",text=f"Quantidade de entrevistados(a): {self.qnt_gente}.",font="Arial 12 bold",width=80,bd=0,fg="black")
        self.texto_t.place(x=200,y=10)
        self.status=StringVar()       
        self.sexo=StringVar()       
        self.texto_t=Label(self.texto,bg="green",text="Status Civil ?",font="Arial 12 bold",width=80,bd=0,fg="black")
        self.texto_t.place(x=0,y=180)
        self.texto_t=Label(self.texto,bg="green",text="Status Civil ?",font="Arial 12 bold",width=80,bd=0,fg="black")
        self.texto_t.place(x=0,y=180)
        self.A=Radiobutton(self.texto,font="Arial 12 bold",variable=self.status,value="Solteiro",text="Solteiro",bg="green",bd=1,fg="black")
        self.A.place(x=150,y=200)
        self.B=Radiobutton(self.texto,font="Arial 12 bold",variable=self.status,value="Casado",text="Casado",bg="green",bd=1,fg="black")
        self.B.place(x=350,y=200)
        self.C=Radiobutton(self.texto,font="Arial 12 bold",variable=self.status,value="Divorciado",text="Divorciado",bg="green",bd=1,fg="black")
        self.C.place(x=550,y=200)
        self.texto_t=Label(self.texto,bg="green",text="Sexo ?",font="Arial 12 bold",width=80,bd=0,fg="black")
        self.texto_t.place(x=0,y=280)
        self.m=Radiobutton(self.texto,font="Arial 12 bold",variable=self.sexo,value="Masculino",text="Masculino",bg="green",bd=1,fg="black")
        self.m.place(x=250,y=300)
        self.f=Radiobutton(self.texto,font="Arial 12 bold",variable=self.sexo,value="Feminino",text="Feminino",bg="green",bd=1,fg="black")
        self.f.place(x=450,y=300)
        self.confirmar=Button(self.fundo,font="Arial 12 bold",text="Confimar",bg="white",bd=2,fg="black",height=1,width=10,command=self.anotai)
        self.confirmar.place(x=500,y=430)
        self.final=Button(self.fundo,font="Arial 12 bold",text="Finalizar",bg="white",bd=2,fg="black",height=1,width=10,command=self.cadeia)
        self.final.place(x=650,y=430)
        self.nome.focus()
    def anotai(self):
        name=self.nome.get()
        age=self.idade.get()
        satatus=self.status.get()
        sexu=self.sexo.get()
        if name and age and satatus and sexu not in (""):
            if not age.isdigit():
                messagebox.showerror("Erro", "A entrada deve self.er apenas números.")
                self.idade.delete(0, tk.END)
                self.idade.focus()
            else:
                if int(age) ==0:
                    self.idade.delete(0, tk.END)
                    self.idade.focus()
                    messagebox.showerror("Erro", "Nao é possivel ter 0 anos.")
                else:
                    self.geral.append([name,age,satatus,sexu])
                    self.qnt_gente+=1
                    self.ciclo()
        else:
            messagebox.showinfo("Error","Responda corretamente!")
            self.nome.focus()
    def cadeia(self):
        if self.qnt_gente>=1:
            self.fundo.destroy()
            self.fundo_=LabelFrame(self.tela,width=800,height=500,bg="green")
            self.fundo_.place(x=0,y=0)
            self.texto_t=Label(self.fundo_,bg="green",text="Os resultados são..",font="Arial 12 bold",width=80,bd=0,fg="black")
            self.texto_t.place(x=0,y=10)
            self.texto_t=Label(self.fundo_,bg="green",text=f"Quantidade de entrevistados(a): {self.qnt_gente}.",font="Arial 13 bold",width=80,bd=0,fg="black")
            self.texto_t.place(x=0,y=30)
            self.porcem()
        else:
            messagebox.showinfo("Aviso","Minimo de entrevistados, não atingido\n(Minimo= 10)")
            self.nome.focus()

    def porcem(self):
        self.sol=0
        self.cas=0
        self.divo=0
        if len(self.geral) > 0:
            for status in self.geral:
                name,age,satatus,sexu=status
                if satatus=="Solteiro":
                    self.sol+=1
                if satatus=="Casado":
                    self.cas+=1
                if satatus=="Divorciado":
                    self.divo+=1
        self.y=50
        self.ps=self.call_por(self.sol,"Solteiro")
        self.pc=self.call_por(self.cas,"Casado")
        self.pd=self.call_por(self.divo,"Divorciado")
        self.idade_status()
    def call_por(self,qnt,sts):
        try:
            porcentagem=(qnt/self.qnt_gente)*100
        except  ZeroDivisionError:
            porcentagem=0
        
        self.texto_t=Label(self.fundo_,bg="green",text=f"São {int(porcentagem)}% de {sts}s",font="Arial 13 bold",width=80,bd=0,fg="black")
        self.texto_t.place(x=0,y=self.y)
        self.y+=20
    def idade_status(self):
        vs=(self.call_ide_v("Solteiro"))
        vc=(self.call_ide_v("Casado"))
        vd=(self.call_ide_v("Divorciado"))
        ns=(self.call_ide_n("Solteiro"))
        nc=(self.call_ide_n("Casado"))
        nd=(self.call_ide_n("Divorciado"))
        self.sexu()
    def call_ide_v(self,sutatu):
        idade_mais_velha = None
        nome_mais_velha = None
        setatu=None
        for pessoa in self.geral:
            nome, idade,status,sexu = pessoa
            if idade_mais_velha is None or idade > idade_mais_velha and status==sutatu:
                idade_mais_velha = idade
                nome_mais_velha = nome
                setatu=status
        if setatu == sutatu:
            self.texto_t=Label(self.fundo_,bg="green",text=f"O(a) Sr(a) {nome_mais_velha} tem {idade_mais_velha} Anos e está {sutatu}.(Mais Velho)",font="Arial 13 bold",width=80,bd=0,fg="black")
            self.texto_t.place(x=0,y=self.y)
            self.y+=20
        else:
            return
    def call_ide_n(self,sutatu):
        idade_mais_nova = None
        nome_mais_nova = None
        setatu=None
        for pessoa in self.geral:
            nome, idade,status,sexu = pessoa
            if idade_mais_nova is None or idade < idade_mais_nova and status==sutatu:
                idade_mais_nova = idade
                nome_mais_nova = nome
                setatu=status
        if setatu == sutatu:
            self.texto_t=Label(self.fundo_,bg="green",text=f"O(a) Sr(a) {nome_mais_nova} tem {idade_mais_nova} Anos e está {sutatu}.(Mais Novo)",font="Arial 13 bold",width=80,bd=0,fg="black")
            self.texto_t.place(x=0,y=self.y)
            self.y+=20
        else:
            return
    
    def sexu(self):
        sm=(self.call_ultima("Solteiro","Masculino"))
        sf=(self.call_ultima("Solteiro","Feminino"))
        cm=(self.call_ultima("Casado","Masculino"))
        cf=(self.call_ultima("Casado","Feminino"))
        dm=(self.call_ultima("Divorciado","Masculino"))
        df=(self.call_ultima("Divorciado","Feminino"))
    def call_ultima(self,civ,sexuu_v):
        qnt=0
        for pessoa in self.geral:
            nome, idade,status,sexu = pessoa
            if status==civ and sexu==sexuu_v:
                qnt+=1

        self.texto_t=Label(self.fundo_,bg="green",text=f"No total temos: {qnt} de habitantes {civ}(s) do sexo {sexuu_v} .",font="Arial 13 bold",width=80,bd=0,fg="black")
        self.texto_t.place(x=0,y=self.y)
        self.y+=20

    def ciclo(self):
        self.fundo.destroy()
        self.tela_fun()
Prova()