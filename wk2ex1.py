# Voorbeeldopgave lists, resultaat: [2, 7, 5, 9]

e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

answer0 = e[0:2] + pi[-2:]
print(answer0)

# Opgave 1: [7, 1] maken
answer1 = e[1:] 
print(answer1)

answer2 = pi[1:5:2] + e[0:1:1]
print(answer2)

answer3 = pi[1::]
print(answer3)

answer4 = e[::-2] + pi[::+2]
print(answer4)

# Oefeningen met strings

h = "hanze"
s = "hogeschool"
g = "groningen"

# Opgave 5:  'hoi' maken

answer5 = s[0:2] + g[4]
print(answer5)

#schoenen
answer6 = s[4:7] + s[1:4:2] + g[5:9:2] + g[-1]
print(answer6)

#anzeogeschool
answer7 = h[1::] + s[1:4] + s[4::]
print(answer7)

#gnagnahahahahaha
answer8 = 2*(g[0] + h[2] +h[1]) + 5*(h[0:2])
print(answer8)

#legonoego
answer9 = 1
print(answer9)

#leggings
answer10 = 1
print(answer10)