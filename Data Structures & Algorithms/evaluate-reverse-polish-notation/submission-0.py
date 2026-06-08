class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = []
        nums = []
        op = set({"+", "-", "*", "/"})

        def _eval(token):
            n2 = nums.pop()
            n1 = nums.pop()
            if token == '+':
                nums.append(n1+n2)
            elif token == '-':
                nums.append(n1-n2)
            elif token == '*':
                nums.append(n1 * n2)
            else:
                if (n1 * n2 < 0):
                    nums.append(-1* (abs(n1)//abs(n2)))
                else:
                    nums.append(n1//n2)
        i = 0
        n = len(tokens)

        while i < n:
            if tokens[i] in op:
                _eval(tokens[i])
            else:
                nums.append(int(tokens[i]))
            i += 1

        return nums[0]