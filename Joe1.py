# this game was made by mamoune allouti in 20/09/2022 Djaafra Algeria , at 12:38 
#this game uses  basic artificial intilegence to work 
# this game contain some glitches , your job is to fix it  
# i used here tkinter and random & test the game and fix this problem after finnishing contact me and tell me what wrong i did here, 
# remember always that we all need to learn more how ever you are advanced in this field 
#thank you ------ enjoy working with bugs !!!!


from codecs import BOM_UTF16
from tkinter import *
from tkinter import ttk 
import random
from tkinter import messagebox
root= Tk()
root.title("Tic Tac Toe : AI")
state = True 
winner = ""
count = 0
n = 0
score_x = 0 
score_o = 0

list2 = []

bu1 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu1))
bu2 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu2))
bu3 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu3))
bu4 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu4))
bu5 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu5))
bu6 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu6))
bu7 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu7))
bu8 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu8))
bu9 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu9))
bu10 = Button(root,text=" " , bg="white",width=10,font=('Arial',15),height=5,command=lambda: click(bu9))


# functions 
def ending_game():
    bu1.config(state=DISABLED)
    bu2.config(state=DISABLED)
    bu3.config(state=DISABLED)
    bu4.config(state=DISABLED)
    bu5.config(state=DISABLED)
    bu6.config(state=DISABLED)
    bu7.config(state=DISABLED)
    bu8.config(state=DISABLED)
    bu9.config(state=DISABLED)
    
def checkinfo():
    global winner ,score_x , score_o , count , list1  ,rand
    
    count += 1 
    if bu1["text"] =="X" and bu2["text"] == "X" and bu3["text"] == "X" :
        bu1.configure(bg="green")
        bu2.configure(bg="green")
        bu3.configure(bg="green")
        winner = "X"
        ending_game()
    elif bu4["text"] =="X" and bu5["text"] == "X" and bu6["text"] == "X" :
        bu4.configure(bg="green")
        bu5.configure(bg="green")
        bu6.configure(bg="green")
        winner = "X"
        ending_game()
    elif bu7["text"] =="X" and bu8["text"] == "X" and bu9["text"] == "X" :
        bu7.configure(bg="green")
        bu8.configure(bg="green")
        bu9.configure(bg="green")
        winner = "X"
        ending_game()
    elif bu1["text"] =="X" and bu4["text"] == "X" and bu7["text"] == "X" :
        bu1.configure(bg="green")
        bu4.configure(bg="green")
        bu7.configure(bg="green")
        winner = "X" 
        ending_game()
    elif bu2["text"] =="X" and bu5["text"] == "X" and bu8["text"] == "X" :
        bu2.configure(bg="green")
        bu5.configure(bg="green")
        bu8.configure(bg="green")
        winner = "X" 
        ending_game()
    elif bu3["text"] =="X" and bu6["text"] == "X" and bu9["text"] == "X" :
        bu3.configure(bg="green")
        bu6.configure(bg="green")
        bu9.configure(bg="green")
        winner = "X"
        ending_game()
    elif bu1["text"] =="X" and bu5["text"] == "X" and bu9["text"] == "X" :
        bu1.configure(bg="green")
        bu5.configure(bg="green")
        bu9.configure(bg="green")
        winner = "X"
        ending_game()
    elif bu3["text"] =="X" and bu5["text"] == "X" and bu7["text"] == "X" :
        bu3.configure(bg="green")
        bu5.configure(bg="green")
        bu7.configure(bg="green")
        winner = "X" 
        ending_game()  
    # the o positions 
    elif bu1["text"] =="O" and bu2["text"] == "O" and bu3["text"] == "O" :
        bu1.configure(bg="green")
        bu2.configure(bg="green")
        bu3.configure(bg="green")
        winner = "O"
        ending_game()
 
    elif bu4["text"] =="O" and bu5["text"] == "O" and bu6["text"] == "O" :
        bu4.configure(bg="green")
        bu5.configure(bg="green")
        bu6.configure(bg="green")
        winner = "O"
        ending_game()
    elif bu7["text"] =="O" and bu8["text"] == "O" and bu9["text"] == "O" :
        bu7.configure(bg="green")
        bu8.configure(bg="green")
        bu9.configure(bg="green")
        winner = "O"
        ending_game()
    elif bu1["text"] =="O" and bu4["text"] == "O" and bu7["text"] == "O" :
        bu1.configure(bg="green")
        bu4.configure(bg="green")
        bu7.configure(bg="green")
        winner = "O" 
        ending_game()
    elif bu2["text"] =="O" and bu5["text"] == "O" and bu8["text"] == "O" :
        bu2.configure(bg="green")
        bu5.configure(bg="green")
        bu8.configure(bg="green")
        winner = "O"
        ending_game() 
    elif bu3["text"] =="O" and bu6["text"] == "O" and bu9["text"] == "O" :
        bu3.configure(bg="green")
        bu6.configure(bg="green")
        bu9.configure(bg="green")
        winner = "O"
        ending_game()
    elif bu1["text"] =="O" and bu5["text"] == "O" and bu9["text"] == "O" :
        bu1.configure(bg="green")
        bu5.configure(bg="green")
        bu9.configure(bg="green")
        winner = "O"
        ending_game()
    elif bu3["text"] =="O" and bu5["text"] == "O" and bu7["text"] == "O" :
        bu3.configure(bg="green")
        bu5.configure(bg="green")
        bu7.configure(bg="green")
        winner = "O" 
        ending_game()
    
    if winner == "X" :
        score_x += 1 
        messagebox.showinfo("Tic Tac Toe",f"{winner} won this round")
        ending_game()
    if  winner == "O" :
        messagebox.showerror("Tic Tac Toe",f"{winner} won this round")
        score_o += 1
        ending_game()
    if count == 9 and winner =="" :
        messagebox.showinfo('tic tac toe',"Draw , refresh and play again")
        ending_game()
 
