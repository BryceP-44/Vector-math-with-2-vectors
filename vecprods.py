print("Vector math with 2 vectors")
from math import *
while True:
    #manual input
    #va = "5,6,7"
    #vb = "8,9,0"

    #command line imput
    va = input("Vector A. Enter vector as    x,y,z: ")
    vb = input("Vector B. Enter vector as    x,y,z: ")
    
    #splice data at the commas
    data = va.split(",")
    i1 = data[0]
    j1 = data[1]
    k1 = data[2]

    #convert spliced strings to floats
    i1 = float(i1)
    j1 = float(j1)
    k1 = float(k1)
    
    #splice data at the commas
    data = vb.split(",")
    i2 = data[0]
    j2 = data[1]
    k2 = data[2]
    
    #convert spliced strings to floats
    i2 = float(i2)
    j2 = float(j2)
    k2 = float(k2)

    #addition
    addi = i1+i2
    addj = j1+j2
    addk = k1+k2
    addmag = (addi**2 + addj**2 + addk**2)**.5

    #subtraction
    subi = i1-i2
    subj = j1-j2
    subk = k1-k2
    submag = (subi**2 + subj**2 + subk**2)**.5

    #dot product
    dot = (i1*i2)+(j1*j2)+(k1*k2)

    #cross product
    crossi = (j1*k2 - k1*j2)
    crossj = (-1*(i1*k2 - k1*i2))
    crossk = (i1*j2 - j1*i2)

    #magnitudes of original vectors
    a = ((i1**2)+(j1**2))**.5
    a = (a**2+k1**2)**.5
    b = ((i2**2)+(j2**2))**.5
    b = (b**2+k2**2)**.5

    #angle
    dottheta = (dot)/(a*b)
    dottheta = (acos(dottheta)) * (180/pi)

    #magnitude of cross product resultant vector
    c = ((crossi**2)+(crossj**2))**.5
    c = (c**2+crossk**2)**.5

    #angle
    crosstheta = c/(a*b)
    crosstheta = (asin(crosstheta)) * (180/pi)

    print("Original vectors: [", va, "]        [", vb, "]\n")
    print("vector a magnitude: ", a, "    vector b magnitude: ", b)
    print("Cross product: [",crossi, ",", crossj, ",", crossk, "]", "    magnitude: ", c)
    print("Dot product: ", dot)
    print("Angle between vectors: ", dottheta, "degrees")
    print("Addition: ", addi, addj, addk, "    magnitude: ", addmag)
    print("Subtraction: ", subi, subj, subk, "    magnitude: ", submag)
    print(" ")





