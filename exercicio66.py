n = 0
s = 0 
v = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    v = v + 1
    s = s + n
print(f'A soma entre os {v} numeros vale {s}')