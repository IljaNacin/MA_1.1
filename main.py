import random
"the random module allows me to create a set of dice rolls, created by pseudo-random values"
import math
"the math module is necessary for combinations, aka the nCr formula"

L = [1, 2, 3, 4, 5, 6]
"This list serves as the domain of numbers which I want the random module to choose from."
"Naturally, It's the numbers 1-6, which represent the six die-face values"

p1 = random.choice(L)
p2 = random.choice(L)
p3 = random.choice(L)
p4 = random.choice(L)
p5 = random.choice(L)
"This block of code picks pseudo-random numbers, from the previously defined list, and assigns the variables"

R = [p1, p2, p3, p4, p5]
"This new list of random values represents the player's deck"

print(" ")
print("your dice rolls:", *R)

amountone = R.count(1)
amounttwo = R.count(2)
amountthree = R.count(3)
amountfour = R.count(4)
amountfive = R.count(5)
amountsix = R.count(6)
"This block counts the amount of face values on the player's deck, and assigns them variables"

print(" ")
print("[ amount of your dice values ->", "ones:", amountone, ",", "twos:", amounttwo, ",", "threes:", amountthree, ",", "fours:", amountfour, ",", "fives:", amountfive, ",", "sixes:", amountsix,"]")
print(" ")

fifteen = (math.comb(15, 15) * ((1 / 6) ** 15) * ((5 / 6) ** (15 - 15)))
fourteen = (math.comb(15, 14) * ((1 / 6) ** 14) * ((5 / 6) ** (15 - 14)))
thirteen = (math.comb(15, 13) * ((1 / 6) ** 13) * ((5 / 6) ** (15 - 13)))
twelve = (math.comb(15, 12) * ((1 / 6) ** 12) * ((5 / 6) ** (15 - 12)))
eleven = (math.comb(15, 11) * ((1 / 6) ** 11) * ((5 / 6) ** (15 - 11)))
ten = (math.comb(15, 10) * ((1 / 6) ** 10) * ((5 / 6) ** (15 - 10)))
nine = (math.comb(15, 9) * ((1 / 6) ** 9) * ((5 / 6) ** (15 - 9)))
eight = (math.comb(15, 8) * ((1 / 6) ** 8) * ((5 / 6) ** (15 - 8)))
seven = (math.comb(15, 7) * ((1 / 6) ** 7) * ((5 / 6) ** (15 - 7)))
six = (math.comb(15, 6) * ((1 / 6) ** 6) * ((5 / 6) ** (15 - 6)))
five = (math.comb(15, 5) * ((1 / 6) ** 5) * ((5 / 6) ** (15 - 5)))
four = (math.comb(15, 4) * ((1 / 6) ** 4) * ((5 / 6) ** (15 - 4)))
three = (math.comb(15, 3) * ((1 / 6) ** 3) * ((5 / 6) ** (15 - 3)))
two = (math.comb(15, 2) * ((1 / 6) ** 2) * ((5 / 6) ** (15 - 2)))
one = (math.comb(15, 1) * ((1 / 6) ** 1) * ((5 / 6) ** (15 - 1)))
"This big block is the main calculation bit. Each of the terms represents the chance of a particular event happening"
"How I got to these calculations will be elaborated in the actual thesis paper"
"Each of the probabilities gets assigned to a variable"

alone = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight+seven+six+five+four+three+two+one)
altwo = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight+seven+six+five+four+three+two)
althree = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight+seven+six+five+four+three)
alfour = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight+seven+six+five+four)
alfive = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight+seven+six+five)
alsix = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight+seven+six)
alseven = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight+seven)
aleight = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine+eight)
alnine = (fifteen+fourteen+thirteen+twelve+eleven+ten+nine)
alten = (fifteen+fourteen+thirteen+twelve+eleven+ten)
aleleven = (fifteen+fourteen+thirteen+twelve+eleven)
altwelve = (fifteen+fourteen+thirteen+twelve)
althirteen = (fifteen+fourteen+thirteen)
alfourteen = (fifteen+fourteen)
alfifteen = fifteen
"This part adds the probabilities together, so that we get values which signify how many dice we get AT LEAST"
"Solely getting the exact probabilities of certain events wouldn't be as useful for the player"

print(' ')
print("=== Probabilities of rolling 1's ===")
print(" ")
if amountone == 0:
    print("one 1:", alone)
if amountone >= 1:
    print("one 1:", 1)

"Each of these boxes serve as different exit values, depending on whether a certain starting condition is met"
"They analyze the amount of 1's and then decide, which probability they want to assign to the event"

"This entire column of code is only responsible for the amount of 1's"
"Adding the other values would simply require me to copy-paste this column and replace the amountone with amount(x)"

if amountone == 0:
    print("two 1's:", altwo)
if amountone == 1:
    print("two 1's:", alone)
if amountone >= 2:
    print("two 1's:", 1)

if amountone == 0:
    print("three 1's:", althree)
if amountone == 1:
    print("three 1's:", altwo)
if amountone == 2:
    print("three 1's:", alone)
if amountone >= 3:
    print("three 1's:", 1)

if amountone == 0:
    print("four 1's:", alfour)
if amountone == 1:
    print("four 1's:", althree)
if amountone == 2:
    print("four 1's:", altwo)
if amountone == 3:
    print("four 1's:", alone)
if amountone >= 4:
    print("four 1's:", 1)

if amountone == 0:
    print("five 1's:", alfive)
if amountone == 1:
    print("five 1's:", alfour)
if amountone == 2:
    print("five 1's:", althree)
if amountone == 3:
    print("five 1's:", altwo)
if amountone == 4:
    print("five 1's:", alone)
if amountone >= 5:
    print("five 1's:", 1)

