import numpy as np

def choice1(choice):
    n1 = int(input("Enter the number of matrices you want to operate on: "))
    print("Provide your", n1, "matrices:")
    matrices = []

    for _ in range(n1):
        r = int(input("Enter the number of rows: "))
        c = int(input("Enter the number of columns: "))
        print(f"Enter the elements of the matrix {len(matrices) + 1} row by row:")
        matrix = []
        for _ in range(r):
            row = list(map(int, input().split()))
            if len(row) != c:
                print("Error: Incorrect number of columns. Please re-enter the row.")
                row = list(map(int, input().split()))
            matrix.append(row)
        matrices.append(matrix)

    rmatrix = [[0 for _ in range(c)] for _ in range(r)]

    if choice == 1:
        for matrix in matrices:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    rmatrix[i][j] += matrix[i][j]
    else:
        rmatrix = matrices[0]
        for matrix in matrices[1:]:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    rmatrix[i][j] -= matrix[i][j]

    print("The result matrix is:")
    for row in rmatrix:
        print(row)

def choice3():
    print("Enter your matrix:")
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    print("Enter the elements of the matrix row by row:")
    matrix = [list(map(int, input().split())) for _ in range(r)]
    
    a = np.array(matrix)
    rank = np.linalg.matrix_rank(a)
    print("The rank of the matrix is:", rank)

def choice4():
    print("Enter your matrix:")
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    print("Enter the elements of the matrix row by row:")
    matrix = [list(map(int, input().split())) for _ in range(r)]
    
    a = np.array(matrix)
    eigen_values, eigen_vectors = np.linalg.eig(a)
    print("Eigen values are:", eigen_values)
    print("Eigen vectors are:", eigen_vectors)

def choice5():
    print("Enter your matrix:")
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    print("Enter the elements of the matrix row by row:")
    matrix = [list(map(int, input().split())) for _ in range(r)]
    
    a = np.array(matrix)
    inverse = np.linalg.inv(a)
    print("The inverse of the matrix is:", inverse)

def choice6():
    print("Thank you for using the matrix calculator. Goodbye!")

print('''Welcome to your matrix calculator...
Enter 1: To perform addition 
Enter 2: To perform subtraction
Enter 3: To find the rank
Enter 4: To calculate eigen vectors and eigen values
Enter 5: To calculate the inverse of a matrix
Enter 6: Exit''')

while True:
    choice = int(input("Enter the operation number: "))
    if choice in [1, 2]:
        choice1(choice)
    elif choice == 3:
        choice3()
    elif choice == 4:
        choice4()
    elif choice == 5:
        choice5()
    elif choice == 6:
        choice6()
        break
    else:
        print("Invalid choice. Please try again.")
