import sys

def zadanie1(zdanie):
    zdanie = zdanie.strip()
    slowo = zdanie.split()
    return len(slowo)

def zadanie2():
    print(f"Wprowadź a")
    a = float(sys.stdin.readline())
    print(f"Wprowadź b")
    b = float(sys.stdin.readline())
    print(f"Wprowadź c")
    c = float(sys.stdin.readline())
    d=a**b+c
    print(f"wynik działania {d}")

    with open("plik.txt", "w") as file:
        file.write(f"Wynik działania to {d}.\n")

def zadanie3(slowo):
    slowo = slowo.lower().replace(" ", "")
    return slowo == slowo[::-1]

def zadanie4(lp):
    for i in range(2,lp):
        if lp % i == 0:
            print("podana liczba nie jest liczbą pierwszą")
            break
        else:
            print("podana liczba jest liczbą pierwszą")
            break

def zadanie6():
    x = [r.randint(1, 100), r.uniform(1.0, 100.0), r.randint(1, 100), r.uniform(5.0, 50.0)]
    print(x)
    for i in range(0, len(x)):
        x[i] = m.pow(x[i], 2)
    print(x)

def zadanie7():
    i = 0
    listaP = []
    while i < 11:
        a = int(input("podaj liczbe "))
        if a % 2 == 0:
            listaP.append(a)
            i += 1
        else:
            i += 1
            continue

    print(f"lista parzystych to {listaP}")


def main():
    wprowadzone_slowo = input("Wprowadź zdanie: ")

    policz = zadanie1(wprowadzone_slowo)

    print("Liczba słów w zdaniu:", policz)

    #zadanie2()

    slowo_od_uzykownika = input("podaj jakiś palindrom ")

    if zadanie3(slowo_od_uzykownika):
        print("słowo jest palindromem ")
    else:
        print("to nie palindrom ")

    lp = int(input("Podaj liczbe do sprawdzenia czy jest liczbą pierwszą: "))

    zadanie4(lp)
    zadanie6()
    zadanie7()


if __name__ == "__main__":
    main()
