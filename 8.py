chislo = int(input('Введите число: '))
base = int(input("Введите систему счисления: "))
def convert(chislo, base):
    if not(2 == base or base == 8):
        return "Неправильная система счисления"
        quit()
    converted = ''
    while chislo > 0:
        converted = str(chislo % base) + converted

        chislo //= base
 
    return converted
print(str(chislo) + '=>' + str(convert(chislo, base)))
