from tkinter import *
from math import sqrt

root = Tk()
root.geometry("400x400")
root.configure(background="gray")
root.title("calculadora")
root.iconbitmap("img/calculadora.ico")
mostrar = ""
equacao = StringVar()

def botao(num):
    global mostrar
    mostrar = mostrar + str(num)
    equacao.set(mostrar)

def calculo():
    global mostrar
    total = str(eval(mostrar))
    equacao.set(total)
    mostrar= ""

def limpar():
    global mostrar
    mostrar = ""
    equacao.set("")

def raiz():
    global mostrar
    mostrar = float(mostrar)
    quadrada = mostrar**0.5
    mostrar = str(quadrada)
    equacao.set(mostrar)
    mostrar = ""

def porcentagem():
    global mostrar
    mostrar = float(mostrar)
    porcento = mostrar*(1)/100 
    mostrar = str(porcento)
    equacao.set(mostrar)
    mostrar = ""

#Tela
f=Frame(root,bg="#575656", width=400,borderwidth=3, relief="raised")
f.place(x=0,y=0,height=100)
tela = Label(root, textvariable=equacao, bg="#575656", fg="white", font="Arial 40 bold")
tela.place(x=10,y=20)

#4 coluna
bRoot=Button(root, bg="#FF8A35", text="/", fg="white", font="Arial 28 bold",command=lambda:botao("/"))
bRoot.place(x=300,y=100, width=100, height=60)
bMult=Button(root, bg="#FF8A35", text="x", fg="white", font="Arial 28 bold",command=lambda:botao("*"))
bMult.place(x=300,y=160, width=100, height=60)
bSub=Button(root, bg="#FF8A35", text="-", fg="white", font="Arial 28 bold",command=lambda:botao("-"))
bSub.place(x=300,y=220, width=100, height=60)
bPlus=Button(root, bg= "#FF8A35", text="+", fg="white", font= "Arial 28 bold",command=lambda:botao("+"))
bPlus.place(x=300,y=280, width=100, height=60)
bIgual=Button(root, bg="#FF8A35", text="=", fg="white", font="Arial 28 bold",command=lambda:calculo())
bIgual.place(x=300,y=340, width=100, height=60)

#3 coluna
b=Button(root, bg="#B3B3B3", text="C", fg="white", font="Arial 28 bold", command=lambda:limpar())
b.place(x=200,y=100, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="9", fg="white", font="Arial 28 bold",command=lambda:botao(9))
b.place(x=200,y=160, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="6", fg="white", font="Arial 28 bold",command=lambda:botao(6))
b.place(x=200,y=220, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="3", fg="white", font="Arial 28 bold",command=lambda:botao(3))
b.place(x=200,y=280, width=100, height=60)
b=Button(root, bg="#B3B3B3", text=".", fg="white", font="Arial 28 bold",command=lambda:botao("."))
b.place(x=200,y=340, width=100, height=60)

#2 coluna
b=Button(root, bg="#B3B3B3", text="√", fg="white", font="Arial 28 bold",command=lambda:raiz())
b.place(x=100,y=100, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="8", fg="white", font="Arial 28 bold",command=lambda:botao(8))
b.place(x=100,y=160, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="5", fg="white", font="Arial 28 bold",command=lambda:botao(5))
b.place(x=100,y=220, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="2", fg="white", font="Arial 28 bold",command=lambda:botao(2))
b.place(x=100,y=280, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="0", fg="white", font="Arial 28 bold",command=lambda:botao(0))
b.place(x=100,y=340, width=100, height=60)

#1 coluna
b=Button(root, bg="#B3B3B3", text="%", fg="white", font="Arial 28 bold",command=lambda:porcentagem())
b.place(x=0,y=100, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="7", fg="white", font="Arial 28 bold",command=lambda:botao(7))
b.place(x=0,y=160, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="4", fg="white", font="Arial 28 bold",command=lambda:botao(4))
b.place(x=0,y=220, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="1", fg="white", font="Arial 28 bold",command=lambda:botao(1))
b.place(x=0,y=280, width=100, height=60)
b=Button(root, bg="#B3B3B3", text="^", fg="white", font="Arial 28 bold",command=lambda:botao("**"))
b.place(x=0,y=340, width=100, height=60)

root.mainloop() 
