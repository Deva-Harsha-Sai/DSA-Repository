#Om Namah Shivaya
class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        transpose = [[row[i] for row in grid] for i in range(len(grid[0]))]
        rowsZeroes = []
        rowsOnes = []
        for i in grid:
            rowsZeroes.append(i.count(0))
            rowsOnes.append(i.count(1))
        colZeroes = []
        colOnes = []
        for i in transpose:
            colZeroes.append(i.count(0))
            colOnes.append(i.count(1))
        ans = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(rowsOnes[i]+colOnes[j]-rowsZeroes[i]-colZeroes[j])
            ans.append(temp)
        return ans