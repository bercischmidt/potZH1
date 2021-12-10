def dij(km):
    if km == 1:
        return (300)
    elif km < 1:
        return (km * 300)
    else:
        return (1800)


print('1. feladat: A tavok.txt beolvasása.')
utak = []
fbe = open('tavok.txt', 'r')
for sor in fbe:
    s = sor.split()
    utak.append([int(s[0]), int(s[1]), int(s[2])])
fbe.close()
utak.sort()

print('2. feladat: A hét első útja', utak[0][2], 'km hosszú volt.')

"""for utak in range:
    nsorszam = utak[0]
    fsorszam= utak[1]"""
# Ezt nem sikerült megcsinálnom
"""nsorszam = int(input('3. feladat: Adja meg a nap sorszámát (1-7): '))
fsorszam = int(input('3. feladat: Adja meg a fuvar sorszámát (1-40): '))
print('A(z) ', nsorszam, '. nap ', fsorszam, '. fuvarához ',
      utak[nsorszam][fsorszam][2], 'km került rögzítésre.')"""

fuvarok = [0] * 8
tavok = [0] * 8
for ut in utak:
    fuvarok[ut[0]] += 1
    tavok[ut[0]] += ut[2]
print('4. feladat: A futár nem dolgozott ezen nap(ok)on:', end=' ')
for i in range(1, 8):
    if fuvarok[i] == 0:
        print(i, end=' ')
print()
nap = fuvarok.index(max(fuvarok))
print('5. feladat: Ezen nap(ok)on volt a maximális számú fuvar:', nap, '\b.')
print('--- 6. feladat ---')
for i in range(1, 8):
    print(i, '. nap:', tavok[i], 'km')

print('7. feladat: Fuvarok ellenértékének meghatározása.')
heti = 0
fki = open('dijazas.txt', 'w')
for ut in utak:
    nap = ut[0]
    fuvar = ut[1]
    ar = dij(ut[2])
    heti += int(ar)
    fki.write(str(nap) + '. nap ' + str(fuvar) + '. út: ' + str(ar) + ' Ft\n')
fki.close()
print('8. feladat: A futár a heti fizetése', heti, 'Ft.')
