from threading import *
import time

class Cube:
    def volume(self, a):
        self.a = a
        time.sleep(1)
        print("The volume is: ", self.a*self.a*self.a)
       

    def amount (self, b):
        self.b = b
        time.sleep(1)
        print ("The amount is: ", self.b * 12)
        


firstObj = Cube()
secondObj = Cube()

t1 = Thread(target = firstObj.volume, args = (5,))


t2 = Thread(target = secondObj.amount, args = ( 5,))

t2.start()
t2.join()

t1.start()
t1.join()
