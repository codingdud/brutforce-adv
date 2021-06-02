
import random
import pyautogui
st=input("enter ur name:")
i=int(input("enter number<=4:"))
pas=pyautogui.password("enter ur password:")
gs=""
cl=list("0123456789")
while True:
    gs=list(st)+random.sample(cl,i
                              )
    s=random.sample(cl,1)
    print("<=========>"+str(gs)+"<========>")
    if gs==list(pas):
        print("your password:"+"".join(gs))
        break
    
    if i ==4:
         print("if4")
         gr=list(st)+s+s+s+s
         if gr==list(pas):
                       print(gr)
                       break
         gr=list(st)+random.sample(cl,1)+s+random.sample(cl,1)+s
         if gr==list(pas):
                       print(gr)
                       break
         gr=list(st)+s+random.sample(cl,1)+s+random.sample(cl,1)
         if gr==list(pas):
                       print(gr)
                       break
                 
    if i ==3:
         print("if3")  
         gr=list(st)+s+s+s
         if gr==list(pas):
                       print(gr)
                       break
         gr=list(st)+s+random.sample(cl,1)+s
         if gr==list(pas):
                       print(gr)
                       break
         gr=list(st)+s+s+random.sample(cl,1)
         if gr==list(pas):
                       print(gr)
                       break 
               
    if i ==2:
         print("if2")   
         gr=list(st)+s+s
         if gr==list(pas):
                       print(gr)
                       break
         gr=list(st)+random.sample(cl,1)+s
         if gr==list(pas):
                       print(gr)
                       break
         gr=list(st)+s+random.sample(cl,1)
         if gr==list(pas):
                       print(gr)
                       break  