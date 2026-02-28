from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import string
import random


# cores
cores= ['#444466', '#feffff','#f05a43',"#0C0A10" ]

#Configurando Janela
janela= Tk()
janela.title("")
janela.geometry("310x375")
janela.configure(bg="white")


#Configurando Tema a usar
tema=ttk.Style(janela)
tema.theme_use("clam")

# configurando Frame
frame_top= Frame(janela, width=340, height=50, bg=cores[1], pady=0, padx=0, relief="flat" )
frame_top.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=340, height=310, bg="white", pady=0, padx=0, relief="flat" )
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalhando no Tema de Cima
app_name= Label(frame_top,text="GERADOR DE SENHAS ",width=20,padx=0, height=2, relief="flat",anchor="nw", font=("Ivy 16 bold"),fg=cores[0], bg=cores[1])
app_name.place(x=31, y=6)

app_linha= Label(frame_top,text="",width=295,padx=0, height=2, relief="flat",anchor="nw", font=("Ivy 2 bold"),fg="#fb831a", bg="#fb831a")
app_linha.place(x=0, y=45)


# Trabalhando no Tema de Baixo

app_senha= Label(frame_baixo,text="- - - -",width=26,height=2, relief="solid",anchor="center", font=("Ivy 10 bold"),fg=cores[3], bg=cores[1])
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info= Label(frame_baixo,text="Numero Total de Caracteres para a Senha",height=1, relief="flat",anchor="nw", font=("Ivy 10 bold"),fg=cores[0], bg=cores[1])
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=5, pady=1)

var=IntVar(value=8)
spin= Spinbox(frame_baixo,from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, sticky=NW,padx=5, pady=8)

# função geral

def gera():
    
    alfa_maior=string.ascii_uppercase
    alfa_menor=string.ascii_lowercase
    numeros='123456789'
    simbolos='![]{}/*-,.;@_ '

    combinar= ""

    if estado_1.get():
        combinar += alfa_maior

    if estado_2.get():
        combinar += alfa_menor
        
    if estado_3.get():
        combinar += numeros
        
    if estado_4.get():
        combinar += simbolos

    if not combinar:
        app_senha.config(text="Seleciona uma Opção")
        return

    comprimento= int(spin.get())
    senha= "".join(random.choices(combinar, k=comprimento))
    app_senha.config(text=senha)
    

#  FUNCÇÃO COPIAR 
def copiar():

    texto = app_senha.cget("text")

    if texto == "- - - -":
        messagebox.showwarning("Aviso","Gera uma senha primeiro")
        return

    janela.clipboard_clear()
    janela.clipboard_append(texto)
    janela.update()

    messagebox.showinfo("Copiado","Senha copiada com sucesso ✅")


# Trabalhando na Frame Caracteres
frame_caracteres=Frame(frame_baixo,width=340, height=210,bg="white",relief="flat")
frame_caracteres.grid(row=3,column=0,sticky=NSEW, columnspan=2)     


# letras maiusculas 
estado_1=BooleanVar()

check1=Checkbutton(frame_caracteres,width=1,variable= estado_1,relief="flat", bg="white")
check1.grid(row=0, column=0,sticky=NW,padx=2, pady=5)

Label(frame_caracteres,text="ABC letras maiusculas",font=("Ivy 10 bold"),fg=cores[0], bg=cores[1]).grid(row=0,column=1)


# minusculas
estado_2=BooleanVar()

check2=Checkbutton(frame_caracteres,width=1,variable=estado_2,relief="flat", bg="white")
check2.grid(row=1, column=0,sticky=NW,padx=2, pady=5)

Label(frame_caracteres,text="abc letras menusculas",font=("Ivy 10 bold"),fg=cores[0], bg=cores[1]).grid(row=1,column=1)


# numeros
estado_3=BooleanVar()

check3=Checkbutton(frame_caracteres,width=1,variable=estado_3,relief="flat", bg="white")
check3.grid(row=2, column=0,sticky=NW,padx=2, pady=5)

Label(frame_caracteres,text="123 Números",font=("Ivy 10 bold"),fg=cores[0], bg=cores[1]).grid(row=2,column=1)


# simbolos
estado_4=BooleanVar()

check4=Checkbutton(frame_caracteres,width=1,variable=estado_4,relief="flat", bg="white")
check4.grid(row=3, column=0,sticky=NW,padx=2, pady=5)

Label(frame_caracteres,text="!@# Simbolos",font=("Ivy 10 bold"),fg=cores[0], bg=cores[1]).grid(row=3,column=1)


# botão gerar
botao= Button(frame_caracteres,text="Gerar Senha",width=34,height=1,
overrelief="solid",relief="flat",font=("Ivy 10 bold"),
fg=cores[1], bg=cores[2],command=gera)

botao.grid(row=4,column=0,padx=5,pady=11,columnspan=5)


# botão copiar
botao_copiar= Button(frame_baixo,command=copiar,text="Copiar",
width=7,height=2,overrelief="solid",relief="raised",
font=("Ivy 10 bold"),fg=cores[3], bg=cores[1])

botao_copiar.grid(row=0,column=1,padx=5,pady=10)

janela.mainloop()
