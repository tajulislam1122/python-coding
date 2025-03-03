
from tkinter import *
from tkinter import ttk 
import os 
# funtion about restart
def restart():
    os.system("C:\\Windows\\System32\\shutdown.exe /r /t 1")
# funtion about restart time 
def restart_time():
    os.system("C:\\Windows\\System32\\shutdown.exe /r /t 20")
# funtion about shutdown
def logout():
    os.system("C:\\Windows\\System32\\shutdown.exe /l")
# funtion about shutdown
def shutdown():
    os.system("C:\\Windows\\System32\\shutdown.exe /s /t 0")
# main window 
st =Tk()
st.title("shutdown App")
st.geometry("500x500")
st.config(bg="black")
# Rstart butten
r_butten=Button(st,text="Rstart",font=("Time New Roman",20,"bold"),
            relief=RAISED,cursor="plus",command=restart)
r_butten.place(x=150,y=70,height=40,width=200)
# Rstart buttem time 
rt_butten=Button(st,text="Rstart Time",font=("Time New Roman",20,"bold"),
            relief=RAISED,cursor="plus",command=restart_time)
rt_butten.place(x=150,y=170,height=40,width=200)
# Logout butten
lg_butten=Button(st,text="Log_Out",font=("Time New Roman",20,"bold"),
            relief=RAISED,cursor="plus",command=logout)
lg_butten.place(x=150,y=270,height=40,width=200)
# shutdown butten
st_butten=Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),
            relief=RAISED,cursor="plus",command=shutdown)
st_butten.place(x=150,y=370,height=40,width=200)



st.mainloop()
  
