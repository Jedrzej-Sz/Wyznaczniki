print("Metoda wyznacznikowa")
a1 = float(input("Wpisz a1: "))#inputy
b1 = float(input("Wpisz b1: "))
c1 = float(input("Wpisz c1: "))
a2 = float(input("Wpisz a2: "))
b2 = float(input("Wpisz b2: "))
c2 = float(input("Wpisz c2: "))
w = (a1 * b2) - (a2 * b1) #Główny wyznacznik W
wx = (c1 * b2) - (c2 * b1) #Wyznacznik Wx
wy = (a1 * c2) - (a2 * c1)#Wyznacznik Wy
if w != 0:
    print("Jest jedno rowiązanie")
    print("a wynosi: " + str(wx/w))
    print("b wynosi: " + str(wy/w))
    print("Wyznacznik główny wynosi: " + str(w))
elif w==0 and wx==0 and wy==0:
    print("Równanie nieoznaczone, ilość rozwiązań nieograniczona")
    print("a wynosi: " + str(wx/w))
    print("b wynosi: " + str(wy/w))
    print("Wyznacznik główny wynosi: " + str(w))
elif w == 0 and (wx != 0 or wy != 0):
    print("Równanie sprzeczne, brak rozwiązań")
else:
    print('błąd')