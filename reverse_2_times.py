n, x, y, a, b = input().split()
seq = [i for i in range(1, int(n) + 1)]
seq[int(x) - 1:int(y)] = seq[int(x) - 1:int(y)][::-1]
seq[int(a) - 1:int(b)] = seq[int(a) - 1:int(b)][::-1]
print(" ".join(map(str, seq)))