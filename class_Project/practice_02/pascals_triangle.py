from math import ceil

def generateTriangle(triangle_heigth):

    #declare list for main triangle
    triangle = [[0, 1, 0]]

    row_count = 0

    while(row_count < triangle_heigth):

        previous_row_len = len(triangle[row_count])

        newList = [0] * (previous_row_len + 2)


        triangle.append(newList)

        row_count += 1

    fillTriangleRowValues(triangle)
    displayTriangle(triangle)



def displayTriangle(listValue):

    space = len(listValue) * 5

    for index , row in enumerate(listValue):
        print()
        print((" " * space), end="")

        for i in row:

            if i == 0:
                print("", end=" ")
            if i != 0:
                print("{:^5d}".format(i), end="")

        space -= 3




def fillTriangleRowValues(triangle):

    for count, row in enumerate(triangle):

        if count == 0:
            print("true")
            continue;

        length = len(row)
        is_even = True if length % 2 == 0 else False
        starting_index = int((length-2) / 2) + (count+1)%2

        for index in range(starting_index, length, 2):
            a = 0 if index-2 < 0 else triangle[count - 1][index-2]
            b = 0 if index >= len(triangle[count-1]) else triangle[count-1][index]
            newValue = a + b
            triangle[count][index] = newValue

        triangle[count][:ceil(len(triangle[count])/2)-1] = triangle[count][ceil(len(triangle[count])/2):][::-1]


generateTriangle(15)










