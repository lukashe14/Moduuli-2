import random

kolminumeroinen_koodi = ""
for _ in range(3):
    kolminumeroinen_koodi += str(random.randint(0,9))


nelinumeroinen_koodi = ""
for _ in range(4):
    nelinumeroinen_koodi += str(random.randint(0,6))

print("kolmenumeroinen koodi:", kolminumeroinen_koodi)
print("nelinumeroinen_koodi:", nelinumeroinen_koodi)