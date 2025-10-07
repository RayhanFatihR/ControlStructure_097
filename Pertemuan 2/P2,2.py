a = float(input("Masukkan nilai pertama:"))
b = float(input("Masukkan nilai kedua:"))
c = float(input("Masukkan nilai ketiga:"))

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c
else :
    largest = print("Tidak ada angka terbesar")

print("Angka terbesar adalah:", largest)