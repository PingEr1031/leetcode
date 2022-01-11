# 剑指 Offer 04. 二维数组中的查找
"""在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。"""

import unittest


def findNumberIn2DArray(matrix, target):
    if not matrix or not target:
        return False

    n = len(matrix)
    m = len(matrix[0])
    # 从左上角出发，以此比较matrix[i，j]和target
    i = 0
    j = m - 1
    while i <= n - 1 and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            # 往左移动（排除一列）
            j -= 1
        else:
            i += 1
    return False


class TestSolution(unittest.TestCase):
    def test_mat(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        self.assertEqual(findNumberIn2DArray(matrix, target=5), True)
