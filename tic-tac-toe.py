#SAGATAVO DARBA VIDI
from tkinter import *
from tkinter import messagebox #paziņojumi, ieteikumi
mansLogs=Tk() #loga objekts
mansLogs.title("TicTacToe")


#Divi spēlētāji spēlēs vienā datorā
#Pirmais sāks X, otrais - O


#POGU IZVEIDE, PIEVIENOŠANA (LAUKUMU VEIDO KĀ POGAS)
btn1=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn1),bg="whitesmoke") #pogas izmērs, teksta fonts un strādāšana
btn2=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn2),bg="lightblue")
btn3=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn3),bg="whitesmoke")
btn4=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn4),bg="lightblue")
btn5=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn5),bg="whitesmoke")
btn6=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn6),bg="lightblue")
btn7=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn7),bg="whitesmoke")
btn8=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn8),bg="lightblue")
btn9=Button(mansLogs,text="",width=6,height=3,font=("Helvica",24),command=lambda:btnClick(btn9),bg="whitesmoke") #kopā 9 spēļu lauciņi


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


#POGU STĀVOKLIS
def disableButtons(): #spēle beidzas, pogas izslēdzas
     btn1.config(state=DISABLED) #pogas stāvoklis ir izslēgts
     btn2.config(state=DISABLED)
     btn3.config(state=DISABLED)
     btn4.config(state=DISABLED)
     btn5.config(state=DISABLED)
     btn6.config(state=DISABLED)
     btn7.config(state=DISABLED)
     btn8.config(state=DISABLED)
     btn9.config(state=DISABLED)
     return 0

def reset():
     btn1.config(state=NORMAL)
     btn2.config(state=NORMAL)
     btn3.config(state=NORMAL)
     btn4.config(state=NORMAL)
     btn5.config(state=NORMAL)
     btn6.config(state=NORMAL)
     btn7.config(state=NORMAL)
     btn8.config(state=NORMAL)
     btn9.config(state=NORMAL)

     btn1["text"]=""
     btn2["text"]=""
     btn3["text"]=""
     btn4["text"]=""
     btn5["text"]=""
     btn6["text"]=""
     btn7["text"]=""
     btn8["text"]=""
     btn9["text"]=""

     global winner, count, speletajsX
     winner=False
     count=0
     speletajsX=True
     return 0

    
#DEFINĒ MAINĪGOS
speletajsX=True #kuram spēlētājam kārta spēlēt, liks krustiņus
count=0 #aizpildīto rūtiņu skaits
winner=True


#UZVARĒTĀJA FUNKCIJA
def checkWinner():
    global winner #checkWinner
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
            disableButtons() #iekavā kaut kas notiek
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
            disableButtons()
            messagebox.showinfo("Tic-Tac-Toe","Spēlētājs O ir uzvarētājs!")
    elif count==9 and winner==False:
         disableButtons()
         messagebox.showinfo("Tic-Tac-Toe","Spēle beidzās ar neizšķirtu!")
    return


#POGU FUNKCIJA
def btnClick(button): #poga klikšķinās
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


def infoLogs():
    jaunsLogs=Toplevel()
    jaunsLogs.title("Informācija par programmu")
    jaunsLogs.geometry("1250x255")
    virsraksts=Label(jaunsLogs,text="Spēles noteikumi",font=("Verdana",20,"bold"))
    virsraksts.grid(row=0,column=0)
    apraksts1=Label(jaunsLogs,text="1. Spēlē piedalās divi spēlētāji;",font=("Verdana",12),padx=0)
    apraksts1.grid(row=1,column=0)
    apraksts2=Label(jaunsLogs,text="2. Spēles sākumā viens spēlētājs izvēlas X zīmi, bet otrs spēlētājs izvēlas O zīmi;",font=("Verdana",12))
    apraksts2.grid(row=2,column=0)
    apraksts3=Label(jaunsLogs,text="3. Spēlētāji pēc kārtas liek savas zīmes uz tukšiem lauciņiem;",font=("Verdana",12))
    apraksts3.grid(row=3,column=0)
    apraksts4=Label(jaunsLogs,text="4. Spēlētājs var likt savu zīmi tikai uz tukša lauciņa;",font=("Verdana",12))
    apraksts4.grid(row=4,column=0)
    apraksts5=Label(jaunsLogs,text="5. Spēlētāji liek savas zīmes pēc kārtas",font=("Verdana",12))
    apraksts5.grid(row=5,column=0)
    apraksts6=Label(jaunsLogs,text="6. Spēle turpinās, līdz vienam no spēlētājiem izdodas iegūt trīs savas zīmes rindā, kolonnā;",font=("Verdana",12))
    apraksts6.grid(row=6,column=0)
    apraksts7=Label(jaunsLogs,text="7. Ja laukums tiek pilnībā aizpildīts, un nevienam spēlētājam neizdodas iegūt trīs zīmes rindā, kolonnā vai diagonālē, tad spēle beidzas ar neizšķirtu;",font=("Verdana",12))
    apraksts7.grid(row=7,column=0)
    apraksts8=Label(jaunsLogs,text="8. Spēlētāji nevar mainīt savu gājienu, un nevar likt savu zīmi uz jau aizpildītas rūtiņas;",font=("Verdana",12))
    apraksts8.grid(row=8,column=0)
    apraksts9=Label(jaunsLogs,text="9. Spēli var spēlēt vairākas reizes, mainot spēlētāju, kas sāk spēli.",font=("Verdana",12))
    apraksts9.grid(row=9,column=0)
    return 0

#infoLogs()
#jaunsLogs.create_text(300,50,text="Hello world!")

#GALVENĀ IZVĒLNE
galvenaIzvelne=Menu(mansLogs) #izveido galveno izvēlni
mansLogs.config(menu=galvenaIzvelne) #pievieno galvenajam logam


#MAZĀ IZVĒLNE
opcijas=Menu(galvenaIzvelne,tearoff=False)#mazā izvelne
galvenaIzvelne.add_cascade(label="Opcijas",menu=opcijas) #lejupkrītošais saraksts
galvenaIzvelne.add_command(label="Par programmu", command=infoLogs)#pievieno mazajai izvēlnei


#MAZĀS IZVĒLNES KOMANDAS 
opcijas.add_command(label="Jauna spēle", command=reset)#jaunas speles sākšanas poga
opcijas.add_command(label="Iziet",command=mansLogs.quit) #aiztaisa logu, speli


mansLogs.mainloop()