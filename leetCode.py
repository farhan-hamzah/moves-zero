nums = list(map(int, input().split()))
hasil = []
b = 0
for i in nums:
    if i != 0:
        hasil.append(i)
    else:
        b += 1
while b > 0:
    hasil.append(0)
    b -= 1
print(hasil)