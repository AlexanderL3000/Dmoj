class Solution:
    def solve(self, fractions):
        out = []
        for item in fractions:
            a = item[0]
            b = item[1]
            while b:
                a, b = b, a % b
            out.append([int(item[0]/a), int(item[1]/a)])

        out = set(tuple(element) for element in out)
        return sorted(list(out), key=lambda x: x[0] / x[1])
  