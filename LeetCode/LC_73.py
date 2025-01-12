class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    matrix[i][j] = "z"
                    for p in range(0,row):
                        if matrix[p][j]!=0:
                            matrix[p][j]="z"
                    for q in range(0,col):
                        if matrix[i][q]!=0:
                            matrix[i][q]="z"
        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j]=="z":
                    matrix[i][j]=0
        return matrix