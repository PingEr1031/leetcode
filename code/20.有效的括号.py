class Solution:
    def isValid(self, s: str) -> bool:
        left = "([{"
        right = ")]}"
        dic = {key: value for key, value in zip(left, right)}
        stack = []
        for e in s:
            if e in dic.keys():
                stack.append(e)
            elif e in dic.values():
                # 判断弹出的元素和
                k = stack.pop()
                if dic[k] == e:
                    continue
                else:
                    return False
        return True if stack else False


if __name__ == "__main__":
    s = "()"
    my_answer = Solution()
    my_answer.isValid(s)
