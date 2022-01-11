# 逆波兰表达式是一种后缀表达式
# 算符写在后面
"""
适合用栈操作运算：
1、遇到数字则入栈；
2、遇到算符则取出栈顶两个数字进行计算
3、将结果压入栈中。
"""
import unittest
import operator


class Solution:
    def evalRPN(self, tokens):
        # 运算符字符串
        cal = "+-*/"
        oper = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y)

        }
        # 创建栈
        stack = []
        for i in tokens:
            try:
                num = int(i)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = oper[i](num1, num2)
            finally:
                stack.append(num)
        return stack[0]


class Test_Solution(unittest.TestCase):
    def test_1(self):
        ans = Solution()
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(ans.evalRPN(tokens), 9)

    def test_2(self):
        ans = Solution()
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(ans.evalRPN(tokens), 22)

    def test_3(self):
        ans = Solution()
        tokens = ["1", "2", "+"]
        self.assertEqual(ans.evalRPN(tokens), 3)


if __name__ == '__main__':
    unittest.main()
