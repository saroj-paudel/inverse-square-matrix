from fractions import Fraction

def print_mat(jk):
    print()
    for row in jk:
        print("|",end="")
        print(" ".join(f"{num:5}" for num in row), end=" |\n")
    print()

rw= input("enter row of square matrix: ")
junee = []
print("Enter the matrix row by row (space-separated values):")
for _ in range(int(rw)):
    row = list(map(int, input().split()))
    junee.append(row)



def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def merge_matrices(mat1, mat2):
    return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
def unmerge_matrix(mat):
    n = len(mat)
    half = len(mat[0]) // 2
    original = [row[:half] for row in mat]
    identity = [row[half:] for row in mat]
    return original, identity
identity = identity_matrix(len(junee))

print_mat(junee)


junee = merge_matrices(junee, identity)

print("Solving ...")
print("[A I]=[I A']")
print_mat(junee)

def make_one(mat,m,n):
    if 0!= mat[m][n]:
        if mat[m][n] != 1:
            div = mat[m][n]
            for i in range(len(mat[m])):
                mat[m][i]=Fraction(mat[m][i],div)
            print(f"R{m+1} -> R{m+1}/{div}")
            # print("@@")
            print_mat(mat)
            # print("##")

        for j1 in range(0,m):
            if mat[j1][n] != 0:
                fctr1 = mat[j1][n]
                print(f"R{j1+1} -> R{j1+1} - ({fctr1}*R{m+1})")
                for k1 in range(len(mat[j1])):
                    # print(j,m,k)
                    # print(f"{mat[j1][k1]}={mat[j1][k1]} - {fctr1}*{mat[m][k1]}")
                    mat[j1][k1]=mat[j1][k1] - fctr1*mat[m][k1]
            # print("@@")
                print_mat(mat)
            # print("##")




        for j in range(m+1,len(mat)):
            if mat[j][n] != 0:
                fctr = mat[j][n]
                print(f"R{j+1} -> R{j+1} - ({fctr}*R{m+1})")
                for k in range(len(mat[j])):
                    # print(j,m,k)
                    # print(f"{mat[j][k]}={mat[j][k]} - ({fctr}*{mat[m][k]})")
                    mat[j][k]=mat[j][k] - (fctr*mat[m][k])
            print_mat(mat)
    else:
        print("Can't compute inverse !") 
        exit()  
def solve(matrix):
    for l in range(len(matrix)):
        make_one(matrix,l,l)
    a,inv=unmerge_matrix(junee)
    print("Inverse matrix is :")
    print_mat(inv)

solve(junee)
