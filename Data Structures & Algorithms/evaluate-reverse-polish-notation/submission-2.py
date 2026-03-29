class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []
        operations = ['*','-','/','+']

        for n in tokens:

            if n in operations:
                n1 = s.pop()
                n2 = s.pop()
                if n == '*':
                    s.append(n2 * n1)
                elif n == '-':
                    s.append(n2 - n1)
                elif n == '/':
                    s.append(int((n2 /n1)))
                elif n == '+':
                    s.append(n2 + n1)

            else:

                s.append(int(n))

        return s.pop()

        