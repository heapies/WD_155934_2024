import math

def zadanie1():
    numbers_list = []
    while True:
        user_input = input("Wpisz liczbę lub 'end', aby zakończyć: ")

        if user_input.lower() == 'end':
            break

        if user_input.isdigit():
            numbers_list.append(int(user_input))
            print("Dodano liczbę do listy.")
        else:
            print("To nie jest liczba. Nie dodano do listy.")

    print("Lista liczb:", numbers_list)

def zadanie2():
    def monotonicznosc_funkcji(a, b):
        if a > 0:
            return "Funkcja jest rosnąca."
        elif a < 0:
            return "Funkcja jest malejąca."
        else:
            return "Funkcja jest stała."

    a1 = 2
    b1 = 1
    print("Dla y =", a1, "x +", b1, monotonicznosc_funkcji(a1, b1))

    a2 = 3
    b2 = 7
    print("Dla y =", a2, "x +", b2, monotonicznosc_funkcji(a2, b2))

    a3 = 6
    b3 = 9
    print("Dla y =", a3, "x +", b3, monotonicznosc_funkcji(a3, b3))

def zadanie3(a1, b1, a2, b2):
    if a1 == a2:
        return "Proste są równoległe."
    elif a1 * a2 == -1:
        return "Proste są prostopadłe."
    else:
        return "Proste nie są ani równoległe, ani prostopadłe."

def zadanie4(a=3, b=4):
    return math.sqrt(a ** 2 + b ** 2)

def suma_ciagu_arytmetycznego(a1=1, r=1, ile_elementow=10):
    suma = 0
    for i in range(ile_elementow):
        suma += a1 + i * r
    return suma

def dodaj_znak(lista_stringow):
    for i in range(len(lista_stringow)):
        lista_stringow[i] += "!"
    return lista_stringow

def dodaj_znak_nowa_lista(lista_stringow):
    nowa_lista = []
    for string in lista_stringow:
        nowa_lista.append(string + "!")
    return nowa_lista

def zadanie6a(lista_stringow):
    return dodaj_znak(lista_stringow)

def zadanie6b(lista_stringow):
    return dodaj_znak_nowa_lista(lista_stringow)

lista = ["Python", "to", "super"]
nowa_lista_a = zadanie6a(lista)
nowa_lista_b = zadanie6b(lista)

print("Oryginalna lista:", lista)
print("Nowa lista (zadanie 6a):", nowa_lista_a)
print("Nowa lista (zadanie 6b):", nowa_lista_b)

def main():
    zadanie1()
    zadanie2()
    a1 = 2
    b1 = 1
    a2 = 2
    b2 = 4
    print("Dla y =", a1, "x +", b1, "i y =", a2, "x +", b2, zadanie3(a1, b1, a2, b2))
    print("Długość przeciwprostokątnej dla a=3, b=4:", zadanie4())
    print("Suma ciągu arytmetycznego (a1=1, r=1, ile=10):", suma_ciagu_arytmetycznego())
    print("Suma ciągu arytmetycznego (a1=3, r=2, ile=5):", suma_ciagu_arytmetycznego(a1=3, r=2, ile_elementow=5))

main()
