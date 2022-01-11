class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        stack = []
        # 设置一个栈，从头依次扫描字符串
            #loop: 判断当前元素和栈顶元素是否相等，相等则pop，不等则入栈
        for e in s:
            if stack != [] and stack[-1] == e:
                stack.pop()
                continue
            stack.append(e)
        return "".join(stack)

