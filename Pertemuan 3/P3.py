def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32  
    elif unit.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("Unit harus 'C' or 'F'")    

print("====== Konversi Suhu ======")  
try:
    input_suhu = float(input("Masukkan nilai suhu:"))
    unit = input("Masukkan satuan suhu ('C' untuk celsius atau 'f' untuk fahrenheit): ")
    konversi = convert_temperature(input_suhu, unit)
    