if amountone == 0:
    print("six 1's:", alsix)
if amountone == 1:
    print("six 1's:", alfive)
if amountone == 2:
    print("six 1's:", alfour)
if amountone == 3:
    print("six 1's:", althree)
if amountone == 4:
    print("six 1's:", altwo)
if amountone == 5:
    print("six 1's:", alone)

if amountone == 0:
    print("seven 1's:", alseven)
if amountone == 1:
    print("seven 1's:", alsix)
if amountone == 2:
    print("seven 1's:", alfive)
if amountone == 3:
    print("seven 1's:", alfour)
if amountone == 4:
    print("seven 1's:", althree)
if amountone == 5:
    print("seven 1's:", altwo)

if amountone == 0:
    print("eight 1's:", aleight)
if amountone == 1:
    print("eight 1's:", alseven)
if amountone == 2:
    print("eight 1's:", alsix)
if amountone == 3:
    print("eight 1's:", alfive)
if amountone == 4:
    print("eight 1's:", alfour)
if amountone == 5:
    print("eight 1's:", althree)

if amountone == 0:
    print("nine 1's:", alnine)
if amountone == 1:
    print("nine 1's:", aleight)
if amountone == 2:
    print("nine 1's:", alseven)
if amountone == 3:
    print("nine 1's:", alsix)
if amountone == 4:
    print("nine 1's:", alfive)
if amountone == 5:
    print("nine 1's:", alfour)

if amountone == 0:
    print("ten 1's:", alten)
if amountone == 1:
    print("ten 1's:", alnine)
if amountone == 2:
    print("ten 1's:", aleight)
if amountone == 3:
    print("ten 1's:", alseven)
if amountone == 4:
    print("ten 1's:", alsix)
if amountone == 5:
    print("ten 1's:", alfive)

if amountone == 0:
    print("eleven 1's:", aleleven)
if amountone == 1:
    print("eleven 1's:", alten)
if amountone == 2:
    print("eleven 1's:", alnine)
if amountone == 3:
    print("eleven 1's:", aleight)
if amountone == 4:
    print("eleven 1's:", alseven)
if amountone == 5:
    print("eleven 1's:", alsix)

if amountone == 0:
    print("twelve 1's:", altwelve)
if amountone == 1:
    print("twelve 1's:", aleleven)
if amountone == 2:
    print("twelve 1's:", alten)
if amountone == 3:
    print("twelve 1's:", alnine)
if amountone == 4:
    print("twelve 1's:", aleight)
if amountone == 5:
    print("twelve 1's:", alseven)

if amountone == 0:
    print("thirteen 1's:", althirteen)
if amountone == 1:
    print("thirteen 1's:", altwelve)
if amountone == 2:
    print("thirteen 1's:", aleleven)
if amountone == 3:
    print("thirteen 1's:", alten)
if amountone == 4:
    print("thirteen 1's:", alnine)
if amountone == 5:
    print("thirteen 1's:", aleight)

if amountone == 0:
    print("fourteen 1's:", alfourteen)
if amountone == 1:
    print("fourteen 1's:", althirteen)
if amountone == 2:
    print("fourteen 1's:", altwelve)
if amountone == 3:
    print("fourteen 1's:", aleleven)
if amountone == 4:
    print("fourteen 1's:", alten)
if amountone == 5:
    print("thirteen 1's:", alnine)

if amountone == 0:
    print("fifteen 1's:", alfifteen)
if amountone == 1:
    print("fifteen 1's:", alfourteen)
if amountone == 2:
    print("fifteen 1's:", althirteen)
if amountone == 3:
    print("fifteen 1's:", altwelve)
if amountone == 4:
    print("fifteen 1's:", aleleven)
if amountone == 5:
    print("fifteen 1's:", alten)

if amountone == 0:
    print("sixteen 1's:", 0)
if amountone == 1:
    print("sixteen 1's:", alfifteen)
if amountone == 2:
    print("sixteen 1's:", alfourteen)
if amountone == 3:
    print("sixteen 1's:", althirteen)
if amountone == 4:
    print("sixteen 1's:", altwelve)
if amountone == 5:
    print("sixteen 1's:", aleleven)

if amountone == 0:
    print("seventeen 1's:", 0)
if amountone == 1:
    print("seventeen 1's:", 0)
if amountone == 2:
    print("seventeen 1's:", alfifteen)
if amountone == 3:
    print("seventeen 1's:", alfourteen)
if amountone == 4:
    print("seventeen 1's:", althirteen)
if amountone == 5:
    print("seventeen 1's:", altwelve)

if amountone == 0:
    print("eighteen 1's:", 0)
if amountone == 1:
    print("eighteen 1's:", 0)
if amountone == 2:
    print("eighteen 1's:", 0)
if amountone == 3:
    print("eighteen 1's:", alfifteen)
if amountone == 4:
    print("eighteen 1's:", alfourteen)
if amountone == 5:
    print("eighteen 1's:", althirteen)

if amountone == 0:
    print("nineteen 1's:", 0)
if amountone == 1:
    print("nineteen 1's:", 0)
if amountone == 2:
    print("nineteen 1's:", 0)
if amountone == 3:
    print("nineteen 1's:", 0)
if amountone == 4:
    print("nineteen 1's:", alfifteen)
if amountone == 5:
    print("nineteen 1's:", alfourteen)

if amountone == 0:
    print("twenty 1's:", 0)
if amountone == 1:
    print("twenty 1's:", 0)
if amountone == 2:
    print("twenty 1's:", 0)
if amountone == 3:
    print("twenty 1's:", 0)
if amountone == 4:
    print("twenty 1's:", 0)
if amountone == 5:
    print("twenty 1's:", alfifteen)