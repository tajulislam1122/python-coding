# this project about the typing speed 
# import time module 
from time import*
# import random module
import random as r
# using function 
# this function used for the mistaks 
def mistaks(partest,usertest):
    errer = 0
    for i in range(len(partest)):
        try:
           if partest[i] != usertest[i]:
               errer=errer+1
        except :
           errer=errer+1
    return errer
# this function used for the speed calculat !  
def speed_time(time_s,time_e,user_input):
    time_dalay = time_e - time_s
    time_r = round(time_dalay,2)
    speed = len(user_input)/time_r
    return  round(speed)
# here we used while loop for the multi chouse checking !
while True:
    ch=input("Ready to testing yes/no ?")
    if ch == "yes":
        # this is the pregraph 
        test=["With consistent practice and proper technique",
        "her typing speed saw a significant increase",
        "allowing her to complete tasks more efficiently",]
        # here used random module function and print this random pregraph
        test1=r.choice(test)
        print("***** Typing Speed *****")
        print(test1)
        print()
        print()
        # here is used the time modul function 
        time_1 = time ()
        # here is take the user input 
        input_test = input(" Enter !")
        # here is used the time modul function
        time_2 = time ()
        # the functin call here is it !
        print("speed :",speed_time(time_1,time_2,input_test)," w/sec ")
        print("Errer :",mistaks(test1,input_test))
    elif ch == "no":
        print("Thank you !")
    else:
        print("worng input !")