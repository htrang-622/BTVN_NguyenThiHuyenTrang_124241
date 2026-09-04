import time

n = int(input("Nhập n: "))
x = float(input("Nhập x: "))

a = [1] * (n+1)


# Cách 1
start = time.time()

P1 = 0
for i in range(n + 1):
    P1 = P1 + a[i] * (x ** i)

end = time.time()
time1 = end - start


# Cách 2 - Horner
start = time.time()

P2 = a[n]
for i in range(n - 1, -1, -1):
    P2 = a[i] + x * P2

end = time.time()
time2 = end - start


print("\nKẾT QUẢ")
print("P(x) cách 1 =", P1)
print("Thời gian cách 1 =", time1, "giây")

print("P(x) cách 2 =", P2)
print("Thời gian cách 2 =", time2, "giây")

print("\nNhận xét:")
if time1 > time2:
    print("Cách 2 (Horner) nhanh hơn.")
else:
    print("Cách 1 nhanh hơn.")