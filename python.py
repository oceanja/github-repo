from time import *
import random as r
def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
             error=error+1
        except:
            error=error+1
    return error        
                 
def speed_time(time_s,time_e,userinput):
     time_delay=time_e - time_s
     time_r=round(time_delay,2)
     speed=len(userinput)/time_r
     return round(speed)
        
    
test=["hello i am happy","this is a big thing","welcome to my house,it is beautiful","i am very exhausted seriously"]
test1=r.choice(test)
print("*******Typing speed calculator*******")
print(test1)
print()
print()
time1=time()
testinput=input("Enter: ")
time2=time()

print('Speed:',speed_time(time1,time2,testinput),"w/s")
print("Error:",mistake(test1,testinput))
