#Object is part of class/instance of classs that intialize  or call any method/ variables inside that class
#class : is definations
class Human:
    # self here it's object  for calling itself and variables 
    def speak(self):
        print("hi i do want speak")
    
    
    def eat(self):
        
        print("i eat apple")
    
    def read(self):
        print("book name : sharlock holmes")
    
    
    def sleep(self):
        
        print("sleeping:ZzZzZz");


def main():
    
   #dot it's refernce to the class method or vaiables 
    jhon = Human()
    jhon.speak()
    jhon.eat()
    jhon.sleep() 

if __name__ =='__main__':main()