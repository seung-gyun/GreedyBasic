n, m = map(int, input().split())
money = []

for i in range(n):
    money.append(int(input()))

count = 0

for i in reversed(range(n)):
    if m >= money[i]:
        count+= m//money[i]
        m = m%money[i]

print(count)