leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

grammat1 = leiviskät * 20 * 32 * 13.3
grammat2 = naulat * 32 * 13.3
grammat3 = luodit * 13.3

kaikkigrammat = grammat1 + grammat2 + grammat3
kilo = int(kaikkigrammat // 1000)
loputgrammat = kaikkigrammat % 1000
print("Massa nykymittojen mukaan:")
print(f"{kilo} kilogrammaa ja {loputgrammat:.2f} grammaa")

