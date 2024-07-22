#Om Namah Shivaya
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = []
        for i in range(len(names)):
            temp = []
            temp.append(names[i])
            temp.append(heights[i])
            people.append(temp)
        people.sort(key=lambda x:x[1])
        people = people[::-1]
        res = []
        for i in people:
            res.append(i[0])
        return res