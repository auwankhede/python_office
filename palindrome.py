'''
Write a version of a palindrome recogniser that accepts a file name from the user,
reads each line, and prints the line to the screen if it is a palindrome.
'''


def palindrome(o,r):
    if o == r:
        print("Word is palindrome",o)

        
with open("input.txt") as inputConnection:
    for line in inputConnection:
        #print(line)
        reverse=line[::-1]
        palindrome(line.replace('\n',''),reverse.replace('\n',''))        


        