# click -----------------------------------------------------------------click------------------------click----------------------click----------
def click(b):
    global state , count ,list2 ,rand ,winner
    
    list1 = [bu1,bu2,bu3,bu4,bu5,bu6,bu7,bu8,bu9]
  
    if b["text"] == " " and state == True and b["state"] == NORMAL:
        b["text"] = "X"
        state = False
        list2.append(b)
        b["state"] = DISABLED
        
        list1.remove(b)
    rand  = ""
    

    if state == False :    #row ----------------------------------------------------------------------rows -----------------------------------------
        if bu1["text"] == "X" and bu2["text"] == "X" and bu3["state"] == NORMAL:
                rand = bu3
        elif bu2["text"] == "X" and bu3["text"] == "X" and bu1["state"] == NORMAL:
            rand = bu1
        elif bu1["text"] == "X" and bu3["text"] == "X" and bu2["state"] == NORMAL:
            rand = bu2
            
        elif bu4["text"] == "X" and bu5["text"] == "X" and bu6["state"] == NORMAL :
            rand = bu6      
        elif bu4["text"] == "X" and bu6["text"] == "X" and bu5["state"] == NORMAL :
            rand = bu5
        elif bu5["text"] == "X" and bu6["text"] == "X" and bu7["state"] == NORMAL :
            rand = bu4
        elif bu7["text"] == "X" and bu8["text"] == "X" and bu9["state"] == NORMAL:
            rand = bu9
        elif bu7["text"] == "X" and bu9["text"] == "X"and bu8["state"] == NORMAL :
            rand = bu8
        elif bu8["text"] == "X" and bu9["text"] == "X" and bu7["state"] == NORMAL:
            rand = bu7
        #cols ------------------------------------cols------------------------------------cols-------------------------------------cols 01101001110010111010
        elif bu1["text"] == "X" and bu4["text"] == "X" and bu7["state"] == NORMAL:
            rand = bu7
        elif bu1["text"] == "X" and bu7["text"] == "X" and bu1["state"] == NORMAL:
            rand = bu4
        elif bu7["text"] == "X" and bu4["text"] == "X" and bu7["state"] == NORMAL:
            rand = bu1
            
        elif bu2["text"] == "X" and bu5["text"] == "X"and bu8["state"] == NORMAL :
            rand = bu8     
        elif bu8["text"] == "X" and bu5["text"] == "X" and bu2["state"] == NORMAL:
            rand = bu2
        elif bu2["text"] == "X" and bu8["text"] == "X" and bu5["state"] == NORMAL:
            rand = bu5   
        elif bu3["text"] == "X" and bu9["text"] == "X" and bu6["state"] == NORMAL :
            rand = bu6
        elif bu6["text"] == "X" and bu9["text"] == "X" and bu3["state"] == NORMAL:
            rand = bu3
        elif bu3["text"] == "X" and bu6["text"] == "X" and bu9["state"] == NORMAL:
            rand = bu9
        # other side------------------------------------------------other sides---------------------------other sides-------------------------
        
        elif bu1["text"] == "X" and bu5["text"] == "X" and state == False and bu9["state"] == NORMAL:
            rand = bu9
        elif bu1["text"] == "X" and bu9["text"] == "X" and bu5["state"] == NORMAL:
            rand = bu5
        elif bu5["text"] == "X" and bu9["text"] == "X" and bu1["state"] == NORMAL:
            rand = bu1
            
        elif bu3["text"] == "X" and bu5["text"] == "X" and bu7["state"] == NORMAL :
            rand = bu7     
        elif bu7["text"] == "X" and bu5["text"] == "X" and bu7["state"] == NORMAL :
            rand = bu3
        elif bu7["text"] == "X" and bu3["text"] == "X" and bu5["state"] == NORMAL  :
            rand = bu5 
        else :
            rand = random.choice(list1)
        if rand["state"] != DISABLED:
            rand["text"] = "O"
            rand["state"] = DISABLED 
            state = True
            list1.remove(rand)
            print(b,rand)
            checkinfo()
        if list1 == [] :
            checkinfo()

    
    
        
    
 #ai-----------------------------------AI-------------------AI-----------------------AI-------------------------AI--------------------------AI
