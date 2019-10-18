

length = 1.0
width = 1.0


def setLength(l):
    length = l

def getLength():
    return length

def setWidth(w):
    width = w

def getWidth():
    return width

def calPerimeter():
    perimeter = 2 * (getLength() + getWidth())
    return perimeter

len_temp = input("Enter rectangles length ")

##setLength(float(len_temp))
length = float(len_temp)

print(getLength())
wid_temp = input("Enter rectangles width ")

##setWidth(float(wid_temp))
print(getWidth())
width = float(wid_temp)

print("Perimeter equals: ", calPerimeter())
