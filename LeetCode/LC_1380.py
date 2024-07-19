#Om Namah Shivaya
#Leetcode 19-07-2024 Daily question
#Question 1380. Lucky Numbers in a Matrix
class Solution(object):
    def luckyNumbers (self, matrix):
        transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        print(transpose)
        minimum_elements = []
        for row in matrix:
            minimum_elements.append(min(row))
        maximum_elements = []
        for col in transpose:
            maximum_elements.append(max(col))
        answer = []
        for i in minimum_elements:
            if i in maximum_elements:
                answer.append(i)
        return answer