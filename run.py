import pyqrcode
import random

f= open("proto-5/lot.txt","w+")

k = "06092018"
s = "SMAV"

for i in range(1, 600):
    if(i < 10):
        x = 2
    elif(i < 100):
        x = 1
    else:
        x = 0

    folder = "one"
    if(i>200):folder = "two"
    if(i>300):folder = "three"
    if(i>400):folder = "four"
    if(i>500):folder = "five"
    if(i>600):folder = "six"
    
    s = ''.join(random.sample(s,len(s)))
    k = ''.join(random.sample(k,len(k)))
    text = s + "-"+ k + "-" + "0" * x + str(i)
    file = "proto-5/" + folder + "/" + text + ".png"
    qr = pyqrcode.create(text)
    qr.png(file, scale=7)
    qr.png("proto-5/" + "all" + "/" + text + ".png", scale=7)
    print(file)
    f.write(text+"\n")