def ai_round(b):
    global list1 , list2 , state ,count ,rand
    rand  = ""
    

        #row ----------------------------------------------------------------------rows -----------------------------------------
    if bu1["text"] == "X" and bu2["text"] == "X" and bu3["state"] == NORMAL:
            rand = bu3
    elif bu2["text"] == "X" and bu3["text"] == "X" and bu1["state"] == NORMAL:
        rand = bu1
    elif bu1["text"] == "X" and bu3["text"] == "X" and bu2["state"] == NORMAL:
        rand = bu2
        
    elif bu4["text"] == "X" and bu5["text"] == "X" and bu6["state"] == NORMAL :
        rand = bu6      
    elif bu4["text"] == "X" and bu6["text"] == "X" and bu5["state"] == NORMAL :
        rand = bu5
    elif bu5["text"] == "X" and bu6["text"] == "X" and bu7["state"] == NORMAL :
        rand = bu4
    elif bu7["text"] == "X" and bu8["text"] == "X" and bu9["state"] == NORMAL:
        rand = bu9
    elif bu7["text"] == "X" and bu9["text"] == "X"and bu8["state"] == NORMAL :
        rand = bu8
    elif bu8["text"] == "X" and bu9["text"] == "X" and bu7["state"] == NORMAL:
        rand = bu7
    #cols ------------------------------------cols------------------------------------cols-------------------------------------cols 01101001110010111010
    elif bu1["text"] == "X" and bu4["text"] == "X" and bu7["state"] == NORMAL:
        rand = bu7
    elif bu1["text"] == "X" and bu7["text"] == "X" and bu1["state"] == NORMAL:
        rand = bu4
    elif bu7["text"] == "X" and bu4["text"] == "X" and bu7["state"] == NORMAL:
        rand = bu1
        
    elif bu2["text"] == "X" and bu5["text"] == "X"and bu8["state"] == NORMAL :
        rand = bu8     
    elif bu8["text"] == "X" and bu5["text"] == "X" and bu2["state"] == NORMAL:
        rand = bu2
    elif bu2["text"] == "X" and bu8["text"] == "X" and bu5["state"] == NORMAL:
        rand = bu5   
    elif bu3["text"] == "X" and bu9["text"] == "X" and bu6["state"] == NORMAL :
        rand = bu6
    elif bu6["text"] == "X" and bu9["text"] == "X" and bu3["state"] == NORMAL:
        rand = bu3
    elif bu3["text"] == "X" and bu6["text"] == "X" and bu9["state"] == NORMAL:
        rand = bu9
    # other side------------------------------------------------other sides---------------------------other sides-------------------------
    
    elif bu1["text"] == "X" and bu5["text"] == "X" and state == False and bu9["state"] == NORMAL:
        rand = bu9
    elif bu1["text"] == "X" and bu9["text"] == "X" and bu5["state"] == NORMAL:
        rand = bu5
    elif bu5["text"] == "X" and bu9["text"] == "X" and bu1["state"] == NORMAL:
        rand = bu1
        
    elif bu3["text"] == "X" and bu5["text"] == "X" and bu7["state"] == NORMAL :
        rand = bu7     
    elif bu7["text"] == "X" and bu5["text"] == "X" and bu7["state"] == NORMAL :
        rand = bu3
    elif bu7["text"] == "X" and bu3["text"] == "X" and bu5["state"] == NORMAL  :
        rand = bu5 
    elif rand == "" and state == False :
        rand = random.choice(list1)
        
    if rand not in list2 and rand["state"] != DISABLED:
        rand["text"] = "O"
        rand["state"] = DISABLED 
        state = True
        list1.remove(rand)
        print(b,rand)
        checkinfo()
    if list1 == [] :
        checkinfo()
            
    
    

    

        
        
               
