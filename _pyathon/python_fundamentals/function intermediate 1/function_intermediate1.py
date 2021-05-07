
import random
def randInt(min=0 , max= 100  ):
    num = random.random() * (max-min) + min

    return round(num)
print(randInt(20))
print(randInt(20,100))
print(randInt(max=20, min=10))
print(randInt())