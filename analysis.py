from uncertainties import ufloat
from uncertainties.umath import *

data = {
  (-45, -22.5): 490,
  (-45, 22.5): 107,
  (-45, 67.5): 92,
  (-45, 112.5): 532,
  (0, -22.5): 531,
  (0, 22.5): 540,
  (0, 67.5): 109,
  (0, 112.5): 133,
  (45, -22.5): 134,
  (45, 22.5): 554,
  (45, 67.5): 561,
  (45, 112.5): 208,
  (90, -22.5): 73,
  (90, 22.5): 94,
  (90, 67.5): 566,
  (90, 112.5): 519
}

def N(a,b):
  if (a,b) in data.keys():
    return ufloat(data[(a,b)], sqrt(data[(a,b)]))
  elif (b,a) in data.keys():
    return ufloat(data[(b,a)], sqrt(data[(b,a)]))
  else:
    return data[(a,b)] # throws error

num1 = N(0, -22.5) + N(90, 67.5) - N(0, 67.5) - N(90, -22.5)
den1 = N(0, -22.5) + N(90, 67.5) + N(0, 67.5) + N(90, -22.5)
e2 = num1 / den1

num2 = N(0, 22.5) + N(90, 112.5) - N(0, 112.5) - N(90, 22.5)
den2 = N(0, 22.5) + N(90, 112.5) + N(0, 112.5) + N(90, 22.5)
e3 = num2 / den2

num3 = N(45, -22.5) + N(-45, 67.5) - N(45, 67.5) - N(-45, -22.5)
den3 = N(45, -22.5) + N(-45, 67.5) + N(45, 67.5) + N(-45, -22.5)
e4 = num3 / den3

num4 = N(45, 22.5) + N(-45, 112.5) - N(45, 112.5) - N(-45, 22.5)
den4 = N(45, 22.5) + N(-45, 112.5) + N(45, 112.5) + N(-45, 22.5)
e1 = num4 / den4

print e1
print e2
print e3
print e4
print e1 + e2 + e3 - e4 