# the buttons ----------------------------Buttons----------------------Buttons-------------------------------Buttons-----------------------------------

burefresh = Button(root,text="refresh" , bg="white",width=10,font=('Arial',15),height=5)
score_xl = Label(root,text=f"X : {score_x}",font=("Arial",15))
score_ol = Label(root,text=f"o : {score_o}",font=("Arial",15))

#refresh---------------------------------------refresh--------------------------------refresh--------------------------refresh--------------------

def refresh():
    global winner , score_x , score_o ,state , list1 , list2 , rand ,count
    bu1.config(state=NORMAL,bg="white",text=" ")
    bu2.config(state=NORMAL,bg="white",text=" ")
    bu3.config(state=NORMAL,bg="white",text=" ")
    bu4.config(state=NORMAL,bg="white",text=" ")
    bu5.config(state=NORMAL,bg="white",text=" ")
    bu6.config(state=NORMAL,bg="white",text=" ")
    bu7.config(state=NORMAL,bg="white",text=" ")
    bu8.config(state=NORMAL,bg="white",text=" ")
    bu9.config(state=NORMAL,bg="white",text=" ")
    score_xl.config(text=f"{score_x}")
    score_ol.config(text=f"{score_o}")
    click.list1 = [bu1,bu2,bu3,bu4,bu5,bu6,bu7,bu8,bu9]
     
    list2 = []
    state = True
    winner = ""
    count = 0
    rand = ""
    
burefresh.config(command=refresh)
    
bu1.grid(row=0,column=0)
bu2.grid(row=0,column=1)
bu3.grid(row=0,column=2)
bu4.grid(row=1,column=0)
bu5.grid(row=1,column=1)
bu6.grid(row=1,column=2)
bu7.grid(row=2,column=0)
bu8.grid(row=2,column=1)
bu9.grid(row=2,column=2)
burefresh.grid(row=1,column=3)
score_xl.grid(row=0,column=3)
score_ol.grid(row=2,column=3)


root.mainloop()



