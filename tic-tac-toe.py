from tkinter import *
from tkinter import messagebox #paziņojumi, ieteikumi

mansLogs=Tk() #loga objekts
mansLogs.title("TicTacToe")


#DEFINĒ MAINĪGOS
speletajsX=True
count=0
winner=True
#Divi spēlētāji spēlēs vienā datorā
#Pirmais sāks X, otrais - O

#POGU FUNKCIJA
def btnClick(button): #poda klikšķinās
    global speletajsX,count #kādi mainīgie tiks izmantoti visā programmā
    if button["text"]==""and speletajsX==True: #X spēlētāja kārta spēle (true), uz pogām nav nekā
        button["text"]="X" #nomaina tukšo rūtiņu uz X
        speletajsX=False #spelētāja X kārta ir beigusies
        count+=1 #palielina rūtiņu skaitu skaitu
        checkWinner()
    elif button["text"]==""and speletajsX==False:
        button["text"]="O"
        speletajsX=True
        count+=1
        checkWinner()
    else:
        messagebox.showerror("Tic-Tac-Toe", "Šeit kāds ir klikšķinājis!")
    return



#POGU IZVEIDE, PIEVIENOŠANA (LAUKUMU VEIDO KĀ POGAS)
btn1=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn1)) #pogas izmērs, teksta fonts un strādāšana
btn2=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn2))
btn3=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn3))
btn4=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn4))
btn5=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn5))
btn6=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn6))
btn7=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn7))
btn8=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn8))
btn9=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn9))


#POGU PIEVIENOŠANA, NOVIETOJUMS
btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)


#UZVARĒTĀJA FUNKCIJA
def checkWinner():
    global checkWinner
    winner=False #noteiks, ja būs neizšķirts
    if (btn1["text"]=="X"and btn2["text"]=="X"and btn3["text"]=="X"or 
        btn4["text"]=="X"and btn5["text"]=="X"and btn6["text"]=="X"or
        btn7["text"]=="X"and btn8["text"]=="X"and btn9["text"]=="X"or
        btn1["text"]=="X"and btn5["text"]=="X"and btn9["text"]=="X"or
        btn3["text"]=="X"and btn5["text"]=="X"and btn7["text"]=="X"or
        btn1["text"]=="X"and btn4["text"]=="X"and btn7["text"]=="X"or
        btn2["text"]=="X"and btn5["text"]=="X"and btn8["text"]=="X"or
        btn3["text"]=="X"and btn6["text"]=="X"and btn9["text"]=="X"):
            winner=True
            messagebox.showinfo("Tic-Tac-Toe","Spēlētājs X ir uzvarētājs!")
    elif (btn1["text"]=="O"and btn2["text"]=="O"and btn3["text"]=="O"or 
        btn4["text"]=="O"and btn5["text"]=="O"and btn6["text"]=="O"or
        btn7["text"]=="O"and btn8["text"]=="O"and btn9["text"]=="O"or
        btn1["text"]=="O"and btn5["text"]=="O"and btn9["text"]=="O"or
        btn3["text"]=="O"and btn5["text"]=="O"and btn7["text"]=="O"or
        btn1["text"]=="O"and btn4["text"]=="O"and btn7["text"]=="O"or
        btn2["text"]=="O"and btn5["text"]=="O"and btn8["text"]=="O"or
        btn3["text"]=="O"and btn6["text"]=="O"and btn9["text"]=="O"):
            winner=True
            messagebox.showinfo("Tic-Tac-Toe","Spēlētājs O ir uzvarētājs!")
    elif count==9 and winner==False:
         messagebox.showinfo("Tic-Tac-Toe","Spēle beidzās ar neizšķirtu!")


mansLogs.mainloop()