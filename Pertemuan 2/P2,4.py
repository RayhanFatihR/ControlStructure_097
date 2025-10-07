n = int(input("Masukkan nilai n untuk mencetak bilangan ganjil:"))

print("Bilangan ganjil hingga", n, ":")
for i in range(1, n + 1, 2):
    print(i, end=" ")