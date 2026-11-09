

class Calc:
    def __init__(self):
        pass 

    def add(self , a , b):
        return a+b 

    def divide(self , a , b):
        if a == 0 or b == 0:
            return ValueError("can not divide by zero")
        else:
            return a // b 

        
        