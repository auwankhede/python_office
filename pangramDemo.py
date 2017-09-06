def checkPangram(str):
    strAtoZ ="abcdefghijklmnopqrstuvwxyz"
    flag = True;
    for letter in strAtoZ:
        #print(letter)
        flag = False
        for inputLetter in str:
            if letter == inputLetter:
                flag = True
                #print(letter ," matches ",inputLetter)
                break

    return flag;
#print(checkPangram("The quick brown fox jumps over the lazy dog"))
print("Paragram status :",checkPangram("abcdefghijklmnopqrstuvwxyz") )
print("Paragram status :",checkPangram("The quick brown fox jumps over the lazy dog") )
