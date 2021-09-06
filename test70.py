
tempFascii= ord('F')
# print(tempFascii)

tempdascii=ord('d')
divide= tempFascii /tempFascii
divideint= int(divide)
print(divideint)

def printonetoh(divideint,tempdascii):
    if (divideint<=tempdascii):
        divideint = divideint + 1
        print(divideint)
        printonetoh(divideint,tempdascii)

printonetoh(divideint,tempdascii)
