import random
class game:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def result(self):
       count=0
       if(self.bgame!=self.inpnum):
           count=+1
           print("Oops try again !")
           self.start()
           self.brain()
           self.result()
           
       else:
            if(count==0):
                print("Horray you have in single shot !")
            else:
                print("you have won after",count,"retries")
        
       
            
          
       
    def start(self):
        print("guess the number in range(1-10) \n")
        number=int(input())
        self.inpnum=number
        print(self.name,'have entered \n ',number)
    def brain(self):
       self.bgame=random.randrange(1,10)
   
    
name=input("enter your name \n")
age=int(input("enter your age \n"))
obj=game(name,age)

obj.start()
obj.brain()
obj.result()
    
        
        