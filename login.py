from tkinter import *



def verifica_senha(user, senha):
    if user == "admin" and senha == "admin":
        print("Usuário Validado!")        
    else:
        print("Usuário inválido!")

login = Tk()
login.title("LOGIN")
login.geometry("500x250+200+200") 
login.resizable(True, True) #controla o redimensionamento da janela
login.minsize(200, 100)
login.maxsize(400, 150)
#login.state("zoomed") #executar em modo maximizado
#login.iconbitmap("IMAGENS/ICONE.ico")

container1 = Frame()
container1["pady"] = 10
container1.pack()

container2 = Frame()
container2["padx"] = 20
container2["pady"] = 5
container2.pack()

container3 = Frame()
container3["padx"] = 20
container3["pady"] = 5
container3.pack()

login = Label(container1, text = "LOGIN: ", font = "Calibri 12 bold")
login.pack(side = LEFT)
txtlogin = Entry(container1)
txtlogin["width"] = 20
txtlogin.pack(side=LEFT)

senha = Label(container2, text = "SENHA: ", font = "Calibri 12 bold")
senha.pack(side = LEFT)
txtsenha = Entry(container2, show="*")
txtsenha["width"] = 20
txtsenha.pack(side=LEFT)

botaologin = Button(container3, text = "LOGIN",
                    command=lambda: verifica_senha(txtlogin.get(),txtsenha.get()))
btnsair = Button(container3, text="SAIR", command=login.quit)
botaologin.pack(side=LEFT)
btnsair.pack(side=RIGHT)

    
login.mainloop()