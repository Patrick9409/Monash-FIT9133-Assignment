'''
9133 Python Assignment 1.1
'''
morseCode = {'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0',
             'F': '0010', 'G': '110', 'H': '0000', 'I': '00', 'J': '0111',
             'K': '101', 'L': '0100', 'M': '11', 'N': '10', 'O': '111',
             'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1',
             'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011',
             'Z': '1100', '0': '11111', '1': '01111', '2': '00111', '3': '00011',
             '4': '00001', '5': '00000', '6': '10000', '7': '11000', '8': '11100',
             '9': '11110'}

'''
9133 Python Assignment 1.2

userInput = input("Please input the String which will be used to convert to Morese Code")
str = ""
for i in range(len(userInput)):
    if i != len(userInput) - 1:
        str = str + morseCode.get(userInput[i]) + '***'
    else:
        str = str + morseCode.get(userInput[i])
print(str)
'''
'''
9133 Python Assignment 1.3

def decode(str):
    for j in range(len(str.split('***'))):
        for i in morseCode:
            if morseCode.get(i) == str.split('***')[j]:
                print(i)

str = input("Please input the MorseCode")
decode(str)
'''
'''
9133 Python Assignment 1.4
'''
def newDecode(str, list1):
    for i in str.split('***'):
        for j in morseCode:
            if morseCode.get(j) == i:
                print(j)
                signature = 0
                if len(list1) == 0:
                    list1 = {j: 1}
                else:
                    for k in list(list1):
                        if j == k:
                            list1[j] = list1[j] + 1
                            signature = 1
                        if signature == 0:
                            list1[j] = 1
    return list1


stopSignature = 0
list1 = {}
while stopSignature == 0:
    str = input("Please input the MorseCode")
    list1 = newDecode(str, list1)
    stopSignature = int(input("If want to exit system, input 1, otherwise input 0"))
print(list1)