class person:
    def __init__(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour


p1 = person("francis",12,"red")
print(p1.age)    

class polygon:
    def __init__(self,sizes,name):
        self.sizes = sizes
        self.name = name


square = polygon(4,"square")
pentagon = polygon(5,"pentagon")
print(pentagon.sizes)




# introduction to functions 
def greet():
    name = input("enter your name?\n")
    return print("you are welcome ",name)


greet()

def metrics():
    CONST = 100
    cent = float(input("enter in centimeters"))
    solution = CONST / cent
    return print(cent,"in meters is ",solution)

# creating another function to calculate the area of a circle
def area_of_circle(radius):
    PI = 22/7
    area = PI * radius ** 2
    return area

print(area_of_circle(2))




