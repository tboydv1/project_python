from matrix import Matrix


def main():

    A = Matrix([[1,2,3], [2, 4, 4], [4, 4, 4]])
    B = Matrix([[1,2,3], [2, 40, 4], [4, 4, 4]])


    print(A)
    print(B)
    print(B.add(A))

     
if __name__ == '__main__':
    main()
