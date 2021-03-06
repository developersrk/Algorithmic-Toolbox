# Time:  ctor:   O(mlogm * nlogn)
#        update: O(logm * logn)
#        query:  O(logm * logn)
# Space: O(m * n)

# Binary Indexed Tree (BIT) solution.
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.__matrix = matrix
        self.__bit = [[0] * (len(self.__matrix[0]) + 1) \
                      for _ in xrange(len(self.__matrix) + 1)]
        for i in xrange(len(self.__matrix)):
            for j in xrange(len(self.__matrix[0])):
                self.__add(i, j, matrix[i][j])
        print self.__bit
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if val - self.__matrix[row][col]:
            self.__add(row, col, val - self.__matrix[row][col])
            self.__matrix[row][col] = val


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        def sumRegion_bit(row, col):
            row += 1
            col += 1
            ret = 0
            i = row
            while i > 0:
                j = col
                while j > 0:
                    ret += self.__bit[i][j]
                    j -= (j & -j)
                i -= (i & -i)
            return ret
    
        ret = sumRegion_bit(row2, col2)
        if row1 > 0 and col1 > 0:
            ret += sumRegion_bit(row1 - 1, col1 - 1)
        if col1 > 0:
            ret -= sumRegion_bit(row2, col1 - 1)
        if row1 > 0:
            ret -= sumRegion_bit(row1 - 1, col2)
        return ret

    def __add(self, row, col, val):
        row += 1
        col += 1
        i = row
        while i <= len(self.__matrix):
            j = col
            while j <= len(self.__matrix[0]):
                self.__bit[i][j] += val
                j += (j & -j)
            i += (i & -i)


# Your NumMatrix object will be instantiated and called as such:
matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(0, 1, 2, 3)
numMatrix.update(1, 1, 10)
print numMatrix.sumRegion(1, 2, 3, 4)
